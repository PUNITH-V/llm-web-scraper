
def evaluate_extraction(data: dict, cleaned_text: str):
    print("\n--- EXTRACTION EVALUATION REPORT ---")
    
    articles = data.get("articles", [])
    
    # 1. Completeness
    count_score = "PASS" if len(articles) == 5 else f"FAIL (Expected 5, got {len(articles)})"
    print(f"1. Completeness (Exactly 5 items): {count_score}")
    
    # 2. Sanity Checks
    sanity_passed = True
    for i, article in enumerate(articles):
        if not article.get("title") or len(article["title"]) < 5:
            print(f"Sanity Fail: Article {i} has an invalid title.")
            sanity_passed = False
        if not isinstance(article.get("points"), int) or article["points"] < 0:
            print(f"Sanity Fail: Article {i} has invalid points.")
            sanity_passed = False
            
    print(f"2. Data Sanity (Valid types & lengths): {'PASS' if sanity_passed else 'FAIL'}")
    
    # 3. Deduplication
    titles = [a["title"] for a in articles]
    duplicates = len(titles) != len(set(titles))
    print(f"3. Deduplication (No duplicate titles): {' FAIL' if duplicates else 'PASS'}")
    
    print("----------------------------------------\n")
    
    all_passed = count_score == "PASS" and sanity_passed and not duplicates
    return all_passed