import google.generativeai as genai

genai.configure(api_key="AIzaSyAuS23ddjTtCupx4VZLIMvojFjM-7osm88")

def get_visualization_suggestions(df):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
    Act as a data visualization expert.

    Given the dataset below (first 5 rows):

    {df.head(5).to_markdown()}

    Suggest 2 charts to visualize this data.
    For each chart, provide:
    - Chart type (e.g., bar, line, pie, scatter)
    - X and Y columns
    - A short title
    - A 1-2 line insight or caption

    Respond in a readable and parsable format.
    """
    response = model.generate_content(prompt)
    return response.text
