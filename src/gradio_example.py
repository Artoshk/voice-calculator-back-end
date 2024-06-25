import gradio as gr
from transformers import pipeline
import numpy as np
import torch
from llm import process_natural_language

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# The modes was stored on C:\Users\{user}\.cache\huggingface\hub\
transcriber = pipeline(
    "automatic-speech-recognition", 
    model="openai/whisper-small",
    # Lighter models if you don't have a GPU, from heaviest to lightest 
    # whisper-small > whisper-base > whisper-tiny
    generate_kwargs={"language": "portuguese"},
    device=device,
    batch_size=1,
    chunk_length_s=30,
    framework="pt"
    )

def transcribe(audio) -> str:
    if audio is None:
        return ""
    
    sr, y = audio
    y = y.astype(np.float32)
    y /= np.max(np.abs(y))

    transcription = transcriber({"sampling_rate": sr, "raw": y})["text"]
    
    equation = process_natural_language(transcription)

    if equation == "Operação não suportada":
        return transcription + "\n\n" + equation
    
    result = transcription + "\n\n" + equation + " = " + str(eval(equation))
    return result


demo = gr.Interface(
    transcribe,
    gr.Audio(sources=["microphone"]),
    "text",
)

demo.launch()