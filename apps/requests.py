import os
import logging
import requests
import json

def getAPI(url, headers):
    response = {}
    logger.info("GET URL =>  %s \n\nGET Headers => %s" % (json.dumps(url), json.dumps(headers)))

    try:
        apiResponse = requests.get(url, headers = headers)
        apiResponse = apiResponse.json()
        
        response['hasError'] = False
        response['result'] = apiResponse
        return response
    except Exception as error:

        print("Unsuccessful GET API call \n\nGET URL: %s \n\nGET Headers: %s" % (json.dumps(url), json.dumps(headers)))
        
        response['hasError'] = True
        response['error'] = error
        return response

def postAPI(url, headers, data):
    response = {}
    print("POST URL =>  %s \n\nPOST Headers => %s \n\nPOST Data => %s " % (json.dumps(url), json.dumps(headers), json.dumps(data)))
    
    try:
        apiResponse = requests.post(url, headers=headers, data=json.dumps(data))
        apiResponse = apiResponse.json()
        
        response['hasError'] = False
        response['result'] = apiResponse
        return response

    except Exception as error:

        print("Unsuccessful POST API call \n\nPOST URL: %s \n\nPOST Headers: %s \n\nPOST Data: %s" % (json.dumps(url), json.dumps(headers), json.dumps(data)))

        response['hasError'] = True
        response['error'] = error
        return response

def putAPI(url, headers, data):
    response = {}
    print("PUT URL =>  %s \n\nPUT Headers => %s \n\nPUT Data => %s" % (json.dumps(url), json.dumps(headers), json.dumps(data)))

    try:
        apiResponse = requests.put(url, headers=headers, data=json.dumps(data))
        apiResponse = apiResponse.json()
        
        response['hasError'] = False
        response['result'] = apiResponse
        return response

    except Exception as error:

        print("Unsuccessful PUT API call \n\nPUT URL: %s \n\nPUT Headers: %s \n\nPUT Data: %s" % (json.dumps(url), json.dumps(headers), json.dumps(data)))

        response['hasError'] = True
        response['error'] = error
        return response