# AI Data Visualizer

## Overview
AI Data Visualizer is a web application that allows users to upload CSV files and generate various types of charts (bar, pie, histogram, line) based on selected columns. The backend is built with Flask, and the frontend uses Streamlit for an interactive UI.

## Features
- Upload CSV files via a user-friendly interface.
- Select chart type: bar, pie, histogram, or line.
- Choose the column to visualize.
- Handles missing values by filling them with "Missing".
- Generates interactive charts using Plotly.
- Provides logs of processing steps and errors.

## Installation

1. Clone the repository.

2. Create a virtual environment (recommended):

```bash
python -m venv myenv
```

3. Activate the virtual environment:

- On Windows:

```bash
myenv\Scripts\activate
```

- On macOS/Linux:

```bash
source myenv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask backend server:

```bash
python app.py
```

2. In a separate terminal, start the Streamlit frontend:

```bash
streamlit run ui/main.py
```

3. Open the Streamlit app in your browser at the URL shown (usually http://localhost:8502).

4. Upload a CSV file, select the chart type and column, then generate the chart.

## API Endpoint

- **POST /process**

  - Accepts a CSV file upload with form data:
    - `file`: CSV file
    - `chart_type`: one of `bar`, `pie`, `histogram`, `line`
    - `column`: column name to visualize

  - Returns JSON with:
    - `chart_html`: HTML string of the generated Plotly chart
    - `log`: list of processing log messages

## Error Handling

- Returns appropriate error messages for:
  - Missing file upload
  - Empty uploaded file
  - Column not found in CSV
  - Invalid chart type
  - Chart generation failures

## Project Structure

- `app.py`: Flask backend server handling file processing and chart generation.
- `ui/main.py`: Streamlit frontend for file upload and user interaction.
- `requirements.txt`: Python dependencies.
- `utils/`: Utility modules (cleaning, visualization helpers).
- `uploads/`: Directory for uploaded files (if used).

## Dependencies

- Flask
- Pandas
- Plotly
- Streamlit
- Requests

## Notes

- Ensure the uploaded files are valid CSVs.
- The app currently supports only CSV file uploads.
- For line charts, the index of the dataframe is used as the x-axis.

## License

MIT License

## Author

Your Name
#   A I _ D A T A _ V I S U A L I Z E R  
 #   A I _ D A T A _ V I S U A L I Z E R  
 #   A I _ D A T A _ V I S U A L I Z E R  
 #   A I _ D A T A _ V I S U A L I Z E R  
 