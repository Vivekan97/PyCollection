from flask import Flask, request  # importing Flask app and request
from requests import get  # to send get request to googleapi

app = Flask(__name__)  # an instance of flask app

API_KEY = "AIzaSyCOD3KvY2DDzEfel-NZ_LKIWXr86EF_EUw"  # api key to access google api
BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"  # google api base url


# function for returning the response in JSON format
def json_result(address: str, coordinates: dict) -> dict:
    return {"coordinates": coordinates, "address": address}


# function for returning the response in xml format
def xml_result(address: str, latitude: float, longitude: float):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<root>
    <address>{address}</address>
    <coordinates>
        <lat>{latitude}</lat>
        <lng>{longitude}</lng>
    </coordinates>
</root>"""


# Post method uri
@app.route("/getmyaddress", methods=['POST', ])
def get_address():
    address = request.get_json().get("address", None)  # reading address from request body
    output_format = request.get_json().get("output_format", None)  # reading output_format from request body
    #  if address and output_format both are missing in request
    if address and output_format is None:
        return {"error_message": "address field, output_format should not be empty"}, 400
    # if address is missing or empty
    if address is None or address == "":
        return {"error_message": "address field should not be empty"}, 400
    # if output_format is missing or empty
    if output_format is None:
        return {"error_message": "output_format should not be empty"}, 400
    # if output_format contains other than json or xml
    if output_format and output_format.lower() not in ("json", "xml"):
        return {"error_message": "output_format should be either json or xml"}, 400

    # if address and output_format is valid
    if address and output_format:
        request_params = {"address": address, "key": API_KEY}
        geocoding_api_response = get(url=BASE_URL, params=request_params)
        if geocoding_api_response.status_code == 200:
            my_coordinates = geocoding_api_response.json()["results"][0]['geometry']['location']
            if output_format.lower() == 'json':
                # if json response is required
                return json_result(coordinates=my_coordinates, address=address), 200
            if output_format.lower() == 'xml':
                # if xml response is required
                return xml_result(latitude=my_coordinates["lat"], longitude=my_coordinates["lng"], address=address), 200
    # for any other invalid requests
    return {"error": "Invalid Request"}, 400


if __name__ == "__main__":
    app.run(debug=True, port=5000)
