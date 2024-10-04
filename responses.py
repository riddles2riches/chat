# responses.py

import openai

# Replace with your actual OpenAI API key
openai.api_key = 'your_openai_api_key'

def generate_ai_response(user_message):
    """
    This function sends the user's message to ChatGPT and returns the response.
    """
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # You can change to the model you prefer
            prompt=user_message,
            max_tokens=50,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error calling ChatGPT API: {e}")
        return "Sorry, something went wrong with the AI response."

def handle_custom_commands(message_content):
    """
    This function handles any custom commands. Returns a response if a command is detected.
    """
    if message_content.startswith('!hello'):
        return "Hello! How can I help you today?"

    if message_content.startswith('!ai'):
        user_query = message_content[4:]  # Remove the '!ai ' prefix
        return generate_ai_response(user_query)

    # Add more custom commands as needed

    return None  # Return None if no command is detected
