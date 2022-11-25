from pymongo import MongoClient
from dotenv import load_dotenv
import pprint  # pretty print library is used to make the output look more organized
import datetime
from secrets import *

from bson.objectid import ObjectId


MONGODB_URI = connection_string
client = MongoClient(MONGODB_URI)


# # # List all databases in the cluster.
# for db_name in client.list_database_names():
#     print(db_name)


# # Get reference to 'bank' database
# db = client.bank  # if dont exist, it will be created

# # Get reference to 'accounts' collection
# accounts_collection = db.accounts  # if dont exist, it will be created

# new_account = {
#     "account_holder": "Linus Torvalds",
#     "account_id": "MDB829001337",
#     "account_type": "checking",
#     "balance": 50352434,
#     "last_updated": datetime.datetime.utcnow(),
# }

# # Write an expression that inserts the 'new_account' document into the 'accounts' collection.
# result = accounts_collection.insert_one(new_account)

# document_id = result.inserted_id
# print(f"_id of inserted document: {document_id}")

# # Get reference to 'bank' database
# db = client.bank

# # Get a reference to 'accounts' collection
# accounts_collection = db.accounts

# new_accounts = [
#     {
#         "account_id": "MDB011235813",
#         "account_holder": "Ada Lovelace",
#         "account_type": "checking",
#         "balance": 60218,
#     },
#     {
#         "account_id": "MDB829000001",
#         "account_holder": "Muhammad ibn Musa al-Khwarizmi",
#         "account_type": "savings",
#         "balance": 267914296,
#     },
# ]

# # Write an expression that inserts the documents in 'new_accounts' into the 'accounts' collection.
# result = accounts_collection.insert_many(new_accounts)

# document_ids = result.inserted_ids
# print("# of documents inserted: " + str(len(document_ids)))
# print(f"_ids of inserted documents: {document_ids}")

# # Get reference to 'bank' database
# db = client.bank

# # Get a reference to the 'accounts' collection
# accounts_collection = db.accounts

# # Query by ObjectId
# document_to_find = {"_id": ObjectId("6380516f1279ecfabb3decc9")}

# # Write an expression that retrieves the document matching the query constraint in the 'accounts' collection.
# result = accounts_collection.find_one(document_to_find)
# pprint.pprint(result)

# Get reference to 'bank' database
# db = client.bank

# # Get a reference to the 'accounts' collection
# accounts_collection = db.accounts

# # Query
# documents_to_find = {"balance": {"$gt": 4700}}

# # Write an expression that selects the documents matching the query constraint in the 'accounts' collection.
# cursor = accounts_collection.find(documents_to_find)

# num_docs = 0
# for document in cursor:
#     num_docs += 1
#     pprint.pprint(document)
#     print()
# print("# of documents found: " + str(num_docs))


# # Get reference to 'bank' database
# db = client.bank

# # Get reference to 'accounts' collection
# accounts_collection = db.accounts

# # Filter
# document_to_update = {"_id": ObjectId("6380516f1279ecfabb3decc9")}

# # Update
# add_to_balance = {"$inc": {"balance": 100}}

# # Print original document
# pprint.pprint(accounts_collection.find_one(document_to_update))

# # Write an expression that adds to the target account balance by the specified amount.
# result = accounts_collection.update_one(document_to_update, add_to_balance)
# print("Documents updated: " + str(result.modified_count))

# # Print updated document
# pprint.pprint(accounts_collection.find_one(document_to_update))


# # Get reference to 'bank' database
# db = client.bank

# # Get reference to 'accounts' collection
# accounts_collection = db.accounts

# # Filter
# select_accounts = {"account_type": "savings"}

# # Update
# set_field = {"$set": {"minimum_balance": 100}}

# # Write an expression that adds a 'minimum_balance' field to each savings acccount and sets its value to 100.
# result = accounts_collection.update_many(select_accounts, set_field)

# print("Documents matched: " + str(result.matched_count))
# print("Documents updated: " + str(result.modified_count))
# pprint.pprint(accounts_collection.find_one(select_accounts))

# Get reference to 'bank' database
db = client.bank

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

# Filter by ObjectId
document_to_delete = {"_id": ObjectId("6380516f1279ecfabb3decc9")}

# Search for document before delete
print("Searching for target document before delete: ")
pprint.pprint(accounts_collection.find_one(document_to_delete))

# Write an expression that deletes the target account.
result = accounts_collection.delete_one(document_to_delete)

# Search for document after delete
print("Searching for target document after delete: ")
pprint.pprint(accounts_collection.find_one(document_to_delete))

print("Documents deleted: " + str(result.deleted_count))



client.close()
