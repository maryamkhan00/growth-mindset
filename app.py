# streamlit
import streamlit as st

st.set_page_config(page_title="Growth Mindset", page_icon="🧠", layout="wide", initial_sidebar_state="expanded")
st.title("Growth Mindset")
st.header("🚀 Welcome to your growth journey!")
st.write("This app is designed to help you develop a growth mindset. A growth mindset is the belief that you can develop your abilities through hard work, dedication, and perseverance. It is the belief that you can learn and grow from your experiences, challenges, and failures. With a growth mindset, you are more likely to take on challenges, learn from your mistakes, and achieve your goals. This app will provide you with resources, tools, and strategies to help you develop a growth mindset and reach your full potential. Let's get started!")

#quote section
st.header("🌟 Today's Inspiration Dose")
st.write("'Believe you can and you're halfway there.' -Theodore Roosevelt")

#getting challanges from user
st.header("🧩 What's your challange today?")
challange = st.text_input("What challange are you facing today?: ")
if challange:
    st.success(f"Your challange is: {challange}. Keep going! You've got this! 💪")
else:
    st.warning("psst ... don't forget to enter your challange! 😉")  

#reflection on learning
st.header("📚 Reflect on your learning")
reflection = st.text_area("What did you learn today?: ")
if reflection:
    st.success(f"Great! You've learned: {reflection}. Keep up the good work! Learning will make you grow as a person. 🌟")
else:
    st.info("Take a moment to reflect on what you've learned today. It's important to acknowledge your progress and growth! 🌱")

#achievements
st.header("🏆 Celebrate your achievements")
achievement = st.text_input("What did you achieve today?: ")
if achievement:
    st.success(f"Congratulations! You've achieved: {achievement}. Keep up the amazing work! 🎉")
else:
    st.info("Don't forget to celebrate your achievements, no matter how big or small! 🎈 You deserve it! Remember setbacks are just a part of the journey.🌟 besides they provide you lessons and wisdom along the way.")

#footer
st.markdown("---")
st.write("🚀 Keep going! You're on the right track to developing a growth mindset! Remember, growth is a journey, not a destination. Embrace the challenges, learn from your experiences, and celebrate your achievements along the way. You've got this! 💪🌟")
st.write("📚 created by **[Maryam khan]**")