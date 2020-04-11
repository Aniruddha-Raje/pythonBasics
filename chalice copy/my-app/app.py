from chalice import Chalice, Response
from chalice import BadRequestError
from chalicelib import s3_service 
from chalicelib import s3_sqs_service
import os
import boto3

app = Chalice(app_name='my-app')

country_dict={  
   "countries":{  
      "USA":[  
         "Alabama",
         "Alaska",
         "Arizona",
         "Arkansas",
         "California",
         "Colorado",
         "Connecticut",
         "Delaware",
         "Florida",
         "Georgia",
         "Hawaii",
         "Idaho",
         "Illinois",
         "Indiana",
         "Iowa",
         "Kansas",
         "Kentucky",
         "Louisiana",
         "Maine",
         "Maryland",
         "Massachusetts",
         "Michigan",
         "Minnesota",
         "Mississippi",
         "Missouri",
         "Montana",
         "Nebraska",
         "Nevada",
         "New Hampshire",
         "New Jersey",
         "New Mexico",
         "New York",
         "North Carolina",
         "North Dakota",
         "Ohio",
         "Oklahoma",
         "Oregon",
         "Pennsylvania",
         "Rhode Island",
         "South Carolina",
         "South Dakota",
         "Tennessee",
         "Texas",
         "Utah",
         "Vermont",
         "Virginia",
         "Washington",
         "West Virginia",
         "Wisconsin",
         "Wyoming"
      ],
      "Canda":[  
         "British Columbia",
         "Alberta",
         "Manitoba",
         "Ontario",
         "Prince Edward Island",
         "Newfoundland",
         "Saskatchewan",
         "New Brunswick",
         "Quebec",
         "Nova Scotia"
      ]
   }
}

@app.route('/')
def index():
    return {'hello': 'world'}

# Path Params
@app.route('/department/{value}', methods=['GET'])
def process_departments(value):
    return {"my_department": value}

# Query Parameters
@app.route('/department', methods=['GET'])
def process_departments_query():
    my_params=app.current_request.query_params
    my_response={
      "all_parameters":my_params,
      "selected_department":my_params['department_id']
    }
    return my_response

# Query Parameters with error handling
@app.route('/countries', methods=['GET'])
def process_countries_get():
   requested_country=app.current_request.query_params['country']
   states=[]
   for key,item in country_dict['countries'].items():
      if key==requested_country:
         states=item
   if len(states)>0:
      return {"states":','.join(states)}
   else:
      raise BadRequestError("Unknown country '%s', valid choices are: %s" % (
            requested_country, ', '.join(country_dict['countries'].keys())))

# POST Method
@app.route('/countries', methods=['POST'])
def process_countries():
    my_dict = app.current_request.json_body['countries']
    usa_states=[]
    for key, item in my_dict.items():
        if key == 'USA':
            usa_states=item
    return {"status_code": 200,
            "message": "successfully processed for countries JSON",
            "states": ','.join(usa_states)
            }

# Response type text/plain
@app.route('/text')
def text():
    return Response(body='This is text message',
                    status_code=200,
                    headers={'Content-Type': 'text/plain'})

################################################################################

# Read from Enviornment Variables
@app.route('/enviorment', methods=['GET'])
def process_enviornment():
   application_name=os.environ['application_name']
   db_user=os.environ['db_user']
   db_url=os.environ['db_url']
   return {
   "Application Name": application_name,
   "DB user": db_user,
   "DB URL":db_url
   }

################################################################################

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
