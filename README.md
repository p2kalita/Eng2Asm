# Assamese to English Transliterator

## Overview
The **Assamese to English Transliterator** is a web-based or CLI-based application that allows users to convert Assamese script into its phonetic English representation. This tool is useful for language learners, researchers, and individuals who want to transliterate Assamese words or sentences into the Roman alphabet.

## Features
- Supports real-time transliteration of Assamese text into English.
- Preserves phonetic accuracy to maintain readability.
- Simple and user-friendly interface.
- Can be integrated into larger NLP applications.
- Works with Unicode Assamese script.

## Installation
### Prerequisites
Ensure you have the following dependencies installed:
- Python 3.x
- Flask (for web app) or argparse (for CLI usage)
- Google Gemini API key

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/Eng2Asm.git
   cd Eng2Asm
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up your Gemini API key:
   ```sh
   export GEMINI_API_KEY="your_api_key_here"
   ```
4. Run the application:
   - **For CLI usage:**
     ```sh
     python app.py "অগ্নি"  # Example Assamese text
     ```
   - **For Web App:**
     ```sh
     python app.py
     ```
     Then, open `http://127.0.0.1:5000` in your browser.

## Usage
### CLI Usage
Run the script with an Assamese input string:
```sh
python app.py "অগ্নি"
```
Output:
```
"agni"
```

### Web Application Usage
1. Open the web interface.
2. Enter Assamese text in the input box.
3. Click the "Transliterate" button.
4. View the transliterated output in English.

## API Endpoints
- **POST `/transliterate`**  
  Request:
  ```json
  {
    "text": "অগ্নি"
  }
  ```
  Response:
  ```json
  {
    "transliteration": "agni"
  }
  ```

## Using Gemini API
The transliteration process is powered by the **Google Gemini API**. The application sends a request to the Gemini API, which processes the Assamese text and returns its phonetic English representation.

### Example API Call
```python
import requests
import os

def transliterate(text):
    api_key = os.getenv("GEMINI_API_KEY")
    url = "https://api.gemini.com/v1/transliterate"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    data = {"text": text}
    response = requests.post(url, json=data, headers=headers)
    return response.json()["transliteration"]

print(transliterate("অগ্নি"))
```

## Contributing
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-xyz`
3. Commit your changes: `git commit -m "Add feature xyz"`
4. Push to the branch: `git push origin feature-xyz`
5. Open a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgments
Special thanks to open-source transliteration libraries and contributors who made this project possible.

