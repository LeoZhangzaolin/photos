import streamlit as st
from transformers import pipeline

# Load the language model
model = pipeline("text-generation", model="openai-gpt")

def main():
    # Set page title and add some styling
    st.set_page_config(
        page_title="AI Text Generator",
        page_icon=":zap:",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Add header with image
    header_html = """
    <div style="background-color: #4e73df; padding: 20px; border-radius: 10px;">
        <h1 style="color: white; text-align: center;">⚡ AI Text Generator with Hugging Face</h1>
    </div>
    <br />
    """
    st.markdown(header_html, unsafe_allow_html=True)
    
    # Add introduction section
    st.markdown("""
    <div style="background-color: #4e73df; padding: 20px; border-radius: 10px;">
        <p style="color: white;">Discover the power of AI text generation with our Streamlit app, leveraging the Hugging Face Transformers library. Enter a prompt and let the AI amaze you with its creative responses.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Add text input area with placeholder
    text_input = st.text_area("Type here to start generating text...", height=200)
    
    # Add generate button with custom styling
    st.markdown("<style> .stButton button {background-color: #4e73df; color: white;}</style>", unsafe_allow_html=True)
    if st.button("Generate Text", key="generate_button", help="Click to generate text"):
        if text_input:
            # Generate text with the language model
            generated_text = model(text_input, max_length=50, do_sample=True)[0]['generated_text']
            
            # Display generated text with styling
            st.markdown("## Generated Text:")
            st.markdown(f"<div style='background-color: #4e73df; padding: 20px; border-radius: 10px; color: white;'>{generated_text}</div>", unsafe_allow_html=True)
        else:
            # Display warning if no text input
            st.warning("Please enter some text to start generating.")

if __name__ == "__main__":
    main()

