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
- Any necessary NLP libraries (e.g., indic-transliteration, Aksharamukha)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/p2kalita/Eng2Asm.git
   cd Eng2Asm
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   - **For CLI usage:**
     ```sh
     python transliterator.py "অগ্নি"  # Example Assamese text
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
python transliterator.py "অগ্নি"
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