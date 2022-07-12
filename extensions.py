from pymongo import MongoClient
# Setup MongoDB here
mongo = MongoClient("mongodb+srv://shaikfurkhan1998:&Haik#123@cluster0.024ix.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# Cluster which is being accessed
db = mongo['git_response']
data = db['record_res']

