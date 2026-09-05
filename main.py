import json
from scraper import fetch_and_clean
from parser import extract_and_validate
import os
from eval import evaluate_extraction

def run_pipeline():
    url = "https://news.ycombinator.com"

    cleaned_text = fetch_and_clean(url)
    final_data = extract_and_validate(cleaned_text)

    os.makedirs("output",exist_ok = True)
    with open ("output/hacker_news.json","w")as f:
        json.dump (final_data,f,indent=2)

    passed = evaluate_extraction(final_data, cleaned_text)
    if not passed:
        print("⚠️ Extraction failed quality checks — review output/hacker_news.json manually.")

if __name__ == "__main__":
    run_pipeline()
