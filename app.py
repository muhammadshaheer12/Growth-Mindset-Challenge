import streamlit as st

# Title and Introduction
st.title("🌱 Growth Mindset Challenge")
st.write("### Develop a mindset that embraces learning and growth!")

# Sidebar Navigation
menu = st.sidebar.radio("Navigation", ["🏆 Daily Goals", "📖 Notes", "❓ Q&A", "💡 Motivation", "📊 Progress Tracker", "🎯 Challenges", "🧠 Mindset Journal", "🛠 Productivity Tools"])

# Goal Tracking Section
if menu == "🏆 Daily Goals":
    st.subheader("Set and Track Your Goals")
    goal = st.text_input("What is your main goal for today?")
    if "goals" not in st.session_state:
        st.session_state.goals = []
    
    if st.button("Save Goal", use_container_width=True):
        if goal:
            st.session_state.goals.append({"goal": goal, "completed": False})
            st.success("Goal saved!")
    
    st.write("### Your Tracked Goals")
    for i, item in enumerate(st.session_state.goals):
        col1, col2 = st.columns([0.8, 0.2])
        col1.write(f"✅ {item['goal']}")
        if col2.checkbox("Done", key=f"goal_{i}"):
            item["completed"] = True

# Notes Section
elif menu == "📖 Notes":
    st.subheader("Personal Notes")
    note = st.text_area("Write down your thoughts, reflections, or learnings:")
    if "notes" not in st.session_state:
        st.session_state.notes = []
    
    if st.button("Save Note", use_container_width=True):
        if note:
            st.session_state.notes.append(note)
            st.success("Note saved!")
    
    st.write("### Your Saved Notes")
    for n in st.session_state.notes:
        st.write(f"📝 {n}")

# Q&A Section
elif menu == "❓ Q&A":
    st.subheader("Test Your Growth Mindset")
    questions = {
        "What is a growth mindset?": "The belief that intelligence and abilities can develop with effort and learning.",
        "Why should you embrace challenges?": "Challenges help you grow and improve your skills.",
        "How can mistakes help you learn?": "Mistakes provide opportunities to understand and improve.",
    }
    
    for q, a in questions.items():
        user_answer = st.text_input(q)
        if user_answer:
            st.write(f"✅ Correct Answer: {a}")

# Motivational Quotes Section
elif menu == "💡 Motivation":
    st.subheader("Stay Inspired!")
    quotes = [
        "'Success is not final, failure is not fatal: it is the courage to continue that counts.' – Winston Churchill",
        "'Do not judge me by my success, judge me by how many times I fell down and got back up again.' – Nelson Mandela",
        "'It’s not that I’m so smart, it’s just that I stay with problems longer.' – Albert Einstein",
        "'Hardships often prepare ordinary people for an extraordinary destiny.' – C.S. Lewis",
        "'Believe you can and you're halfway there.' – Theodore Roosevelt"
    ]
    st.write(f"🌟 {quotes[0]}")

# Progress Tracker Section
elif menu == "📊 Progress Tracker":
    st.subheader("Track Your Progress")
    if "goals" in st.session_state and st.session_state.goals:
        completed_goals = sum(1 for g in st.session_state.goals if g["completed"])
        total_goals = len(st.session_state.goals)
        st.metric("Completed Goals", completed_goals, f"Out of {total_goals}")
    else:
        st.write("No goals set yet! Start tracking now.")

# Challenge Section
elif menu == "🎯 Challenges":
    st.subheader("Take a Challenge")
    challenges = [
        "Write down three things you're grateful for today.",
        "Learn a new skill for 10 minutes.",
        "Give someone a compliment or encouragement.",
        "Reflect on a mistake and what you learned from it.",
        "Read about a successful person’s struggles and how they overcame them.",
        "Push yourself outside your comfort zone today."
    ]
    st.write(f"🎯 Your Challenge: {challenges[0]}")

# Mindset Journal
elif menu == "🧠 Mindset Journal":
    st.subheader("Daily Reflections")
    journal_entry = st.text_area("What did you learn today? What challenges did you face? How did you overcome them?")
    if "journal" not in st.session_state:
        st.session_state.journal = []
    
    if st.button("Save Journal Entry", use_container_width=True):
        if journal_entry:
            st.session_state.journal.append({"entry": journal_entry})
            st.success("Entry saved!")
    
    st.write("### Your Journal Entries")
    for entry in st.session_state.journal:
        st.write(f"📔 {entry['entry']}")

# Productivity Tools
elif menu == "🛠 Productivity Tools":
    st.subheader("Enhance Your Productivity")
    st.write("Use these tools to stay focused and improve efficiency:")
    timer_minutes = st.slider("Set a focus timer (minutes):", 1, 60, 25)
    if st.button("Start Timer", use_container_width=True):
        st.write(f"⏳ Timer set for {timer_minutes} minutes. Stay focused!")
    st.write("Try the **Pomodoro Technique**: Work for 25 minutes, then take a 5-minute break.")
