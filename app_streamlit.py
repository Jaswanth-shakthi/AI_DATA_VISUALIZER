import streamlit as st
import requests
import pandas as pd
import io

# App Config
st.set_page_config(page_title=" AI Data Visualizer", layout="centered")
st.title("AI Data Visualizer")

# Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Chart options
chart_types = ["bar", "pie", "histogram", "line"]
chart_type = st.selectbox("Select Chart Type", chart_types)

# Initialize column
column = None

# When a file is uploaded
if uploaded_file is not None:
    try:
        # Safely get file content
        file_bytes = uploaded_file.getvalue()

        # Load preview DataFrame
        df = pd.read_csv(io.BytesIO(file_bytes))
        st.success(" File uploaded and parsed successfully!")

        # Column selector
        column = st.selectbox("Select Column for Chart", df.columns)

        # Show data preview
        with st.expander("Preview Data"):
            st.dataframe(df.head())

    except Exception as e:
        st.error(f" Failed to read the file: {e}")

    # Generate chart
    if st.button("Generate Chart"):
        if chart_type and column:
            try:
                with st.spinner(" Generating chart..."):
                    response = requests.post(
                        "http://localhost:5000/process",
                        files={"file": ("uploaded.csv", io.BytesIO(file_bytes), "text/csv")},
                        data={"chart_type": chart_type, "column": column}
                    )

                    result = response.json()

                    if response.status_code == 200:
                        # Display chart
                        st.components.v1.html(result["chart_html"], height=500, scrolling=True)

                        # Show cleaning log
                        with st.expander(" Cleaning Log"):
                            for entry in result["log"]:
                                st.markdown(f"- {entry}")
                    else:
                        st.error(f" Server error: {result.get('error', 'Unknown error')}")

            except requests.exceptions.RequestException as e:
                st.error(f"🔌 Could not connect to backend: {e}")
        else:
            st.warning("Please select both chart type and column.")
