from fastapi import FastAPI, File, Form, HTTPException, Security, Depends
from fastapi.middleware.cors import CORSMiddleware
import torch
from transformers import pipeline
import torchaudio
import io
from llm import process_natural_language
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi.security.api_key import APIKeyHeader
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()

# Configure CORS
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LANGUAGE = "portuguese"
BATCH_SIZE = 1 # Sequential reading for now
model_name_or_path = "openai/whisper-small"


API_KEY_NAME = "VOICE_CALCULATOR_API_KEY"
API_KEY = os.getenv("VOICE_CALCULATOR_KEY")  # Replace with your actual API key
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header
    raise HTTPException(status_code=403, detail="Could not validate API key")

device = "cuda" if torch.cuda.is_available() else "cpu"
model = pipeline(
    "automatic-speech-recognition",
    model=model_name_or_path,
    generate_kwargs={"language": LANGUAGE},
    device=device,
    batch_size=BATCH_SIZE,
    chunk_length_s=30,
    framework="pt"
    )
print(f"Model loaded on {device}")


@app.post("/process_audio")
async def process_audio(audio: bytes = File(...), api_key: str = Depends(get_api_key)):
    try:
        audio, sr = torchaudio.load(io.BytesIO(audio))
        stream = audio[0].numpy()
        transcription = model({"sampling_rate": sr, "raw": stream})["text"]
            
        equation = process_natural_language(transcription)
            
        if equation == "Operação não suportada":
            return {"result": transcription + "\n\n" + equation}

        result = transcription + "\n\n" + equation + " = " + str(eval(equation))
        return {"result": result}
    except Exception as e:
        # Return 422 status code for invalid operations
        raise HTTPException(status_code=422, detail="Operação não suportada, cheque o formato do arquivo de áudio.")

@app.post("/process_equation")
def process_equation(equation: str = Form(...), api_key: str = Depends(get_api_key)):
    try: 
        eval_result = eval(equation)
        resp = equation + " = " + str(eval_result)
        return {"result": resp}
    except Exception as e:
        # Return 422 status code for invalid operations
        raise HTTPException(status_code=422, detail=str(e))