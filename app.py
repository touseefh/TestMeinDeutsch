import streamlit as st
import google.generativeai as genai
import random

# Configure Gemini API
genai.configure(api_key="your-api-key")

def generate_test(level):
    """Generate a new test with unique questions each time."""
    prompt = f"""
    Generate a 10-question German language test for {level} level.
    Each question should be multiple-choice with 4 options, and the correct answer must always be one of the options.
    Format:
    Q: Question text
    Answer: Correct Answer
    Options: ["Option1", "Option2", "Option3", "Correct Answer"] (shuffle them)
    """
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return parse_questions(response.text)

def parse_questions(response_text):
    """Extract questions, answers, and options while ensuring correct answer is included."""
    questions = []
    parts = response_text.split("Q:")
    
    for part in parts[1:]:
        lines = part.strip().split("\n")
        question = lines[0].strip()
        answer = lines[1].split(": ")[1].strip()

        options = eval(lines[2].split(": ")[1].strip())
        if answer not in options:
            options[random.randint(0, 3)] = answer  # Ensure correct answer is included
        random.shuffle(options)  # Shuffle options for randomness

        questions.append({"question": question, "options": options, "answer": answer})
    return questions

# Streamlit UI
st.set_page_config(page_title="German Language Test", layout="wide")
st.title("🇩🇪 German Language Test Generator")
st.write("Welcome! Select your level and take a test to assess your German skills.")

# Initialize session state
if "questions" not in st.session_state:
    st.session_state.questions = []
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}
if "correct_answers" not in st.session_state:
    st.session_state.correct_answers = {}
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "current_level" not in st.session_state:
    st.session_state.current_level = None  # Track current level for test regeneration

# User selects level
level = st.selectbox("Select proficiency level:", ["A1", "A2", "B1", "B2", "C1", "C2"])

if st.button("Generate Test"):
    if st.session_state.current_level != level:  # Generate a new test only if level changes
        st.session_state.current_level = level
        st.session_state.questions = generate_test(level)
        st.session_state.user_answers = {}  # Reset answers
        st.session_state.correct_answers = {i: q["answer"] for i, q in enumerate(st.session_state.questions)}
        st.session_state.submitted = False  # Reset submission flag

if st.session_state.questions:
    with st.form("test_form"):
        st.write("### 📝 Answer the questions below:")
        for i, q in enumerate(st.session_state.questions):
            st.write(f"**Q{i+1}: {q['question']}**")
            st.session_state.user_answers[i] = st.radio(
                f"Select an answer for Q{i+1}", 
                q['options'], 
                key=f"q{i}",
            )

        submit_button = st.form_submit_button("Submit Test")

    if submit_button:
        st.session_state.submitted = True

# Display Results
if st.session_state.submitted:
    score = sum(1 for i in st.session_state.user_answers if st.session_state.user_answers[i] == st.session_state.correct_answers[i])
    total_questions = len(st.session_state.questions)
    incorrect = total_questions - score

    st.subheader("📊 Test Results")
    st.write(f"### ✅ Correct Answers: **{score}** / ❌ Incorrect Answers: **{incorrect}**")
    st.progress(score / 10)

    st.write("### 🔍 Detailed Results")
    for i in range(total_questions):
        if st.session_state.user_answers[i] == st.session_state.correct_answers[i]:
            st.success(f"Q{i+1}: ✅ Correct | Your Answer: {st.session_state.user_answers[i]}")
        else:
            st.error(f"Q{i+1}: ❌ Incorrect | Your Answer: {st.session_state.user_answers[i]} | Correct Answer: {st.session_state.correct_answers[i]}")

    # Styled message for pass/fail
    if score >= 8:
        st.markdown("""
        <div style='background-color:#28a745; padding: 15px; border-radius: 10px; text-align:center; color:white;'>
        <h3>🎉 Excellent! You mastered this level!</h3>
        </div>""", unsafe_allow_html=True)
        st.balloons()
    elif score >= 5:
        st.markdown("""
        <div style='background-color:#FFC107; padding: 15px; border-radius: 10px; text-align:center; color:black;'>
        <h3>👍 Good attempt! Keep practicing.</h3>
        </div>""", unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style='background-color:#DC3545; padding: 15px; border-radius: 10px; text-align:center; color:white;'>
        <h3>📖 Keep practicing! Study more for better results.</h3>
        </div>""", unsafe_allow_html=True)
