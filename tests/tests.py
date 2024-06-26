from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app

# Initialize TestClient
client = TestClient(app)

def test_process_audio():
    # Load a sample audio file for testing
    with open("tests/audio_pass.wav", "rb") as audio_file:
        response = client.post("/process_audio", files={"audio": audio_file})
    
    assert response.status_code == 200
    result = response.json()
    assert result["result"] == " 25 vezes 35 dividido por 2.\n\n25*35/2 = 437.5"
    
def test_process_audio_invalid():
    # Load a sample audio file for testing
    with open("tests/audio_fail.mp3", "rb") as audio_file:
        response = client.post("/process_audio", files={"audio": audio_file})
    
    assert response.status_code == 200
    result = response.json()
    assert "Operação não suportada" in result["result"]
    
def test_process_audio_unsupported_operation():
    # Load a sample audio file for testing
    with open("tests/not_audio_file.wav", "rb") as audio_file:
        response = client.post("/process_audio", files={"audio": audio_file})
    
    assert response.status_code == 422
    result = response.json()
    assert "Operação não suportada" in result['detail']

def test_process_equation_valid():
    form_data = {
        'equation': '2 + 2'
    }
    response = client.post("/process_equation", data=form_data)
    assert response.status_code == 200
    result = response.json()
    assert result["result"] == "2 + 2 = 4"

def test_process_equation_invalid():
    form_data = {
        'equation': '2 / 0'
    }
    response = client.post("/process_equation", data=form_data)
    assert response.status_code == 422
    result = response.json()
    assert result["detail"] == "division by zero"

def test_process_equation_unsupported_operation():
    form_data = {
        'equation': 'unsupported operation'
    }
    response = client.post("/process_equation", data=form_data)
    assert response.status_code == 422
    result = response.json()
    assert "invalid syntax" in result["detail"]