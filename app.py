import streamlit as st
from transformers import pipeline

# Title of the web app
st.title('Enhanced Hugging Face LLM App with Streamlit')

# Sidebar for model selection
model_type = st.sidebar.selectbox(
    'Select Model Type',
    ('Text Generation - GPT-2', 'Sentiment Analysis - DistilBERT', 'Named Entity Recognition - BERT')
)

# Function to load the model based on selection
def load_model(model_type):
    if model_type == 'Text Generation - GPT-2':
        return pipeline('text-generation', model='gpt2'), 'Enter text to generate from:'
    elif model_type == 'Sentiment Analysis - DistilBERT':
        return pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english'), 'Enter text to analyze sentiment:'
    elif model_type == 'Named Entity Recognition - BERT':
        return pipeline('ner', model='dbmdz/bert-large-cased-finetuned-conll03-english'), 'Enter text to analyze for named entities:'
    else:
        raise ValueError("Unsupported model type")

# Load the selected model
model, input_label = load_model(model_type)

# Text input from the user
user_input = st.text_area(input_label, height=150)

# Function to display model output based on model type
def display_model_output(model_type, model_output):
    if model_type.startswith('Text Generation'):
        return model_output[0]['generated_text']
    elif model_type.startswith('Sentiment Analysis'):
        return str(model_output)
    elif model_type.startswith('Named Entity Recognition'):
        return ', '.join([f"Text: {ent['word']}, Entity: {ent['entity']}" for ent in model_output])
    else:
        return "Unsupported model type"

if st.button('Run Model'):
    with st.spinner('Processing...'):
        model_output = model(user_input)
        output_text = display_model_output(model_type, model_output)
        st.text_area("Model Output:", value=output_text, height=150, disabled=True)
