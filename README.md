# Autogen

A terminal-based Python tool that evaluates the strength of passwords and helps users create more secure ones. Built using Microsoft’s AutoGen framework and powered by GPT-4, this assistant gives practical feedback on password security and can generate strong alternatives for safer usage.

You can input your own passwords for analysis, or simply type `generate` to get a highly secure, randomly created password.

### Features
- Password Analysis: Evaluates strength based on length, character diversity, and patterns.
- Secure Suggestions: Offers tips to enhance password security.
- Password Generation: Instantly creates strong, random passwords.
- GPT-4 Powered: Uses natural language understanding for meaningful feedback.
- AutoGen Agent Integration: Structured AI interaction via AutoGen’s assistant and user proxy agents.

---

## How It Works

### 1. `app.py`
This file drives the interaction between the user and the assistant.
- Accepts input from the user for password evaluation.
- Calls the assistant to respond with security advice.
- Can execute Python code blocks returned by the assistant (like password generation).
- Continues the loop until the user types `exit` to exit.

---

## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/password-strength-agent.git
cd password-strength-agent
```

### 2. Create and Activate Environment
Using Conda:
```sh
conda create -n autogen python=3.10 -y
conda activate autogen
```

### 3. Install Dependencies
```sh
pip install ag2[openai]
```

### 4. Configure OpenAI API Key
In `app.py`, update the `api_key` value:
```python
config_list = {
    'model': 'gpt-4',
    'api_key': 'sk-your-key-here'
}
```

### 5. Run the App
```sh
python app.py
```

---

## Usage
- When prompted, enter a password to analyze.
- Type `generate` to get a strong password.
- After each interaction, you'll be asked whether you want to continue.

Example:
```bash
Enter a password for evaluation (or type 'generate' to get a strong password):
Your password: P1ckL31sC001!
user_proxy (to assistant):

Analyze the password: 'P1ckL31sC001!' and suggest how to make it stronger.

--------------------------------------------------------------------------------
assistant (to user_proxy):

The password 'P1ckL31sC001!' is already quite strong. It includes uppercase and lowercase letters, numbers, and special characters, which are all good practices for creating a strong password. It also has a length of 13 characters, which is above the commonly recommended minimum of 8 characters.

However, there are a few ways to make it even stronger:

1. Increase the length: The longer the password, the harder it is to crack. You could add more characters to this password to make it stronger.

2. Avoid common substitutions: Replacing 'e' with '3' and 'o' with '0' are common substitutions. These can be guessed by advanced cracking tools. Try to avoid these common substitutions.

3. Avoid dictionary words: Even though 'P1ckL31sC001!' doesn't look like it contains any dictionary words, it's actually a leetspeak for 'PickleIsCool!'. Advanced cracking tools can guess passwords that contain dictionary words, even if they're disguised with character substitutions. Try to avoid using dictionary words in your password.

4. Add more special characters or use less common ones: The password only contains one type of special character '!'. Adding more types or using less common ones can make the password stronger.

Here's an example of a stronger password based on 'P1ckL31sC001!': 'P1ckL31sC001!@#%&*'

Please note that the best way to create a strong and secure password is to use a random combination of characters, or a password manager that can generate and store complex passwords for you.

--------------------------------------------------------------------------------
Replying as user_proxy. Provide feedback to assistant. Press enter to skip and use auto-reply, or type 'exit' to end the conversation: Add some new characters and shuffle it around
user_proxy (to assistant):

Add some new characters and shuffle it around

--------------------------------------------------------------------------------
assistant (to user_proxy):

Sure, we can add some new characters and shuffle the existing ones around. Here's a Python script that does just that. It adds a few more special characters and numbers to the password, then shuffles the characters around to create a new password.

```python
# filename: password_shuffle.py

import random

# Original password
password = 'P1ckL31sC001!'

# Add some new characters
password += '@#%&*'

# Convert the password to a list of characters, shuffle it, then convert it back to a string
password = list(password)
random.shuffle(password)
password = ''.join(password)

print(password)
```.

You can run this script to generate a new, stronger password. The new password will be different every time you run the script, thanks to the random shuffle.  

--------------------------------------------------------------------------------
Replying as user_proxy. Provide feedback to assistant. Press enter to skip and use auto-reply, or type 'exit' to end the conversation:

>>>>>>>> NO HUMAN INPUT RECEIVED.

>>>>>>>> USING AUTO REPLY...

>>>>>>>> EXECUTING CODE BLOCK 0 (inferred language is python)...
user_proxy (to assistant):

exitcode: 0 (execution succeeded)
Code output:
11*00Cc&1@!s#kL3P%


--------------------------------------------------------------------------------
assistant (to user_proxy):

Great! The new password '11*00Cc&1@!s#kL3P%' is stronger than the original one. It has a length of 18 characters, includes more special characters, and the characters have been shuffled around. This makes it harder for an attacker to guess the password.

Remember to store your password in a secure place, and consider using a password manager to manage your passwords.

TERMINATE

--------------------------------------------------------------------------------
Replying as user_proxy. Provide feedback to assistant. Press enter to skip and use auto-reply, or type 'exit' to end the conversation: exit

>>>>>>>> TERMINATING RUN (994d4b85-bdf5-4097-af1a-b82902f7ebf6): User requested to end the conversation
Do you want to enter another password? (yes/no): no
Session terminated.
```

---

## Getting Started
### Prerequisites
Ensure the following are installed:
- Python 3.10+
- OpenAI-compatible API key
- Optional: Docker (disabled by default in the config)

---

## Contributing
Feel free to fork the project, submit issues, or open pull requests to improve functionality and extend features.

---

## License
This project is open-source and licensed under the MIT License.

(For educational and personal use only)

