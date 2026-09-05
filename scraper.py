import requests
from bs4 import BeautifulSoup


def scrape(url:str) -> str:
    headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers, timeout =10)
    response.raise_for_status() 
    soup = BeautifulSoup(response.text, 'html.parser')
    for script_or_style in soup(['script', 'style', 'noscript']):
        script_or_style.decompose() 
    return soup


def clean(soup:BeautifulSoup) -> str:
    # Get text and clean it
    text = soup.get_text(separator=' ')
    # Collapse whitespace
    cleaned_text = ' '.join(text.split())

    return cleaned_text

def fetch_and_clean(url: str) -> str:
    soup = scrape(url)
    return clean(soup)