from pydantic import BaseModel, Field
from typing import Literal

class NewsArticle(BaseModel):
    title:str = Field(description="The Headline of article")
    points :int = Field(description = "The number of upvotes as an integer")
    time_ago:str = Field(description = "When it was posted, e.g., '2 hours ago'")

class HackerNewsResponse(BaseModel):
    status: Literal["ok"]
    articles: list[NewsArticle] = Field(
        min_length=5,
        max_length= 5,
        description="Give the top 5 articles"
    )


