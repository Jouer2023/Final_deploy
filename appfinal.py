import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = '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'

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

# Function to start the chat application
def start_chat():
    # Prints a welcome message
    st.text("Yana: Hello, what's up?")

    # Initialize the conversation with a system message
    messages = [
        {"role": "system", "content": "You are a friendly and helpful assistant that is ready to talk about mental health."},
    ]

    # Condition to carry on with the message until the user says bye
    while True:
        # Get user input
        user_input = st.text_input("You:")

        # Checks if the user wants to end the conversation
        if user_input.lower() == 'bye':
            st.text("Yana: Goodbye!")
            break

        # Checks if the user wants to clear context
        elif user_input.lower() == 'clear context':
            messages = clear_context()

        # Carries on with the chat if nothing
        else:
            # Appends the user's message to the conversation and asks for a friendly response
            messages.append({"role": "user", "content": user_input})
            messages.append({"role": "system", "content": "Please provide a friendly and empathetic response"})

            # Provides a response for the user and displays it
            bot_response = chat_with_bot(messages)
            st.text("Yana:" + bot_response)

        # Appends the user's message to the conversation
        messages.append({"role": "user", "content": user_input})

        # Gets the assistant's response using the chat_with_bot function
        bot_response = chat_with_bot(messages)

        # Display the assistant's response
        st.text("Yana:" + bot_response)

# Function to clear context and start again
def clear_context():
    return [
        {"role": "system", "content": "You are a friendly and helpful assistant."},
    ]

# Welcome message
st.text("Hi, I am Yana, a text-based AI assistant that will act as your supportive system to the end.")

# Start the conversation by calling the function
start_chat()
