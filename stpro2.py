import streamlit as st
import random as rd
import mysql.connector

# Database connection details
conn_obj = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Probal@555",
    database="exam_qans1"
)

cur_obj = conn_obj.cursor()

# Define function data_retrieve
def data_retrieve(question_id):

    query = f"select * from exam_questions WHERE question_id={question_id}"

    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()

    except mysql.connector.Error as e:
        st.write("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    if result:
        question_id, multiple_questions, answers = result

        st.write(result[1])

        return result[-1]

    else:
        st.write("No question found with the provided id.")


# ---------------- STREAMLIT CODE ---------------- #

st.title("Online Exam System")

# Input number of questions
x = st.number_input(
    "choose less than 100 questions you want to give exam.......",
    min_value=1,
    max_value=99,
    step=1
)

# Session state variables
if "score" not in st.session_state:
    st.session_state.score = 0

if "i" not in st.session_state:
    st.session_state.i = 1

if "correct_answer" not in st.session_state:
    st.session_state.correct_answer = ""

if "exam_started" not in st.session_state:
    st.session_state.exam_started = False


# Start Exam Button
if st.button("Start Exam"):

    st.session_state.score = 0
    st.session_state.i = 1
    st.session_state.exam_started = True


# Exam Logic
if st.session_state.exam_started:

    if st.session_state.i <= x:

        y = rd.randint(1, 100)

        p = data_retrieve(y)

        st.session_state.correct_answer = p

        z = st.text_input("enter your choice").upper()

        if st.button("Submit Answer"):

            if z == p:
                st.session_state.score += 1

            st.write(f"correct answer is -> {p}")

            st.session_state.i = st.session_state.i + 1

            st.rerun()

    else:

        st.success(
            f"your total score is {st.session_state.score}/{x}"
        )

        conn_obj.close()
