import streamlit as st
from transformers import pipeline

# Load the language models
gpt_model = pipeline("text-generation", model="openai-gpt")
gpt2_model = pipeline("text-generation", model="gpt2")

# Define Streamlit app with enhanced aesthetics, additional content, and fancy styling
def main():
    # Set page title and add some styling
    st.set_page_config(
        page_title="Fancy Text Generation App",
        page_icon=":robot:",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Sidebar for input
    st.sidebar.title("Input Options")
    input_text = st.sidebar.text_area("Enter some text", height=100)
    generate_button = st.sidebar.button("Generate Text")

    # Header
    st.markdown("""
    <div style="background-color: #2a9d8f; padding: 20px; border-radius: 10px;">
        <h1 style="color: white; text-align: center;">🤖 Fancy Text Generation App</h1>
    </div>
    <br />
    """, unsafe_allow_html=True)

    # Introduction section
    st.markdown("""
    <div style="background-color: #2a9d8f; padding: 20px; border-radius: 10px;">
        <p>Welcome to the Fancy Text Generation app powered by Streamlit and Hugging Face Transformers! This app uses GPT and GPT-2 models for text generation.</p>
        <p>Enter some text in the sidebar, click on the <span style="font-weight: bold;">Generate Text</span> button, and see the models generate text for you.</p>
    </div>
    """, unsafe_allow_html=True)

    # Generate and display text when the button is clicked
    if generate_button and input_text:
        with st.spinner("Generating text..."):
            # Generate text with both models
            gpt_generated_text = gpt_model(input_text, max_length=50, do_sample=True)[0]['generated_text']
            gpt2_generated_text = gpt2_model(input_text, max_length=50, do_sample=True)[0]['generated_text']

        # Display generated text with styling
        st.markdown("## Generated Text:")
        st.markdown(f"### GPT Generated Text:")
        st.write(gpt_generated_text)
        st.markdown(f"### GPT-2 Generated Text:")
        st.write(gpt2_generated_text)
    elif generate_button:
        st.warning("Please enter some text first.")

if __name__ == "__main__":
    main()
