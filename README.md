<h1> Voice Calculator Back End </h1>

<h2> Project: Final CI/CD Project </h2>

**Main Code Language:** Python

**Team:**
Anderson Karl,
Isaías Fontes,
Pedro Henrique and
Saynarah Nabuco

<h3> Sources folder: </h3>

1. Calculadora.py

Class named 'Calculadora' with four methods, each one for a math operation.

Somar: addition <br>
Subtrair: subtration <br>
Multiplicar: multiplication <br>
Dividir: division


2. Main_example.py

This script essentially sets up a real-time speech transcription application using Gradio and Hugging Face's Transformers library, capable of transcribing Portuguese speech input through a specified model.


<h3> Github Workflow - Actions: </h3>

1. *Set up job*:

Initializes the job environment, including setting up any necessary configurations and dependencies for the subsequent steps.

2. *Checkout repository*:

Retrieves a copy of the repository's codebase to the runner machine, enabling subsequent steps to access and operate on the code.

3. *Set up Python*:

Configures the runtime environment for Python, typically by installing the specified Python version and setting up any environment variables or configurations required for Python-based tasks.

4. *Install dependencies*:

Installs project dependencies using package managers like pip (Python), ensuring all required libraries or modules are available for the application to function correctly.

5. *Run tests*:

Executes automated tests defined in the project, such as unit tests, integration tests, or end-to-end tests. This step ensures that the code changes meet expected behavior and quality standards.

6. *Post Set up Python*:

Performs any cleanup or additional configuration tasks related to the Python environment setup, ensuring the environment is properly configured before proceeding with subsequent steps.

7. Post Checkout repository:

Performs cleanup or additional configuration tasks related to checking out the repository, ensuring any temporary files or configurations are appropriately handled before moving forward.

8. Complete job:

Finalizes the job execution, providing any necessary summary or status updates. This stage marks the completion of the defined workflow for the job, indicating success or failure based on the preceding steps.


