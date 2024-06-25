from fastapi import FastAPI, File
from fastapi.middleware.cors import CORSMiddleware
import torch
from transformers import pipeline
import torchaudio
import io
from llm import process_natural_language

app = FastAPI()

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


device = "cuda" if torch.cuda.is_available() else "cpu"
model = pipeline(
    "automatic-speech-recognition",
    model=model_name_or_path,
        generate_kwargs={"language": LANGUAGE},
        device=0 if device == "cuda" else -1,
        batch_size=BATCH_SIZE,
        chunk_length_s=30,
        framework="pt"
    )
print(f"Model loaded on {device}")


@app.post("/process_audio")
async def process_audio(audio: bytes = File(...)):
    audio, sr = torchaudio.load(io.BytesIO(audio))
    stream = audio[0].numpy()
    transcription = model({"sampling_rate": sr, "raw": stream})["text"]
        
    equation = process_natural_language(transcription)
        
    if equation == "Operação não suportada":
        return transcription + "\n\n" + equation

    result = transcription + "\n\n" + equation + " = " + str(eval(equation))
    return {"result": result}

@app.post("/process_equation")
def process_equation(equation: str):
    return {"result": equation + " = " + str(eval(equation))}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)