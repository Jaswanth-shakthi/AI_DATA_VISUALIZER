from flask import Flask, request, jsonify
import pandas as pd
import plotly.express as px
import io

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process_file():
    print(" Received request at /process")

    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    chart_type = request.form.get("chart_type")
    column = request.form.get("column")
    log = []

    try:
        #  Read file content safely and reset pointer
        file_content = file.read()
        if not file_content.strip():
            raise ValueError("Uploaded file is empty.")

        # Use io.StringIO for decoded content
        decoded = file_content.decode("utf-8")
        print("Decoded file preview:\n", decoded[:200])  # Just print first 200 chars
        df = pd.read_csv(io.StringIO(decoded))

    except Exception as e:
        print(f"CSV Read Error: {e}")
        return jsonify({"error": f"CSV Read Error: {e}"}), 400

    log.append(" File read successfully.")

    if column not in df.columns:
        return jsonify({"error": f"Column '{column}' not found in CSV."}), 400

    # Basic Cleaning
    null_counts = df[column].isnull().sum()
    if null_counts > 0:
        df[column].fillna("Missing", inplace=True)
        log.append(f" Filled {null_counts} missing values in column '{column}'.")

    try:
        fig = None
        print(f"DEBUG: chart_type={chart_type}, column={column}")
        print(f"DEBUG: df.columns={df.columns.tolist()}")
        if chart_type == "pie":
            fig = px.pie(df, names=column, title=f"{column} - Pie Chart")
        elif chart_type == "bar":
            df_bar = df[column].value_counts().reset_index()
            df_bar.columns = [column, 'count']
            print(f"DEBUG: df_bar.columns={df_bar.columns.tolist()}")
            fig = px.bar(df_bar, x=column, y='count', title=f"{column} - Bar Chart")
        elif chart_type == "histogram":
            fig = px.histogram(df, x=column, title=f"{column} - Histogram")
        elif chart_type == "line":
            df_line = df.copy()
            df_line['index_col'] = df_line.index
            print(f"DEBUG: df_line.columns={df_line.columns.tolist()}")
            fig = px.line(df_line, x='index_col', y=column, title=f"{column} - Line Chart")
        else:
            return jsonify({"error": "Invalid chart type"}), 400

        log.append(" Chart generated successfully.")
        chart_html = fig.to_html(include_plotlyjs='cdn')
        return jsonify({"chart_html": chart_html, "log": log})

    except Exception as e:
        print(f"Chart Generation Error: {e}")
        return jsonify({"error": f"Chart generation failed: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
