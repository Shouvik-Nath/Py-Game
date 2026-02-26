import streamlit as st

st.set_page_config(page_title="পাইথন ক্যালকুলেটর", page_icon="🔢")
st.title("🔢 সহজ ক্যালকুলেটর")

# ইনপুট নেওয়ার জন্য দুটি বক্স
num1 = st.number_input("প্রথম সংখ্যা লিখুন", value=0.0)
num2 = st.number_input("দ্বিতীয় সংখ্যা লিখুন", value=0.0)

st.write("### অপারেশন বেছে নিন:")

# বাটনগুলো পাশাপাশি দেখানোর জন্য কলাম
col1, col2, col3, col4 = st.columns(4)

result = 0

with col1:
    if st.button("➕ যোগ"):
        result = num1 + num2
        st.success(f"ফলাফল: {result}")

with col2:
    if st.button("➖ বিয়োগ"):
        result = num1 - num2
        st.success(f"ফলাফল: {result}")

with col3:
    if st.button("✖️ গুণ"):
        result = num1 * num2
        st.success(f"ফলাফল: {result}")

with col4:
    if st.button("➗ ভাগ"):
        if num2 != 0:
            result = num1 / num2
            st.success(f"ফলাফল: {result}")
        else:
            st.error("শুন্য (0) দিয়ে ভাগ করা সম্ভব নয়!")

st.write("---")
st.caption("Class 12 Python Project - তৈরি করেছে শৌভিক")
