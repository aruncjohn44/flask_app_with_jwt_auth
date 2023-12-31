# Flask App with JWT Authentication and Array Generation

This Flask application provides endpoints for user authentication using JWT (JSON Web Token) and generating random arrays based on user input.

## Setup

1. **Installation**
   - Clone this repository.
   - Install the required packages using `pip install -r requirements.txt`.

2. **Running the Application**
   - Run `python flask_app.py` to start the Flask server.
   - Access the application at `http://localhost:5000`.

## Endpoints

### User Login Endpoint

- **Endpoint:** `/login`
- **Method:** `POST`
- **Description:** Authenticates the user and generates a JWT token.
- **Payload:**

{
"username": "your_username",
"password": "your_password"
}

- **Response (Success):**

{
"access_token": "<generated_token>"
}

- **Response (Error):**

{
"message": "Could not verify",
"WWW-Authenticate": "Basic auth="Login required""
}


### Array Generation Endpoint

- **Endpoint:** `/generate_array`
- **Method:** `POST`
- **Description:** Generates a random 500-dimensional array based on user input.
- **Authentication:** JWT Token required in the header (`Authorization: Bearer <access_token>`)
- **Payload:** {
"sentence": "your_sentence"
}
  - **Response (Success):**

{
"result": [array_of_500_random_numbers],
"user": "current_user"
}
- **Response (Error):**
{
"error": "Invalid input"
}
  
## JWT Configuration

- **Secret Key:** Ensure to set the `JWT_SECRET_KEY` in the Flask application for security.
- **Token Expiry:** Tokens expire after 15 minutes (`JWT_ACCESS_TOKEN_EXPIRES`).

## Example Usage

1. **User Login:**
POST http://localhost:5000/login
Body:
{
"username": "your_username",
"password": "your_password"
}
edit the username and passwords in the credentials file so that you can use the credentials you prefer
   
2. **Generate Array:**
POST http://localhost:5000/generate_array
Headers:
Authorization: Bearer <generated_token>
Body:
{
"sentence": "your_sentence"
}

## Notes

- Ensure proper input validation before processing requests.
- Use the JWT token in the header for authorized endpoints.
- Modify the expiration time for tokens based on your requirements.
- 
## Code Structure and Readability
- **Modularization:** 
  Broken the code into modular components (e.g., separate files for routes, utilities, models) for better organization and maintainability.
- **Comments and Documentation:**
  Provided  comments and docstrings to explain complex logic, endpoints, and functions.
- **Consistent Coding Style:**
  Followed PEP 8 guidelines for Python code consistency.
## Security
- **Input Validation:**
  Validated user inputs to prevent common security vulnerabilities like SQL injection, cross-site scripting (XSS), etc.
- **JWT Security:**
  Ensure secure handling and validation of JWT tokens. Use strong secret keys and appropriate token expiration times.
- **HTTPS:**
  Deploy the application behind HTTPS for encrypted communication between clients and the server.
## Error Handling
- **Custom Error Responses:**
  Provided informative and consistent error messages and status codes for failed requests.
## Testing
-**Unit Tests**: 
Unit tests using framework - unittest  to ensure individual components work as expected.
