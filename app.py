import streamlit as st

st.set_page_config(page_title="কুইজ গেম", page_icon="🎯")
st.title("সাধারণ জ্ঞান কুইজ গেম 🎯")

if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0

questions = [
    {"question": "১. পাইথন (Python) কে তৈরি করেন?", "options": ["Bill Gates", "Guido van Rossum", "Dennis Ritchie", "Mark Zuckerberg"], "answer": "Guido van Rossum"},
    {"question": "২. কম্পিউটারের মস্তিষ্ক কোনটি?", "options": ["RAM", "Hard Disk", "CPU", "Monitor"], "answer": "CPU"},
    {"question": "৩. HTML এর পূর্ণরূপ কী?", "options": ["Hyper Text Markup Language", "High Text Machine Language", "Hyperlink Text Markup Language", "Home Tool Markup Language"], "answer": "Hyper Text Markup Language"}
]

if st.session_state.question_index < len(questions):
    current_q = questions[st.session_state.question_index]
    st.subheader(current_q["question"])
    for option in current_q["options"]:
        if st.button(option, use_container_width=True):
            if option == current_q["answer"]:
                st.success("✅ সঠিক উত্তর!")
                st.session_state.score += 1
            else:
                st.error(f"❌ ভুল! সঠিক উত্তর: {current_q['answer']}")
            st.session_state.question_index += 1
            st.rerun()
else:
    st.balloons()
    st.header(f"গেম শেষ! 🎉")
    st.subheader(f"আপনার চূড়ান্ত স্কোর: {st.session_state.score} / {len(questions)}")
    if st.button("আবার শুরু করুন"):
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.rerun()
      
