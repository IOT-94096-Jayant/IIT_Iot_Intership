# import Flask class from flask module
from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

# create a server using Flask
server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.route('/soil_moisture', methods=['POST'])
def create_soil_moisture():
    # extract data from request body
    id = request.get_json().get('id')
    moisture = request.get_json().get('moisture')
    from datetime import datetime
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 

    # create a query to add sensor reading into table
    query = f"INSERT INTO soil_moisture VALUES({id}, {moisture}, '{timestamp}');"

    executeQuery(query=query)

    return "Sensor reading is added successfully"

@server.route('/soil_moisture', methods=['GET'])
def retrieve_soil_moisture():
    query = "SELECT * FROM soil_moisture;"
    data = executeSelectQuery(query=query)
    return f"Soil moisture readings: {data}"

@server.route('/soil_moisture', methods=['PUT'])
def update_soil_moisture():
    id = request.get_json().get('id')
    moisture = request.get_json().get('moisture')
    query = f"UPDATE soil_moisture SET moisture = {moisture} WHERE id = {id};"
    executeQuery(query=query)
    return "Sensor reading is updated successfully"

@server.route('/soil_moisture', methods=['DELETE'])
def delete_soil_moisture():
    id = request.get_json().get('id')
    query = f"DELETE FROM soil_moisture WHERE id = {id};"
    executeQuery(query=query)
    return "Sensor reading is deleted successfully"

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=4000, debug=True)
