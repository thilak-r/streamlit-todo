import streamlit as st
from datetime import datetime

# Set page configuration for a modern look
st.set_page_config(page_title="Modern To-Do App", page_icon="✅", layout="wide")

# Custom CSS for a modern aesthetic with adjusted task background
st.markdown("""
    <style>
    .main-title {
        font-size: 2.5em;
        font-weight: bold;
        color: #1E90FF;
        text-align: center;
        margin-bottom: 20px;
    }
    .todo-item {
        font-size: 1.2em;
        padding: 10px;
        background-color: #2c2f33; /* Darker background for better readability */
        color: #ffffff; /* White text for contrast */
        border-radius: 8px;
        margin-bottom: 10px;
    }
    .stButton>button {
        background-color: #1E90FF;
        color: white;
        border-radius: 5px;
        padding: 8px 16px;
    }
    .stTextInput>input {
        border-radius: 5px;
        padding: 8px;
        background-color: #40444b; /* Darker input background */
        color: #ffffff; /* White text in input */
    }
    .stForm {
        background-color: #2c2f33;
        padding: 10px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">Modern To-Do List</div>', unsafe_allow_html=True)

# Automatically fetch and display the current date
current_date = datetime.now().strftime("%Y-%m-%d")
st.write(f"Current Date: {current_date}")

# Initialize session state for to-do list
if 'todos' not in st.session_state:
    st.session_state.todos = []

# Input section
with st.form(key='todo_form', clear_on_submit=True):
    new_todo = st.text_input("Add a new task", placeholder="Enter task here...")
    submit_button = st.form_submit_button(label="Add Task")

# Add new task to list
if submit_button and new_todo:
    st.session_state.todos.append({"task": new_todo, "completed": False, "date_added": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    st.success(f"Added: {new_todo}")

# Display to-do list
st.subheader("Your Tasks")
if st.session_state.todos:
    for i, todo in enumerate(st.session_state.todos):
        col1, col2, col3 = st.columns([0.1, 0.7, 0.2])
        with col1:
            # Checkbox to mark as completed
            completed = st.checkbox("", value=todo["completed"], key=f"check_{i}")
            st.session_state.todos[i]["completed"] = completed
        with col2:
            # Display task with strikethrough if completed
            task_style = "~~" if todo["completed"] else ""
            st.markdown(f'<div class="todo-item">{task_style}{todo["task"]}{task_style} <small>({todo["date_added"]})</small></div>', unsafe_allow_html=True)
        with col3:
            # Delete button
            if st.button("Delete", key=f"delete_{i}"):
                st.session_state.todos.pop(i)
                st.rerun()  # Refresh the app after deletion
else:
    st.write("No tasks yet. Add one above!")

# Optional: Clear all tasks
if st.session_state.todos and st.button("Clear All Tasks"):
    st.session_state.todos = []
    st.rerun()