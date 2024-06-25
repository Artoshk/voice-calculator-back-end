<h1> Voice Calculator Back End </h1>

<h2> Project: Final CI/CD Project </h2>

**Team:**
Anderson Karl,
Isaías Fontes,
Pedro Henrique and
Saynarah Nabuco

## Description

This project the back-end of a voice calculator, that uses the Whisper and OpenAI GPT-3.5 to calculate the result of a math expression given by the user in portuguese language. The back-end was a REST API developed using FastAPI.

## Dependencies

The project was developed using `Python >= 3.11`, the other dependencies are in the `requirements.txt` file.
Is necessary to add the credentials to `OpenAI` in the `.env` file inside the `src` folder.

## How to run

To run the project, you need to install the dependencies using the command `pip install -r requirements.txt` and then run the command `python src/main.py`.

You can also use docker to run the project, using the command `docker build -t voice-calculator-back-end -f docker/dockerfile .` to build the image and `docker run -p 8000:8000 voice-calculator-back-end` to run the container.

## Tips

To test the API, you can use the Swagger interface that is available in the route `/docs`.