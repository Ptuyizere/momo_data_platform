# Momo API

## Overview

This is a simple REST API for the Momo Data Platform project. It full implements CRUD (Create, Read, Update, Delete) operations using nothing but pure python with no third party frameworks/libraries.
 . Built on python's built-in http.server
 . Stores data in memory and any changes to a JSON file
 . Uses basic authentication

## Requirements

 . Python 3.8+

## How to run

1. Make sure the project has the correct data/raw and data/processed folders
2. The files data/raw/modified_sms_v2.xml and data/processed/modified_sms_v2.json must both be available.
3. Before launching the server, ensure that the xml data has been parsed to json by running dsa/parse_xml.py
4. Run the server:
   cd api
   python server.py
3. The server will be running at:
   http://127.0.0.1:8000

## Authentication

The server uses basic authentication for every endpoint.
The default credentials are provided here:
 Username: admin
 Password: secret

Example using curl:
 curl -u admin:secret http://127.0.0.1:8000/transactions

## API Endpoints

1. Get all transactions
  GET /transactions

 Request Example:
  curl -u admin:secret http://127.0.0.1:8000/transactions

Request Response:
 [
    {
        "protocol": "0",
        "address": "M-Money",
        "date": "1715351458724",
        "type": "1",
        "subject": "null",
        "body": "You have received 2000 RWF from Jane Smith (*********013) on your mobile money account at 2024-05-10 16:30:51. Message from sender: . Your new balance:2000 RWF. Financial Transaction Id: 76662021700.",
        "toa": "null",
        "sc_toa": "null",
        "service_center": "+250788110381",
        "read": "1",
        "status": "-1",
        "locked": "0",
        "date_sent": "1715351451000",
        "sub_id": "6",
        "readable_date": "10 May 2024 4:30:58 PM",
        "contact_name": "(Unknown)",
        "id": 1
    },
    {
        "protocol": "0",
        "address": "M-Money",
        "date": "1715351506754",
        "type": "1",
        "subject": "null",
        "body": "TxId: 73214484437. Your payment of 1,000 RWF to Jane Smith 12845 has been completed at 2024-05-10 16:31:39. Your new balance: 1,000 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije.",
        "toa": "null",
        "sc_toa": "null",
        "service_center": "+250788110381",
        "read": "1",
        "status": "-1",
        "locked": "0",
        "date_sent": "1715351498000",
        "sub_id": "6",
        "readable_date": "10 May 2024 4:31:46 PM",
        "contact_name": "(Unknown)",
        "id": 2
    }
 ]

2. Get one transaction
  GET /transactions/{id}

 Request Example:
  curl -u admin:secret http://127.0.0.1:8000/transactions/2

 Response Example:
   {
        "protocol": "0",
        "address": "M-Money",
        "date": "1715351506754",
        "type": "1",
        "subject": "null",
        "body": "TxId: 73214484437. Your payment of 1,000 RWF to Jane Smith 12845 has been completed at 2024-05-10 16:31:39. Your new balance: 1,000 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije.",
        "toa": "null",
        "sc_toa": "null",
        "service_center": "+250788110381",
        "read": "1",
        "status": "-1",
        "locked": "0",
        "date_sent": "1715351498000",
        "sub_id": "6",
        "readable_date": "10 May 2024 4:31:46 PM",
        "contact_name": "(Unknown)",
        "id": 2
    }

3. Create a transaction
  POST /transactions
 
 Request Example:
  curl -u admin:secret -X POST http://127.0.0.1:8000/transactions \
    -H "Content-Type: application/json" \
    -d '{
        "protocol": "0",
        "address": "M-Money",
        "date": "1715600000000",
        "type": "1",
        "body": "TxId: 999888777. Your payment of 5,000 RWF ...",
        "readable_date": "13 May 2024 2:15:30 PM"
    }'
 
 Response Example:
  {
    "protocol": "0",
    "address": "M-Money",
    "date": "1715600000000",
    "type": "1",
    "body": "TxId: 999888777. Your payment of 5,000 RWF ...",
    "readable_date": "13 May 2024 2:15:30 PM",
    "id": 9
  }

4. Update a transaction
  PUT /transactions/{id}

 Request Example:
  curl -u admin:secret -X PUT http://127.0.0.1:8000/transactions/1 \
    -H "Content-Type: application/json" \
    -d '{
        "protocol": "0",
        "address": "M-Money",
        "date": "1715351458724",
        "type": "1",
        "body": "Updated SMS body example",
        "readable_date": "10 May 2024 4:30:58 PM"
    }'
 
 Response Example:
  {
    "protocol": "0",
    "address": "M-Money",
    "date": "1715351458724",
    "type": "1",
    "body": "Updated SMS body example",
    "readable_date": "10 May 2024 4:30:58 PM",
    "id": 1
  }

5. Delete a transaction
  DELETE /transactions/{id}
 
 Rquest Example:
  curl -u admin:secret -X DELETE http://127.0.0.1:8000/transactions/1

 Response Example:
  {
    "message": "Deleted"
  }

## Error Codes

Here are the different error codes used:
 . 401 Unauthorized -> Invalid credentials.
 . 404 Not Found -> transaction ID not found.
 . 400 Bad Request -> Invalid ID format.
 . 200 Request successful -> The server has responded as expected.
 . 201 Resource Creation -> POST has successfully created the resource.