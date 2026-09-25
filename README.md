# Project Perfume: fragrance chatbot

A small 2024 Python prototype of a fragrance-expert chatbot. You ask a question ("a fragrance for a summer evening date?"), it sends the question to a GPT-4 endpoint on RapidAPI with a fragrance-expert system prompt, prints the answer, and can email it to you over Gmail SMTP.

This was an early experiment toward a site called Ask Fragrance AI. The command-line version works; the Flask web version was started and never finished.

## Entry points

| Path | State |
|---|---|
| `flaskProject/Project 2/sven.py` | Complete command-line chatbot: two sample questions, then an interactive loop with an optional email step. Credentials are set inside the file. |
| `Mainlead.py` | Same chatbot, reading email credentials from `EMAIL_ADDRESS1` / `EMAIL_PASSWORD1`. The RapidAPI key line is blank, so it does not parse until you add a key. |
| `flaskProject/Mainlead.py` | Start of a Flask web app. Function bodies are placeholders, so it does not run. |
| `flaskProject/templates/index.html` | Form UI for the web app (question, optional email, jQuery AJAX to a `/get_response` route that does not exist yet). |
| `flaskProject/ref.py` | Env-var based `send_email` helper. |
| `flaskProject/Project 2/build/`, `Mainlead.spec` | PyInstaller build output. |

## Run the command-line version

Requires Python 3 and a RapidAPI subscription to the `chatgpt-42` API. Everything else is standard library.

1. In `Mainlead.py`, set the `x-rapidapi-key` header to your key.
2. Set email credentials if you want the email option (for Gmail, use an app password):

   ```bash
   export EMAIL_ADDRESS1=you@gmail.com
   export EMAIL_PASSWORD1=your_app_password
   ```

3. Remove the `import auto_py_to_exe` line (a packaging tool, not needed to run) or `pip install auto-py-to-exe`, then run:

   ```bash
   python Mainlead.py
   ```

Type `exit` to quit.

## Limitations

- Depends on a third-party RapidAPI wrapper (`chatgpt-42.p.rapidapi.com`, `/gpt4`); the response is read from its `result` field.
- The HTTPS connection is created once at import and reused.
- The SMTP host is hard-coded to Gmail.
- The Flask web version is unfinished (see the table above).
