import praw
import json
import os
from datetime import datetime

def download_subreddit_posts(subreddit_name):
    # Reddit API credentials
    reddit = praw.Reddit(
        client_id='YOUR_CLIENT_ID',
        client_secret='YOUR_CLIENT_SECRET',
        user_agent='YOUR_USER_AGENT'
    )

    subreddit = reddit.subreddit(subreddit_name)
    
    # Create output directory
    output_dir = f"{subreddit_name}_posts_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    os.makedirs(output_dir, exist_ok=True)

    posts_data = []
    
    try:
        # Get posts (adjust limit as needed, None tries to get all)
        for post in subreddit.new(limit=None):
            post_data = {
                'title': post.title,
                'author': str(post.author),
                'score': post.score,
                'id': post.id,
                'url': post.url,
                'created_utc': post.created_utc,
                'selftext': post.selftext,
                'num_comments': post.num_comments,
                'permalink': post.permalink,
                'flair': post.link_flair_text
            }
            posts_data.append(post_data)
            
            # Print progress
            print(f"Processed: {post.title}")

        # Save to JSON
        filename = os.path.join(output_dir, f"{subreddit_name}_posts.json")
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(posts_data, f, ensure_ascii=False, indent=2)
            
        print(f"\nSaved {len(posts_data)} posts to {filename}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    try:
        import praw
    except ImportError:
        print("Error: praw not installed. Install with: pip install praw")
        exit(1)

    subreddit_name = input("Enter subreddit name: ").strip()
    download_subreddit_posts(subreddit_name)
