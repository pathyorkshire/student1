import streamlit as st
import time
seconds = st.number_input("Enter countdown time in seconds:", min_value=0)
if st.button("Start Countdown"):
  for i in range(seconds, 0, -1):
  st.write(i)
  time.sleep(1)
  st.write("Time's up!")
