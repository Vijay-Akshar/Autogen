# Autogen

An interactive AI-powered Python application that evaluates password strength and suggests improvements or generates secure passwords. Built with [AutoGen](https://github.com/microsoft/autogen) and powered by GPT-4.

---

## Features

-  Evaluate password strength with detailed feedback
-  Generate strong, secure passwords
-  GPT-4 backed conversation agent using `autogen`
-  Optional code execution (with or without Docker)
-  Clean command-line interface

---

## How It Works

- You provide a password via terminal input
- The assistant evaluates the strength and suggests improvements
- If you type `generate`, it creates a secure password for you
- Uses GPT-4 and OpenAI API to power the conversation
- Continues until you type `exit` to exit

---

## Demo

```bash
Enter a password for evaluation (or type 'generate' to get a strong password):
Your password: pickle1sDB3ST#1P
user_proxy (to assistant):

Analyze the password: 'pickle1sDB3ST#1P' and suggest how to make it stronger.

--------------------------------------------------------------------------------
assistant (to user_proxy):

The password 'pickle1sDB3ST#1P' is already quite strong. It includes uppercase letters, lowercase letters, numbers, and special characters, and it is longer than 12 characters. These are all good practices for creating a strong password.

However, if you want to make it even stronger, you could consider the following:

1. Increase the length: The longer the password, the harder it is to crack. You could add more characters to your password.

2. Use more special characters: You've used a number sign (#), but you could also include other special characters like @, $, %, &, *, etc.

3. Avoid common words or phrases: Even though 'pickle' and 'best' are not very common, they are still English words that could potentially be guessed by a sophisticated attack. Using random combinations of letters and numbers can make your password stronger.

4. Avoid sequential numbers: '1' and '3' are not sequential, but it's still a good idea to avoid sequences or repeated numbers.

Here's a Python code that generates a strong password based on these principles:

```python
import string
import random

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

print(generate_password(20))
```.

This code will generate a 20-character password that includes a mix of uppercase and lowercase letters, numbers, and special characters. The characters are chosen randomly, so it's very unlikely that the password will include common words or phrases.

--------------------------------------------------------------------------------
Replying as user_proxy. Provide feedback to assistant. Press enter to skip and use auto-reply, or type 'exit' to end the conversation: generate
user_proxy (to assistant):

generate

--------------------------------------------------------------------------------
assistant (to user_proxy):

Sure, here is the Python code to generate a strong password. This code will generate a 20-character password that includes a mix of uppercase and lowercase letters, numbers, and special characters. The characters are chosen randomly, so it's very unlikely that the password will include common words or phrases.       

```python
# filename: generate_password.py

import string
import random

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

print(generate_password(20))
```.

You can save this code in a file named `generate_password.py` and run it to generate a new password.

--------------------------------------------------------------------------------
Replying as user_proxy. Provide feedback to assistant. Press enter to skip and use auto-reply, or type 'exit' to end the conversation:

>>>>>>>> NO HUMAN INPUT RECEIVED.

>>>>>>>> USING AUTO REPLY...

>>>>>>>> EXECUTING CODE BLOCK 0 (inferred language is python)...
user_proxy (to assistant):

exitcode: 0 (execution succeeded)
Code output:
RVrd>.T:(78HnPs8g_Aw


--------------------------------------------------------------------------------
assistant (to user_proxy):

Great! The code has successfully generated a strong password: 'RVrd>.T:(78HnPs8g_Aw'. This password is 20 characters long and includes a mix of uppercase and lowercase letters, numbers, and special characters. The characters are chosen randomly, so it's very unlikely that the password will include common words or phrases. This makes it a very strong password.

Remember to store your password in a secure place and do not share it with anyone.

TERMINATE

--------------------------------------------------------------------------------
Replying as user_proxy. Provide feedback to assistant. Press enter to skip and use auto-reply, or type 'exit' to end the conversation: exit

>>>>>>>> TERMINATING RUN (8debe3ef-c27a-4382-b2d2-80499c2b93c6): User requested to end the conversation
Do you want to enter another password? (yes/no): no
Session terminated.
```

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/password-strength-agent.git
cd password-strength-agent
```

### 2. Set Up the Environment
Create and activate a Conda environment (or use `venv`):
```bash
conda create -n autogen python=3.10 -y
conda activate autogen
```

### 3. Install Dependencies
```bash
pip install ag2[openai]
```

### 4. Add Your OpenAI API Key
In `app.py`, replace the placeholder in `config_list` with your actual key:
```python
'api_key': 'sk-...'
```

### 5. Run the App
```bash
python app.py
```

---

## Configuration

To disable Docker-based code execution (recommended if Docker isn't installed), ensure:
```python
code_execution_config={"use_docker": False, "work_dir": "web"}
```

Or, set this environment variable:
```bash
export AUTOGEN_USE_DOCKER=False  # for Linux/macOS
$env:AUTOGEN_USE_DOCKER = "False"  # for Windows PowerShell
```

---

## Security Tips

- Never log or share real passwords.
- Use this tool only for educational or personal learning purposes.
- Use a password manager for storing passwords securely.

---

## Built With

- [Python](https://www.python.org/)
- [AutoGen](https://github.com/microsoft/autogen)
- [OpenAI GPT-4](https://platform.openai.com/docs/guides/gpt)

---

## License

MIT License. See `LICENSE` for details.

---

## Credits

Developed by Akshar — Computer Science student.  
Let's build safer systems, one password at a time.
