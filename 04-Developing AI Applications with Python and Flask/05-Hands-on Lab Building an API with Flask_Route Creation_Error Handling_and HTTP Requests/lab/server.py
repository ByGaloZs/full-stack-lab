from flask import Flask, make_response, request
import requests

# Create an instance of the Flask app
app = Flask(__name__)

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

# Define a route for the root URL ("/")
@app.route("/")
def index():
    """
    Handle requests to the root URL ("/").

    Returns:
        str: A plain text "Hello World" response.
    """
    return "Hello World"


# Define a route for the root URL ("/no_content")
@app.route("/no_content")
def no_content():
    """
    Return a JSON message with HTTP status code 204 (No Content).

    Returns:
        dict: JSON response message.
        int: HTTP status code (204).
    """
    return {"message": "No content found"}, 204


# Define a route for the root URL ("/exp")
@app.route("/exp")
def index_explicit():
    """
    Return Hello World! with a status code of 200

    Returns:
        str: Hello World!
        status code: 200
    """
    res = make_response("Hello World!")
    res.status_code = 200
    return res


# Define a route for the root URL ("/data")
@app.route("/data")
def get_data():
    try:
        # Check if 'data' exists and has a length greater than 0
        if data and len(data) > 0:
            # Return a JSON response with a message indicating the length of the data
            return {"message": f"Data of length {len(data)} found"}
        else:
            # If 'data' is empty, return a JSON response with a 500 Internal Server Error status code
            return {"message": "Data is empty"}, 500
    except NameError:
        # Handle the case where 'data' is not defined
        # Return a JSON response with a 404 Not Found status code
        return {"message": "Data not found"}, 404


# Define a route for the root URL ("/name_search")
@app.route("/name_search")
def name_search():
    """
    Find a person in the database based on the provided query parameter.
    Returns:
        json: Person if found, with status of 200
        404: If not found
        400: If the argument 'q' is missing
        422: If the argument 'q' is present but invalid (e.g., empty or numeric)
    """
    # Get the argument 'q' from the query parameters of the request
    query = request.args.get('q')

    #Check if the query parameter 'q' is missing
    if query is None:
        return{"message": "Query parameter 'q' is missing"}, 400
    
    # Check if the query parameter is present but invalid (e.g., empty or numeric)
    if query.strip() == "" or query.isdigit():
        return {"message": "Invalid input parameter"}, 422
    
    # Iterate through the 'data' list to look for the person whose first name matches the query
    for person in data:
        if query.lower() in person["first_name"].lower():
            return person, 200

    # If no match is found, return a JSON response with a message indicating the person was not found and a 404 Not Found status code    
    return {"message": "Person not Found"}, 404

# Define a route for the root URL ("/count")
@app.route("/count")
def count():
    """
    Return the number of items in the global `data` list.

    If `data` is defined, returns a JSON response containing the count
    and an HTTP 200 status code.

    If `data` is not defined, returns a JSON error message with an
    HTTP 500 status code.

    Returns:
        tuple:
            dict: JSON response with item count or error message.
            int: HTTP status code (200 or 500).
    """
    try:
        # Attempt to return a JSON response with the count of items in 'data'
        return {"data count": len(data)}, 200
    except NameError:
        # If 'data' is not defined and raises a NameError
        # Return a JSON response with a message and a 500 Internal Server Error status code
        return {"message": "data not defined"}, 500


@app.route("/person/<uuid>")
def find_by_uuid(uuid):
    """
    Find and return a person from the 'data' list by their UUID.

    Iterates through the `data` list searching for a person whose
    'd' field matches the provided UUID.

    Args:
        uuid (str): Unique identifier of the person to search for.

    Returns:
        tuple:
            dict: JSON object representing the person if found.
            int: HTTP status code 200.

        If no match is found:
            tuple:
                dict: JSON error message.
                int: HTTP status code 404.
    """
    # Iterate through the 'data' list to search for a person with a matching ID
    for person in data:
        # Check if the 'id' field matches the UUID parameter
        if person["id"] == str(uuid):
            return person, 200

    # If no matching person is found, return 404
    return {"message": "Person not found"}, 404



@app.route("/person/<uuid:id>", methods=["DELETE"])
def delete_person(id):
    """
    Delete a person from the `data` list by their UUID.

    Searches through the `data` list for a person whose `id` field
    matches the provided identifier. If found, removes the person
    from the list and returns a success message with HTTP status
    code 200.

    If no matching person is found, returns an error message with
    HTTP status code 404.

    Args:
        id (str): Unique identifier of the person to delete.

    Returns:
        tuple:
            dict: JSON success or error message.
            int: HTTP status code (200 or 404).
    """
    for person in data:
        if person["id"] == str(id):
            # Remove the person from the data list
            data.remove(person)

            return {"message": "Person with ID deleted"}, 200

    # If no person with the given ID is found
    return {"message": "Person not found"}, 404


@app.route("/person", methods=["POST"])
def add_by_uuid():
    """
    Add a new person to the global `data` list using JSON from the request.

    Expects a JSON payload containing the person's information.
    If the payload is missing or invalid, returns an error message
    with HTTP status code 422 (Unprocessable Entity).

    Attempts to append the new person to the `data` list. If the
    `data` variable is not defined, returns an error message with
    with HTTP status code 500 (Internal Server Error).

    On success, returns the ID of the newly created person.

    Returns:
        tuple:
            dict: JSON response message.
            int: HTTP status code (200, 422, or 500).
    """
    new_person = request.json

    if not new_person:
        return {"message": "Invalid input parameter"}, 422

    # Code to validate new_person omitted
    try:
        data.append(new_person)
    except NameError:
        return {"message": "data not defined"}, 500

    return {"message": f"{new_person['id']}"}, 200


@app.errorhandler(404)
def api_not_found(error):
    """
    Handle 404 Not Found errors and return a JSON response.

    Args:
        error: The error object provided by Flask.

    Returns:
        tuple: JSON message and HTTP 404 status code.
    """
    return {"message": "API not found"}, 404


@app.errorhandler(Exception)
def handle_exception(e):
    """
    Handle unhandled exceptions globally and return a JSON response.

    Args:
        e (Exception): The exception that was raised.

    Returns:
        tuple: JSON message with the exception text and HTTP 500 status code.
    """
    return {"message": str(e)}, 500
