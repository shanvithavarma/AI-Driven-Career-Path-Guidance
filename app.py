import streamlit as st
from groq import Groq
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Hardcoded API Key (Not Recommended for Production)
GROQ_API_KEY = "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"

if not GROQ_API_KEY:
    st.error("Missing Groq API key. Please ensure the GROQ_API_KEY is set.")
    st.stop()

# Initialize Groq client
try:
    client = Groq(api_key=GROQ_API_KEY)
    logging.info("Groq API client initialized successfully.")
except Exception as e:
    logging.error(f"Failed to initialize Groq client: {e}")
    st.error("Error initializing AI model. Please check logs.")
    st.stop()

# Function to get AI-generated career guidance
def get_career_guidance(user_input):
    try:
        messages = [
            {"role": "system", "content": "You are an AI expert providing career guidance based on user skills."},
            {"role": "user", "content": user_input}
        ]
        
        completion = client.chat.completions.create(
            model="qwen-2.5-32b",
            messages=messages,
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            stream=False,
        )
        
        return completion.choices[0].message.content.strip()
    
    except Exception as e:
        if "API key" in str(e):
            logging.error("Invalid or missing Groq API key.")
            return "Error: Invalid or missing API key. Please check your configuration."
        elif "network" in str(e).lower():
            logging.error("Network error while connecting to Groq API.")
            return "Error: Unable to connect to the AI service. Please check your internet connection."
        else:
            logging.error(f"Unexpected error: {e}")
            return "Error: An unexpected issue occurred. Please try again later."

# Placeholder function for salary insights (can integrate real-world APIs here)
def fetch_salary_insights(location, career_interest):
    if location and career_interest:
        return f"Based on market trends in {location}, the average salary for a {career_interest} is $80,000 - $120,000 annually."
    return "Insufficient data to provide salary insights."

# Streamlit UI
st.set_page_config(
    page_title="AI-Driven Career Path Guidance",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .header {
        font-size: 36px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 20px;
    }
    .subheader {
        font-size: 24px;
        font-weight: bold;
        color: #34495e;
        margin-top: 20px;
    }
    .result-box {
        background-color: #f9f9f9;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 15px;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header">🚀 AI-Driven Career Path Guidance</div>', unsafe_allow_html=True)
st.markdown("### Get AI-powered career recommendations based on your skills and industry trends.")

# User Inputs
col1, col2 = st.columns(2)

with col1:
    skills = st.text_area(
        "Enter your skills (comma-separated):",
        "Python, Cybersecurity, Machine Learning",
        help="List your technical and soft skills here, separated by commas."
    )
    career_interest = st.text_input(
        "Enter your career interest (optional):",
        "Cybersecurity Analyst",
        help="Specify your desired role or industry, if any."
    )

with col2:
    experience_level = st.selectbox(
        "Select your experience level:",
        ["Beginner", "Intermediate", "Advanced", "Expert"],
        help="Choose your current experience level."
    )
    location = st.text_input(
        "Enter your location (optional, for job market insights):",
        help="Provide your city or country for localized insights."
    )
    display_salary = st.checkbox("Show salary and job demand insights?")

# Submit Button
if st.button("🔍 Get Career Guidance"):
    if not skills.strip():
        st.error("Please enter at least one skill.")
        st.stop()

    with st.spinner("Analyzing your career options..."):
        user_query = f"Given these skills: {skills}, experience level: {experience_level}, suggest potential career paths. "
        if career_interest:
            user_query += f"The user is interested in {career_interest}. "
        if location:
            user_query += f"Provide insights relevant to {location}. "
        if display_salary:
            user_query += "Include salary ranges and job demand insights. "

        logging.info(f"Processing career guidance request with query: {user_query}")
        guidance = get_career_guidance(user_query)

        # Display Results
        st.markdown('<div class="subheader">📌 Career Guidance</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-box">{guidance}</div>', unsafe_allow_html=True)

        if display_salary:
            st.markdown('<div class="subheader">📊 Salary & Job Demand Insights</div>', unsafe_allow_html=True)
            salary_insights = fetch_salary_insights(location, career_interest)
            st.markdown(f'<div class="result-box">{salary_insights}</div>', unsafe_allow_html=True)