import requests
from bs4 import BeautifulSoup

def handler(request):
    try:
        url = "https://www.youtube.com/@MintyDaCat"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers)

        soup = BeautifulSoup(r.text, "html.parser")
        count = "unknown"

        for meta in soup.find_all("meta"):
            if meta.get("itemprop") == "interactionCount":
                count = meta.get("content")

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": f'{{"subscriberCount": "{count}"}}'
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": f'{{"error": "{str(e)}"}}'
        }
