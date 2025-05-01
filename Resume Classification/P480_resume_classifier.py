import os
import shutil
import pickle
import chardet
import streamlit as st
from docx import Document
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load the saved model and vectorizer
with open("resume_classifier_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("tfidf_vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Define a new temp directory
temp_dir = r"C:\\Temp\\resume_files"  # Changed directory
os.makedirs(temp_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Function to detect encoding
def detect_encoding(data):
    result = chardet.detect(data)
    return result['encoding'] or 'utf-8'  # Fallback to 'utf-8' if encoding is None

# Function to extract text from .doc files
def extract_text_from_doc(file_path):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            encoding = detect_encoding(content)
            return content.decode(encoding, errors='ignore')
    except Exception as e:
        return f"Error reading DOC file {file_path}: {e}"

# Function to extract text from .docx files
def extract_text_from_docx(file_path):
    try:
        doc = Document(file_path)
        return '\n'.join([para.text for para in doc.paragraphs])
    except Exception as e:
        return f"Error reading DOCX file {file_path}: {e}"

# Function to extract text from .pdf files
def extract_text_from_pdf(file_path):
    try:
        text = []
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                extracted_text = page.extract_text()
                if extracted_text:
                    text.append(extracted_text)
        return '\n'.join(text)
    except Exception as e:
        return f"Error reading PDF file {file_path}: {e}"

# Function to clean extracted text
def clean_text(text):
    # Remove any unwanted non-printable characters or junk data
    cleaned_text = ''.join(char if char.isprintable() else ' ' for char in text)
    return cleaned_text.strip()

# Function to preprocess resume text (to lowercase)
def preprocess_resume(resume_text):
    return resume_text.lower()

# Function to classify resume text
def classify_resume(resume_text):
    processed_text = preprocess_resume(resume_text)
    vectorized_text = vectorizer.transform([processed_text])  # Transform text to numerical format
    prediction = model.predict(vectorized_text)
    return prediction[0]

# Streamlit app
st.title("Resume Classification App")
st.write("Upload a resume to classify it into predefined categories.")

# File uploader
uploaded_file = st.file_uploader("Upload a Resume (PDF, DOCX, or DOC)", type=["pdf", "docx", "doc"])

if uploaded_file is not None:
    file_name = uploaded_file.name
    file_path = os.path.join(temp_dir, file_name)
    
    # Save uploaded file to temp directory
    with open(file_path, "wb") as temp_file:
        temp_file.write(uploaded_file.read())
    
    # Extract text from uploaded file
    if file_path.endswith(".docx"):
        resume_text = extract_text_from_docx(file_path)
    elif file_path.endswith(".doc"):
        resume_text = extract_text_from_doc(file_path)
    elif file_path.endswith(".pdf"):
        resume_text = extract_text_from_pdf(file_path)
    else:
        resume_text = None

    # Clean the extracted text
    if resume_text:
        resume_text = clean_text(resume_text)
        
        # Classify resume
        if st.button("Classify Resume"):
            category = classify_resume(resume_text)
            st.success(f"The resume has been classified as: **{category}**")
    else:
        st.error("Could not extract text from the uploaded file.")
