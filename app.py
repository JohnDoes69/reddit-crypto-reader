import praw
import json
from datetime import datetime

REDDIT = praw.Reddit(
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET",
    user_agent = "CryptoReader by u/Fit_Bid9619"
)

SUBS = [
    "CryptoCurrency",
    "Bitcoin",
    "EtherMining",
    "CryptoMarkets",
]

def fetch_posts():
    output = {}

    for sub in SUBS:
        subreddit = REDDIT.subreddit(sub)
        posts = []

        for submission in subreddit.hot(limit=10):
            submission.comments.replace_more(limit=0)

            post_data = {
                "id": submission.id,
                "title": submission.title,
                "score": submission.score,
                "url": submission.url,
                "created_utc": submission.created_utc,
                "top_comments": [
                    c.body for c in submission.comments[:5]
                ]
            }

            posts.append(post_data)

        output[sub] = posts

    return output


if __name__ == "__main__":
    data = fetch_posts()

    filename = f"crypto_data_{datetime.utcnow().strftime('%Y%m%d_%H%M')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Saved data to {filename}")
