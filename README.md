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

To run the project, you need to install the dependencies using the command `pip install -r requirements.txt`, cd into the `src` folder and run the command `uvicorn main:app --host 0.0.0.0 --port 8000`.

You can also use docker to run the project, using the command `docker build -t voice-calculator-back-end -f docker/dockerfile .` if you want call the docker compose file, use the command `docker-compose -f .\docker\docker-compose.yaml --env-file src/.env up -d`

## Tips

To test the API, you can use the Swagger interface that is available in the route `/docs`.

## Ngrok

To use the Ngrok, you need to install the Ngrok in your machine.
Then you can run the command `ngrok http 8000` to expose the API to the internet.
