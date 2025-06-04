import streamlit as st

st.title("Group Prediction App")
st.write("📌 Group 0 = Time Period (11–25), Group 1 = Time Period (26–52)")

value = st.slider("Enter Value", 0.0, 100.0, 50.0)
subgroup = st.text_input("Enter Subgroup (e.g. Female, 18 - 29 years)", "18 - 29 years")
time_period = st.number_input("Enter Time Period", min_value=1, max_value=100, value=20)

if st.button("Predict Group"):
    if time_period < 11 or time_period > 52:
        st.warning("⚠️ Prediction not available for this Time Period. Only 11 to 52 are allowed.")
    else:
        if 11 <= time_period <= 25:
            st.success("✅ Predicted Group: Group 0 (11–25)")
        elif 26 <= time_period <= 52:
            st.success("✅ Predicted Group: Group 1 (26–52)")
