# Subreddit Post Downloader 🚀

A Python script to archive posts from any public subreddit using Reddit's API via PRAW.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Reddit API](https://img.shields.io/badge/Reddit_API-TOS_compliant-orange)

## Features

- 📥 Download Reddit posts with metadata (title, author, score, etc.)
- 🗂 Save posts in JSON format with timestamps
- ⏱ Automatic rate limit handling
- 📂 Creates organized output directories
- 🔒 Reddit API authentication support
- 🚫 Error handling for removed/deleted posts

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/subreddit-post-downloader.git
   cd subreddit-post-downloader

2. **Install dependencies**

   pip install -r requirements.txt

3. **Configuration**

    Create Reddit App
    Get API credentials from Reddit Apps:

        Go to "Create App"

        Choose "Script" type

        Use http://localhost:8080 as redirect URI

    Set up credentials
    Create .env file:
   
CLIENT_ID=your_client_id_here
CLIENT_SECRET=your_client_secret_here
USER_AGENT=script:subreddit-downloader:v1.0 (by /u/yourusername)

Usage

    Run the script:

bash
Copy

python download_posts.py

    Enter subreddit name when prompted:

text
Copy

Enter subreddit name: python

    Output will be saved to:

text
Copy

./python_posts_<timestamp>/python_posts.json

Sample Output (python_posts.json):
json
Copy

[
  {
    "title": "Python 3.12 Released!",
    "author": "python_dev",
    "score": 15432,
    "created_utc": 1690843200,
    "url": "https://reddit.com/r/python/...",
    "num_comments": 892,
    "permalink": "/r/python/comments/...",
    "flair": "Official Announcement"
  }
]

API Compliance

    Respect Reddit's API Rules

    Default limit: ~60 requests/minute

    Automatic rate limiting

    Add manual delays for large operations

    Do not collect personal/private data
