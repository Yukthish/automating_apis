import requests
import json

def fetch_posts(api_url):
    response = requests.get(api_url)
    
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        return None

    data = response.json()
    print(f"Fetched posts: {json.dumps(data, indent=2)}")
    for post in data:
        print(f"Post ID: {post['id']}, Title: {post['title']}")
def main():
    api_url = "https://jsonplaceholder.typicode.com/posts"  #for posts
    fetch_posts(api_url)

if __name__ == "__main__":
    main()
