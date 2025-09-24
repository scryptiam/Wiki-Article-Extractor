import wikipediaapi

def get_wiki_article():
    article_title = input("Enter the Wikipedia article title: ")

    headers = {
        'User-Agent': 'MyWikiStoryApp/1.0 (contact@example.com)'
    }
    
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        user_agent='MyWikiStoryApp/1.0 (contact@example.com)',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )

    print("\nFetching article, please wait...")

    page = wiki_wiki.page(article_title)

    if not page.exists():
        print(f"\n--- Sorry, the article '{article_title}' was not found. Please check the spelling and capitalization. ---")
    else:
        print("\n--- COPY THE TEXT BELOW ---\n")
        print(page.text)

if __name__ == "__main__":
    get_wiki_article()
