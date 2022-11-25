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

    try:
        # read json raw
        data = request.get_json()
    except Exception as e:
        return jsonify({"message": "Error parsing json  confirm that Body  is not empty and each parameters  have double quotes"}, {"additional info": e.args})

    try:
        # insert data
        result = collection.insert_one(data)
        return jsonify({"message": "inserted successfully", "inserted id": str(result.inserted_id)})
    except Exception as e:
        return jsonify({"message": "error", "Info": e.args})


# Insert multiple documents into the collection
@app.route('/insert_many', methods=['POST'])
def insert_many():
    # reference  database and collection  # if dont exist, it will be created
    db = client['Hospital']
    collection = db['Patients']

    json_patient = csv_to_json('patients.csv')

    try:
        # insert json data into collection
        result = collection.insert_many(json_patient)

        # count number of documents inserted
        count = len(result.inserted_ids)

        # inserted_ids = parse_json(result.inserted_ids)
        return jsonify({"message": "inserted successfully", "Count": count, "inserted ids": parse_json(result.inserted_ids)})

    except Exception as e:
        return jsonify({"message": "error", "Info": e.args})


# find one document
@app.route('/find_one', methods=['GET'])
def find_one():
    # reference  database and collection  # if dont exist, it will be created
    db = client['Hospital']
    collection = db['Patients']

    try:
        document_to_find = request.get_json()
    except Exception as e:
        return jsonify({"message": "Error parsing json  confirm that Body is not empty and each parameters  have double quotes"}, {"additional info": e.args})
    try:
        result = collection.find_one(document_to_find)
        # if document is not found, return message
        if result is None:
            return jsonify({"message": "Document not found for " + str(document_to_find)})
        return jsonify({"message": "Found successfully", "result": parse_json(result)})
    except Exception as e:
        return jsonify({"message": "error", "Info": e.args})


# find one document
@app.route('/find_all', methods=['GET'])
def find_all():
    # reference  database and collection  # if dont exist, it will be created
    db = client['Hospital']
    collection = db['Patients']

    try:
        documents_to_find = request.get_json()
    except Exception as e:
        return jsonify({"message": "Error parsing json  confirm that Body is not empty and each parameters  have double quotes"}, {"additional info": e.args})
    try:
        # find all document
        result = collection.find(documents_to_find)
        # if document is not found, return message
        if result is None:
            return jsonify({"message": "Document not found for " + str(documents_to_find)})

        return jsonify({"message": "Found successfully", "result": parse_json(result)})

    except Exception as e:
        return jsonify({"message": "error", "Info": e.args})


# update one document

@app.route('/update_one', methods=['PUT'])
def update_one():
    # reference  database and collection  # if dont exist, it will be created
    db = client['Hospital']
    collection = db['Patients']

    try:
        document_to_find = request.get_json()
    except Exception as e:
        return jsonify({"message": "Error parsing json  confirm that Body is not empty and each parameters  have double quotes"}, {"additional info": e.args})

    try:
        update_operation = {"$set": {"patient_name": "Baburo Mastani"}}

        # update one document
        result = collection.update_one(document_to_find, update_operation)

        # if document is not found, return message
        if result.modified_count == 0:
            return jsonify({"message": "Document not found for " + str(document_to_find)})

        return jsonify({"message": "Updated successfully", "result": parse_json(result.raw_result)})
    except Exception as e:
        return jsonify({"message": "error", "Info": e.args})


# update many document
@app.route('/update_many', methods=['PUT'])
def update_many():
    # reference  database and collection  # if dont exist, it will be created
    db = client['Hospital']
    collection = db['Patients']

    try:
        document_to_find = request.get_json()
    except Exception as e:
        return jsonify({"message": "Error parsing json  confirm that Body is not empty and each parameters  have double quotes"}, {"additional info": e.args})

    try:
        update_operation = {"$set": {"patient_city": "Sindupalchowk"}}

        # update many document
        result = collection.update_many(document_to_find, update_operation)

        # if document is not found, return message
        if result.modified_count == 0:
            return jsonify({"message": "Document not found for " + str(document_to_find)})

        return jsonify({"message": "Updated successfully", "result": parse_json(result.raw_result), "Modified count": result.modified_count})
    except Exception as e:
        return jsonify({"message": "error", "Info": e.args})

# delete one document


@app.route('/delete_one', methods=['DELETE'])
def delete_one():
    # reference  database and collection  # if dont exist, it will be created
    db = client['Hospital']
    collection = db['Patients']

    try:
        document_to_find = request.get_json()
    except Exception as e:
        return jsonify({"message": "Error parsing json  confirm that Body is not empty and each parameters  have double quotes"}, {"additional info": e.args})

    try:
        # delete one document
        result = collection.delete_one(document_to_find)

        # if document is not found, return message
        if result.deleted_count == 0:
            return jsonify({"message": "Document not found for " + str(document_to_find)})

        return jsonify({"message": "Deleted successfully", "result": parse_json(result.raw_result)})
    except Exception as e:
        return jsonify({"message": "error", "Info": e.args})


# delete many document
@app.route('/delete_many', methods=['DELETE'])
def delete_many():
    # reference  database and collection  # if dont exist, it will be created
    db = client['Hospital']
    collection = db['Patients']

    try:
        document_to_find = request.get_json()

    except Exception as e:
        return jsonify({"message": "Error parsing json  confirm that Body is not empty and each parameters  have double quotes"}, {"additional info": e.args})

    # extract dob from json
    dob = document_to_find['patient_dob']

    # edit json to delete all documents  dob greater than given dob
    document_to_find_updated = {"patient_dob": {"$gt": dob}}

    try:
        # delete many document
        result = collection.delete_many(document_to_find_updated)

        # if document is not found, return message
        if result.deleted_count == 0:
            return jsonify({"message": "Document not found for " + str(document_to_find)})

        return jsonify({"message": "Deleted successfully", "result": parse_json(result.raw_result), "Deleted count": result.deleted_count})
    except Exception as e:
        return jsonify({"message": "error", "Info": e.args})


if __name__ == '__main__':

    app.run(debug=True)
