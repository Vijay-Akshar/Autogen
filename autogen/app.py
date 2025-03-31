import autogen
import random
import string

# OpenAI API configuration
config_list = {
    'model': 'gpt-4',
    'api_key': 'Insert your API key here'
}

llm_config = {
    "seed": 42,  # For caching
    "config_list": config_list,
    "temperature": 0
}

# Function to generate a strong password
def generate_strong_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Initialize Assistant Agent
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config
)

# Initialize User Proxy Agent
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="ALWAYS",  # Allows continuous interaction
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"use_docker": False, "work_dir": "web"},
    llm_config=llm_config,
    system_message="""You are a security expert specializing in password security. 
    When given a password, analyze its strength and suggest improvements.
    If the password is weak, provide a stronger alternative.
    If the user asks, generate a strong password for them."""
)

# Start the interactive conversation
print("Enter a password for evaluation (or type 'generate' to get a strong password):")
while True:
    user_input = input("Your password: ")

    if user_input.lower() == "generate":
        strong_password = generate_strong_password()
        print(f"Suggested strong password: {strong_password}")
    else:
        task = f"Analyze the password: '{user_input}' and suggest how to make it stronger."
        user_proxy.initiate_chat(assistant, message=task)
    
    continue_chat = input("Do you want to enter another password? (yes/no): ")
    if continue_chat.lower() != "yes":
        break

print("Session terminated.")