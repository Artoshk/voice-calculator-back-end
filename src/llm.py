from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key = str(os.getenv("OPENAI_KEY")),
    organization = str(os.getenv("OPENAI_ORG_KEY"))
)

model_name = "gpt-3.5-turbo"

system_role = f"""
Imagine que você é um grande matemático e foi cotado para converter transcrições de áudio em equações matemáticas. Essas equações estão em linguagem natural e você deve traduzi-las para uma expressão matemática em python. As operações suportadas são: adição(+), subtração(-), multiplicação(*) e divisão(/). Podem haver casos em que a transcrição não contenha nenhuma operação matemática.

Nunca retorne a resposta, apenas a expressão matemática.

Aqui estão alguns exemplos para orientar sua análise:

Texto: '45 vezes 2 mais 3'
Resposta:
45*2+3

Texto: '25 vezes 4 é igual a 125?'
Resposta:
25*4

Texto: "Quero a raiz quadrada de 9"
Resposta:
Operação não suportada

Texto: "É... dois mais cinco dividido por três"
Resposta:
2+5/3

Texto: 'Qual é a fórmula de báskara?'
Resposta:
Operação não suportada

Caso receba um texto vazio, retorne;
Resposta:
Operação não suportada

Agora, aplique a sua especialidade:
Resposta:
"""

def resp_to_string(string: str) -> str:
    string = string.replace("\n", "").replace("\t", "").replace("Resposta:", "")
    return string

def process_natural_language(text: str) -> str:
    if len(text) > 250:
        text = text[:250]
    
    messages = [
        {
            'role': 'system',
            'content': system_role
        },
        {
            'role': 'user',
            'content': text
        }]
    
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        max_tokens=200,        # The maximum number of tokens (words or subwords) in the generated response
        stop=None,              # The stopping sequence for the generated response, if any (not used here)
        temperature=0.01,        # The "creativity" of the generated response (higher temperature = more creative)
    )

    result = response.choices[0].message.content
    print(resp_to_string(result))
    return resp_to_string(result)
