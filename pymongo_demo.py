from pymongo import MongoClient
import requests
import json

client = MongoClient("mongodb://localhost:27017/")
db = client["assignnew"]

url_users = "https://jsonplaceholder.typicode.com/users"
url_posts = "https://jsonplaceholder.typicode.com/posts"
url_comments = "https://jsonplaceholder.typicode.com/comments"

collection_users = db["users"]
u1 = requests.get(url_users)
users_dict = json.loads(u1.text)
collection_users.insert_many(users_dict)

collection_posts = db["posts"]
u2 = requests.get(url_posts)
posts_dict = json.loads(u2.text)
collection_posts.insert_many(posts_dict)

collection_comments = db["comments"]
u3 = requests.get(url_comments)
comments_dict = json.loads(u3.text)
collection_comments.insert_many(comments_dict)
