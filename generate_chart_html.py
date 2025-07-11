import plotly.express as px
import pandas as pd

def generate_chart_html(df: pd.DataFrame, chart_config: dict) -> str:
    chart_type = chart_config.get("chart_type") or chart_config.get("type")
    column = chart_config.get("column") or chart_config.get("field")
    title = chart_config.get("title", "Chart")

    if column not in df.columns:
        return f"<p>Error: Column '{column}' does not exist in the dataset.</p>"

    try:
        if chart_type == "pie":
            fig = px.pie(df, names=column, title=title)
        elif chart_type == "bar":
            fig = px.bar(df, x=column, title=title)
        elif chart_type == "histogram":
            fig = px.histogram(df, x=column, title=title)
        elif chart_type == "line":
            # Only use line chart if the column is numeric or has a proper index
            if not pd.api.types.is_numeric_dtype(df[column]):
                df[column] = pd.factorize(df[column])[0]  # convert non-numeric to numeric
            fig = px.line(df, y=column, title=title)
        else:
            return f"<p>Unsupported chart type: {chart_type}</p>"

        return fig.to_html(full_html=False)
    except Exception as e:
        return f"<p>Error generating chart for column '{column}': {str(e)}</p>"
