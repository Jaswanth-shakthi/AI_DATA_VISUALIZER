import plotly.express as px
import os

def generate_chart_from_instruction(df, gemini_text):
    charts = []
    lines = gemini_text.strip().split('\n')

    for i in range(len(lines)):
        if "Chart type" in lines[i]:
            chart_type = lines[i].split(":")[1].strip().lower()
            x_col = lines[i + 1].split(":")[1].strip()
            y_col = lines[i + 2].split(":")[1].strip()
            title = lines[i + 3].split(":")[1].strip()

            if chart_type == "bar":
                fig = px.bar(df, x=x_col, y=y_col, title=title)
            elif chart_type == "line":
                fig = px.line(df, x=x_col, y=y_col, title=title)
            elif chart_type == "scatter":
                fig = px.scatter(df, x=x_col, y=y_col, title=title)
            elif chart_type == "pie":
                fig = px.pie(df, names=x_col, values=y_col, title=title)
            else:
                continue  # Unsupported

            path = f"uploads/chart_{len(charts)}.html"
            fig.write_html(path)
            charts.append({"type": chart_type, "path": path, "title": title})

    return charts
