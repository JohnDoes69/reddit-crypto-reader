# Reddit Crypto Reader

A minimal Python application that reads public posts and top-level comments
from crypto-related subreddits using Reddit's official API via PRAW.

This app is for research and analytics purposes only.  
It does not post, vote, message, or interact with users in any way.

## Features
- Fetches latest posts from selected subreddits
- Reads top-level comments from those posts
- Stores data locally for analysis (JSON)

## Subreddits accessed
- r/CryptoCurrency
- r/Bitcoin
- r/EtherMining
- r/CryptoMarkets

## Installation
pip install -r requirements.txt

## Usage
Set your Reddit API credentials as environment variables:
export CLIENT_ID="your_client_id"
export CLIENT_SECRET="your_client_secret"
export USER_AGENT="CryptoReader by u/Fit_Bid9619"

Then run:
python app.py

## Notes
- This app only reads public data.
- No private data or user interactions are performed.
- This project complies fully with Reddit API Terms of Service.
