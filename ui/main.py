# ui/main.py
import streamlit as st
import pandas as pd
import requests

st.title("📊 AI Data Visualizer")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    st.success("✅ File uploaded")
    chart_type = st.selectbox("Select Chart Type", ["bar", "pie", "histogram", "line"])
    
    df = pd.read_csv(uploaded_file)
    column = st.selectbox("Select Column for Chart", df.columns)

    # Reset file pointer to the beginning before sending to backend
    uploaded_file.seek(0)

    if st.button("Generate Chart"):
        with st.spinner("Cleaning data and generating chart..."):
            response = requests.post(
                "http://127.0.0.1:5000/process",
                files={"file": uploaded_file},
                data={"chart_type": chart_type, "column": column}
            )
            if response.status_code == 200:
                result = response.json()
                st.components.v1.html(result.get("chart_html"), height=600, scrolling=True)
                st.json(result.get("log"))
            else:
                st.error("❌ Failed to process the file.")
