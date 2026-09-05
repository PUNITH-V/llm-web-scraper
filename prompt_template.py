system_prompt = """
You are a data extraction assistant.

Extract information accurately from the provided text.
Do not make up or guess any information.

Return the extracted information as JSON only.

For each article, provide:
- title: the headline of the article
- points: the number of upvotes as an integer
- time_ago: when the article was posted, e.g. "2 hours ago"

The JSON must have this exact structure:

{
    "status": "ok",
    "articles": [
        {
            "title": "article headline",
            "points": 123,
            "time_ago": "2 hours ago"
        }
    ]
}
"""

user_prompt = """
Extract the top 5 news articles from the following News text.

For each article, extract its title, points, and time posted.

Source text:
{cleaned_text}
"""


repair_prompt = """
Your previous response failed validation.

Validation errors:
{error_message}

Previous response:
{previous_response}

Please correct the response so that it matches the required schema.

Rules:
- Return ONLY valid JSON.
- Do not add explanations or markdown.
- Do not invent or guess information.
- Keep the information from the previous response unless it needs to be corrected.
"""
