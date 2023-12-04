import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = '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'

# Define the purpose of your bot - it is small scale
# My bot serves as a mental health support and companionship system.

# Features to have
# Empathetic and understanding
# Active listener
# Resource provision
# Daily positive affirmations
# Safety and privacy
# Issuing a terms and conditions policy
# Constant improvement

# Welcome message
st.title("Yana - Your Supportive System")

# Function to interact with the GPT-3.5 model for testing
def chat_with_bot(messages):
    # Make a request to the OpenAI Chat API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5,
        max_tokens=120
    )
    # Extract and return the assistant's response from the API response
    return response['choices'][0]['message']['content']



# Initialize the conversation with a system message
messages = [
    {"role": "system", "content": "You are a friendly and helpful assistant that is ready to talk about mental health."},
]

# Streamlit app
user_input = st.text_input("You:")
if st.button("Send"):
    # Append the user's message to the conversation
    messages.append({"role": "user", "content": user_input})
    messages.append({"role": "system", "content": "Please provide a friendly and empathetic response"})

    # Get the assistant's response using the chat_with_bot function
    bot_response = chat_with_bot(messages)

    # Append the assistant's response to the conversation
    messages.append({"role": "assistant", "content": bot_response})

    # Display the conversation
    for message in messages:
        role = message["role"]
        content = message["content"]

        if role == "user":
            st.text_input("You:", content, key=role, disabled=True)
        elif role == "assistant":
            st.text_area("Yana:", content, key=role, disabled=True)
        elif role == "system":
            st.text(content)

# Function to interact with the GPT-3.5 model for testing
def chat_with_bot(messages):
    # Make a request to the OpenAI Chat API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5,
        max_tokens=120
    )
    # Extract and return the assistant's response from the API response
    return response['choices'][0]['message']['content']
