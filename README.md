# TestMeinDeutsch

## Overview
The **German Language Test Generator** is a Streamlit-based web application that generates German language tests for different proficiency levels (A1 - C2). The app utilizes the **Gemini API** to generate unique multiple-choice questions each time a user selects a test. The test evaluates the user's knowledge and provides an interactive score report at the end.

## Features
- 🌍 **Supports All CEFR Levels**: A1, A2, B1, B2, C1, C2

- 🎯 **Multiple-Choice Format**: Each question has four answer options
- ✅ **Real-time Scoring**: Immediate feedback upon submission
- 📊 **Detailed Test Report**: Shows correct/incorrect answers and progress
- 🎉 **Pass/Fail Feedback**: Encouraging messages based on the score
- 🏗️ **Built with Streamlit**: A simple and interactive UI
- 🔗 **Google Gemini AI-Powered**: Uses AI to generate relevant test questions

## Installation
### Prerequisites
Ensure you have Python 3.10+ installed. You also need an API key for Google Gemini AI.

### Steps to Install and Run
1. **Clone the Repository** (or download the script)
   ```bash
   git clone https://github.com/touseefh/TestMeinDeutsch.git
   cd TestMeinDeutsch
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

   ```

3. **Set up Gemini API Key**
   Open the Python script and replace `your-api-key` with your actual Google Gemini API key:
   ```python
   genai.configure(api_key="your-api-key")
   ```

4. **Run the App**
   ```bash
   streamlit run app.py
   ```

## How to Use
1. **Select Your Proficiency Level**: Choose from A1, A2, B1, B2, C1, or C2.
2. **Generate a Test**: Click on "Generate Test" to create a new 10-question quiz.
3. **Answer the Questions**: Select your answers for each question.
4. **Submit the Test**: Click the "Submit Test" button.
5. **View Results**:
   - ✅ See your correct and incorrect answers.
   - 📊 Check your progress bar.
   - 🎉 Receive feedback on your performance.

## Code Structure
- `app.py` → The main Streamlit app script.
- `requirements.txt` → Contains all dependencies for easy setup.

## Troubleshooting
- **Streamlit Not Found?** Install it using `pip install streamlit`.
- **Gemini API Issues?** Ensure your API key is valid and set correctly.
- **App Not Running?** Try `streamlit run app.py` from the correct directory.

## Future Enhancements
- 📝 Add writing and listening exercises.
- 🎤 Include speech recognition for pronunciation tests.
- 📈 Store user scores for tracking progress over time.

## Author
Developed by **HireSync.ai** 🚀
