from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/api/subs")
def get_subscriber_count():
    try:
        url = "https://www.youtube.com/@MintyDaCat"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers)

        soup = BeautifulSoup(r.text, "html.parser")
        count = "unknown"

        for meta in soup.find_all("meta"):
            if meta.get("itemprop") == "interactionCount":
                count = meta.get("content")

        return jsonify({"subscriberCount": count})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
