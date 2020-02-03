from pymongo import MongoClient
from pymongo_demo import collection_users, collection_posts, collection_comments

query1 = collection_posts.aggregate([{'$group': {'_id':"$userId","maxpost":{'$sum': 1}}},{'$sort':{ "maxpost":-1}},{'$limit':1}])
query2 = collection_comments.aggregate([{'$group': {'_id':"$postId","maxcomments":{'$sum': 1}}},{'$sort':{ "maxcomments":-1}},{'$limit':1}])
query3 = collection_posts.aggregate([{'$group': {'_id':"$userId","postcount":{'$sum': 1}}}])
query4 = collection_comments.aggregate([{'$group': {'_id':"$userId","commentcount":{'$sum': 1}}}])
query5 = collection_posts.aggregate([{'$group': {'_id':"$userId", "maxlentitle":{ '$max':  {'$strLenCP': "$title"}}}},{'$sort':{ "maxlentitle":-1}},{'$limit':1}])

def query_print(query):
    for x in query:
        print(x)

query_print(query1)
query_print(query2)
query_print(query3)
query_print(query4)
query_print(query5)