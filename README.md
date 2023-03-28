# Prerequisites
In order to run the files in this repository, you must first have the AWS CLI set up on your device along with a local copy of dynamodb. It must be pre-configured with an access key and the local copy of dynamodb must be running.

# The following files are currently available in this repository:
## 1. data.json
 - This file contains the inital data to be loaded if the table is re-initialized using the initialize_table.py script

## 2. intialize_table.py
 - This script creates the items table and loads it with the data from data.json

## 3. item_manipulations.py
 - This file contains all of the methods that will be needed to manipulate the items in the database.

## 4. delete_table.py
 - This script deletes the items table and all items in it.

# References:
https://docs.aws.amazon.com/code-library/latest/ug/python_3_dynamodb_code_examples.html
https://www.section.io/engineering-education/python-boto3-and-amazon-dynamodb-programming-tutorial/
