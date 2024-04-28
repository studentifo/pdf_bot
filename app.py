import streamlit as st
import pdfplumber
import openai

# Set up OpenAI API
openai.api_key = "sk-proj-0p5yomeNioeP1JVSw7ZeT3BlbkFJC5lGXwrFcNFiAhl61N3N"  # Replace with your OpenAI API key

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    with pdfplumber.open(uploaded_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Function to generate response from OpenAI API
def generate_response(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Update the engine name
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()


# Main function to run Streamlit app
def main():
    st.markdown(
        """
        <style>
            .chat-textarea {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 10px;
                height: 200px;
                overflow-y: scroll;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("PDF Chatbot")

    # File uploader
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        st.write("PDF uploaded successfully!")

        # Extract text from PDF
        pdf_text = extract_text_from_pdf(uploaded_file)

        # Initialize conversation with PDF text
        conversation_history = pdf_text

        # User input
        user_input = st.text_area("You:")

        if user_input:
            # Append user input to conversation history
            conversation_history += "\nUser: " + user_input

            # Generate response from OpenAI API
            bot_response = generate_response(conversation_history)

            # Display bot response with custom styling
            st.write(
                bot_response,
                style="border: 1px solid #ccc; border-radius: 5px; padding: 10px; height: 200px; overflow-y: scroll;"
            )

# Run the app
if __name__ == "__main__":
    main()
