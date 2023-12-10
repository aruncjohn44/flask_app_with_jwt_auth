from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import numpy as np
from authentication import SECRET_KEY, USERS
from datetime import timedelta

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = SECRET_KEY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)
jwt = JWTManager(app)


# Endpoint for user login to generate a JWT token
@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'The server cannot process the request'}), 400
    
    if USERS.get(auth.username) != auth.password:
        return jsonify({'message': 'Could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

    access_token = create_access_token(identity=auth.username)
    return jsonify({'access_token': access_token}), 200


@app.route('/generate_array', methods=['POST'])
@jwt_required()
def generate_array():
    """
    Generate a random 500-dimensional array in response to a POST request.

    This endpoint takes a sentence as input and returns a random 500-dimensional array of floats.

    Parameters:
    -----------
    request : Request object
        The request object containing JSON data with the key 'sentence'.

    Returns:
    --------
    Response
        A JSON response containing either an error message for invalid input or a random 500-dimensional array.
        If the input is valid, the response format is:
        {
            "result": [float, float, ... (500 floats)]
        }
        If the input is invalid or missing, the response format is:
        {
            "error": "Invalid input"
        }

    HTTP Status Codes:
    ------------------
    200: OK - Response containing the random 500-dimensional array.
    400: Bad Request - Invalid input or missing 'sentence' key in the JSON request.
    """
    current_user = get_jwt_identity()

    data = request.get_json()
    sentence = data.get('sentence')

    # Perform input validation
    if not sentence:
        return jsonify({'error': 'Invalid input'}), 400

    # Generate random 500-dimensional array
    random_array = np.random.rand(500).tolist()

    return jsonify({'result': random_array, 'user': current_user}), 200


if __name__ == '__main__':
    app.run(debug=True)
