# Gideon AI

## Personal Voice Assistant

Gideon AI is a Python-based personal voice assistant designed to interact with users through **voice commands and a graphical interface**. The project combines speech recognition, text-to-speech, web services, Wikipedia search, WolframAlpha, and SQLite database functionality into a single assistant application.

## Features

* Voice-based interaction
* Speech recognition for processing user commands
* Text-to-speech responses
* Graphical user interface using CustomTkinter
* Wikipedia search
* Web search and information retrieval
* WolframAlpha integration for computational queries
* SQLite database integration
* Personalized assistant responses
* Time and date-related commands
* Command-based interaction through the assistant interface

## Technologies Used

* **Python**
* **CustomTkinter** — Graphical user interface
* **SpeechRecognition** — Speech-to-text processing
* **pyttsx3** — Text-to-speech
* **Wikipedia** — Wikipedia information retrieval
* **WolframAlpha API** — Computational queries
* **SQLite** — Local database functionality
* **Web Browser** — Web search and navigation



## How Gideon AI Works

The assistant follows a basic voice-interaction workflow:

```text
User
  ↓
Voice Command
  ↓
Speech Recognition
  ↓
Command Processing
  ↓
Selected Service / Function
  ↓
Response Generation
  ↓
Text-to-Speech
  ↓
Voice Response
```

Depending on the command, Gideon can process the request locally or use external services such as Wikipedia and WolframAlpha.

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Gideon-AI
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API credentials

If the application uses external APIs, store API credentials in environment variables rather than directly inside the Python source code.

Create a `.env` file:

```text
WOLFRAM_APP_ID=your_api_key_here
```

Do not upload `.env` to GitHub.

### 4. Run the application

```bash
python src/main.py
```

## Example Commands

Gideon can be used for commands such as:

```text
"What is the time?"
"Search Wikipedia for Python."
"Search the web for ..."
"Calculate ..."
```

The exact commands depend on the functions implemented in the selected version of the assistant.

## Database

The project uses SQLite for local data storage. The database can be used by the assistant for storing and retrieving application-related information.

If the database contains personal or sensitive information, it should not be uploaded to a public repository.

## Security

API keys and other credentials should never be hard-coded into the source code or committed to a public GitHub repository.

Use environment variables for sensitive information and add the following to `.gitignore`:

```text
.env
__pycache__/
*.pyc
```

## Future Improvements

Possible improvements for Gideon AI include:

* Improved natural-language command understanding
* More reliable speech recognition
* Additional voice commands
* Better conversational capabilities
* Modular command handling
* More external API integrations
* Improved graphical interface
* User authentication and personalization
* Better error handling
* Configuration through environment variables

## Disclaimer

Gideon AI is an educational and personal software project. The accuracy and availability of responses may depend on external services and APIs used by the application.

## Author

Developed as a Python and Artificial Intelligence project.
