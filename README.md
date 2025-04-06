# 🚀 AI-Driven Career Path Guidance

Welcome to **AI-Driven Career Path Guidance**, a powerful tool designed to help you discover personalized career opportunities based on your skills, experience, and aspirations. Leveraging cutting-edge AI technology, this app provides tailored career advice and market insights to guide your professional journey.

## Features

✅ **Personalized Career Recommendations**: Enter your skills and experience level to receive AI-driven career suggestions.  
✅ **Localized Insights**: Provide your location to get job market and salary information specific to your area.  
✅ **Salary Insights**: Toggle to view estimated salaries and job demand for your desired roles.  
✅ **Beautiful UI**: A sleek and intuitive interface powered by Streamlit.  

---

## How to Use

1. **Install Dependencies**  
   Ensure you have Python installed, then install the required libraries:

   ```bash
   pip install streamlit groq requests

2. **Set Up Environment Variables**  
   For security, store your Groq API key as an environment variable:

   ```bash
   export GROQ_API_KEY="your_api_key_here"
   ```

   Alternatively, replace `"your_api_key_here"` in the code with your actual API key.

3. **Run the App**  
   Start the Streamlit app locally:

   ```bash
   streamlit run app.py
   ```

4. **Interact with the App**  
   - Enter your skills (comma-separated).  
   - Optionally specify your career interest, experience level, and location.  
   - Click "🔍 Get Career Guidance" to receive personalized results.  

---

## Example Input

- **Skills**: `Python, Cybersecurity, Machine Learning`  
- **Career Interest**: `Cybersecurity Analyst`  
- **Experience Level**: `Intermediate`  
- **Location**: `New York, USA`  
- **Show Salary Insights**: ☑️  

---

## Screenshots

![example-1](https://github.com/user-attachments/assets/114f8705-daaa-4a7a-8cf4-aa353bf35d8b)

---

## Contributing

We welcome contributions! If you'd like to improve this project, please follow these steps:

1. Fork the repository.  
2. Create a new branch (`git checkout -b feature/YourFeature`).  
3. Commit your changes (`git commit -m "Add Your Feature"`).  
4. Push to the branch (`git push origin feature/YourFeature`).  
5. Open a pull request.  

---

## Acknowledgments

- Built using [Streamlit](https://streamlit.io/) for the frontend.
- Powered by [Groq](https://groq.com/) for AI-driven insights.
- Inspired by the need for accessible and personalized career guidance.

---
 
Happy career hunting! 🌟
