from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app

# Initialize TestClient
client = TestClient(app)

def should_process_audio():
    # Arrange
    with open("tests/audio_pass.wav", "rb") as audio_file:
        # Act
        response = client.post("/process_audio", files={"audio": audio_file})
    # Assert
    assert response.status_code == 200
    result = response.json()
    assert result["result"] == " 25 vezes 35 dividido por 2.\n\n25*35/2 = 437.5"
    
def should_not_process_invalid_audio():
    # Arrange
    with open("tests/audio_fail.wav", "rb") as audio_file:
        # Act
        response = client.post("/process_audio", files={"audio": audio_file}) 
    # Assert
    assert response.status_code == 200
    result = response.json()
    assert "Operação não suportada" in result["result"]
    
def should_not_process_files_that_are_not_audio():
    # Arrange
    with open("tests/not_audio_file.wav", "rb") as audio_file:
        # Act
        response = client.post("/process_audio", files={"audio": audio_file})
    # Assert
    assert response.status_code == 422
    result = response.json()
    assert "Operação não suportada" in result['detail']

def should_add_numbers():
    # Arrange
    form_data = {
        'equation': '2 + 2'
    }
    # Act
    response = client.post("/process_equation", data=form_data)
    # Assert
    assert response.status_code == 200
    result = response.json()
    assert result["result"] == "2 + 2 = 4"

def should_not_divide_by_zero():
    # Arrange
    form_data = {
        'equation': '2 / 0'
    }
    # Act
    response = client.post("/process_equation", data=form_data)
    # Assert
    assert response.status_code == 422
    result = response.json()
    assert result["detail"] == "division by zero"

def should_not_process_invalid_equation():
    # Arrange
    form_data = {
        'equation': 'unsupported operation'
    }
    # Act
    response = client.post("/process_equation", data=form_data)
    # Assert
    assert response.status_code == 422
    result = response.json()
    assert "invalid syntax" in result["detail"]