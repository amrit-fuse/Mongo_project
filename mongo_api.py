from pymongo import MongoClient
from dotenv import load_dotenv
import pprint  # pretty print library is used to make the output look more organized
import datetime
import csv
import json
from flask import Flask, jsonify, request
from bson.objectid import ObjectId
from bson import json_util

app = Flask(__name__)

MONGODB_URI = "mongodb://localhost:27017"
client = MongoClient(MONGODB_URI)


# parse json
def parse_json(data):
    return json.loads(json_util.dumps(data))

# convert csv to json


def csv_to_json(csv_file):
    jsonArr = []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            jsonArr.append(row)
    return jsonArr


# Insert a document into the collection
@app.route('/insert_one', methods=['POST'])
def insert_one():
    # reference  database and collection  # if dont exist, it will be created
    db = client['Hospital']
    collection = db['Patients']

    # read json raw
    data = request.get_json()

    # insert data
    result = collection.insert_one(data)

    inserted_id = parse_json(result.inserted_id)
    return jsonify(inserted_id)


# Insert multiple documents into the collection
@app.route('/insert_many', methods=['POST'])
def insert_many():
    # reference  database and collection  # if dont exist, it will be created
    db = client['Hospital']
    collection = db['Patients']

    json_patient = csv_to_json('patients.csv')

    # insert json data into collection
    result = collection.insert_many(json_patient)

    inserted_ids = parse_json(result.inserted_ids)
    return jsonify(inserted_ids)

# find one document


@app.route('/find_one', methods=['GET'])
def find_one():
    # reference  database and collection  # if dont exist, it will be created
    db = client['Hospital']
    collection = db['Patients']

    document_to_find = request.get_json()
    # find one document
    result = collection.find_one(document_to_find)

    return jsonify(parse_json(result))


# find one document
@app.route('/find_all', methods=['GET'])
def find_all():
    # reference  database and collection  # if dont exist, it will be created
    db = client['Hospital']
    collection = db['Patients']

    documents_to_find = request.get_json()

    # find all document
    result = collection.find(documents_to_find)

    return jsonify(parse_json(result))

# update one document


@app.route('/update_one', methods=['PUT'])
def update_one():
    # reference  database and collection  # if dont exist, it will be created
    db = client['Hospital']
    collection = db['Patients']

    document_to_find = request.get_json()  # unique _id to identify documnent
    update_operation = {"$set": {"patient_name": "Baburo Mastani"}}

    # update one document
    result = collection.update_one(document_to_find, update_operation)

    return jsonify(parse_json(result.raw_result))


# update many document
@app.route('/update_many', methods=['PUT'])
def update_many():
    # reference  database and collection  # if dont exist, it will be created
    db = client['Hospital']
    collection = db['Patients']

    document_to_find = request.get_json()
    update_operation = {"$set": {"patient_city": "Sindupalchowk"}}

    # update many document
    result = collection.update_many(document_to_find, update_operation)
    return jsonify(parse_json(result.raw_result))

# delete one document


@app.route('/delete_one', methods=['DELETE'])
def delete_one():
    # reference  database and collection  # if dont exist, it will be created
    db = client['Hospital']
    collection = db['Patients']

    document_to_find = request.get_json()

    # delete one document
    result = collection.delete_one(document_to_find)
    return jsonify(parse_json(result.raw_result))


# delete many document
@app.route('/delete_many', methods=['DELETE'])
def delete_many():
    # reference  database and collection  # if dont exist, it will be created
    db = client['Hospital']
    collection = db['Patients']

    document_to_find = request.get_json()

    # delete many document
    result = collection.delete_many(document_to_find)
    return jsonify(parse_json(result.raw_result))


if __name__ == '__main__':

    app.run(debug=True)
