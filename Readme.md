# MongoDB python

This is a sole project done during my traineeship at Fusemachines Nepal. This project includes topics like API, MongoDB, Python, Flask etc.

## Create and activate a virtual environment:

`>> python -m venv env_name`

`>> . env_name/bin/activate`

Use `pip install -r requirements.txt` to install the required packages.

## Import Postman config
 Use file *Mongo Project.postman_collection.json* to import the config

## Input format
+ Raw json in body part of url ( Recommened  to use postman )
  
## API and Descriptions
| **API**      | **Description**                                                                                                           |
| ------------ | ------------------------------------------------------------------------------------------------------------------------- |
| /insert_one  | Insert one document in the database                                                                                       |
| /insert_many | Insert many documents in the database(No argument in body)                                                                |
| /find_one    | Find one document in the database that has name "Bond007"                                                                 |
| /find_all    | Find all documents in the database having city "Chitwan"                                                                  |
| /update_one  | Update one document in the database , change the name of the document having name "baburam shrestha" to "Baburao Mastani" |
| /update_many | Update many documents in the database , change the name of the document having city "kathmandu" to "Sindupalchowk"        |
| /delete_one  | Delete one document in the database having name "Baburao Mastani"                                                         |
| /delete_many | Delete many documents in the database having dob greater than "1990"                                                      |







