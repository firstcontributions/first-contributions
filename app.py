import streamlit as st

st.set_page_config(
    page_title="AI Student Life Assistant",
    page_icon="🎓"
)

st.title("🎓 AI Student Life Assistant")
st.write("Your personal college study planner!")

st.subheader("📚 Today's Study Plan")

subject = st.text_input("Enter your subject")
task = st.text_input("Enter your study task")
hours = st.number_input(
    "Study time (hours)",
    min_value=0.5,
    max_value=12.0,
    value=1.0
)

if st.button("Add Study Task"):
    if subject.strip() and task.strip():
        st.success(
            f"Added: {subject} - {task} ({hours} hours)"
        )
    else:
        st.warning("Please enter your subject and task.")

st.subheader("✅ Daily Tasks")

task1 = st.checkbox("Attend classes")
task2 = st.checkbox("Complete assignments")
task3 = st.checkbox("Revise today's lessons")

completed = sum([task1, task2, task3])
st.progress(completed / 3)
st.write(f"Completed {completed} out of 3 tasks.")