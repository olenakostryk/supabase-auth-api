# Supabase Auth API

A secure REST API built with **Python, FastAPI, and Supabase Auth**. The project demonstrates user registration, login, JWT-based authentication, protected routes, logout, and Swagger UI documentation with Bearer token authentication.

## Features

* User registration with Supabase Auth
* User login with email and password
* JWT access token authentication
* Refresh token support
* Protected API endpoints
* Reusable FastAPI authentication dependency
* Public API endpoint
* Logout endpoint
* Swagger UI with Bearer authentication
* Environment variables for sensitive configuration

## Tech Stack

* **Python 3.10+**
* **FastAPI**
* **Supabase Auth**
* **Supabase Python SDK**
* **Uvicorn**
* **Pydantic**
* **Git / GitHub**

## Project Structure

```text
supabase-auth-api/
├── .env
├── .gitignore
├── requirements.txt
└── app/
    ├── __init__.py
    ├── main.py
    ├── schemas.py
    ├── supabase_client.py
    ├── dependencies.py
    └── routes/
        ├── __init__.py
        ├── auth.py
        ├── public.py
        └── protected.py
```


## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd supabase-auth-api
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create the `.env` file and add the required Supabase configuration.

## Running the Server

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload --port 8000
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger UI is available at:

```text
http://127.0.0.1:8000/docs
```

## API Reference

| Method | Endpoint               | Authentication | Description                                |
| ------ | ---------------------- | -------------- | ------------------------------------------ |
| POST   | `/auth/signup`         | No             | Create a new user account                  |
| POST   | `/auth/login`          | No             | Authenticate a user and receive JWT tokens |
| POST   | `/auth/logout`         | Yes            | Log out an authenticated user              |
| GET    | `/public/info`         | No             | Return public information                  |
| GET    | `/protected/profile`   | Yes            | Return authenticated user's profile        |
| GET    | `/protected/dashboard` | Yes            | Return authenticated user's dashboard      |

## Authentication Flow

The authentication process uses Supabase as the Identity Provider.

```text
Client
   │
   │ Email + Password
   ▼
Supabase Auth
   │
   │ Access Token (JWT)
   ▼
Client
   │
   │ Authorization: Bearer <JWT>
   ▼
FastAPI
   │
   │ Verify JWT
   ▼
Protected Endpoint
```

### 1. Sign Up

Send a `POST` request to:

```text
/auth/signup
```

Request body:

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

Successful registration returns:

```text
201 Created
```

### 2. Login

Send a `POST` request to:

```text
/auth/login
```

Request body:

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

Successful authentication returns:

```json
{
  "access_token": "JWT_ACCESS_TOKEN",
  "refresh_token": "REFRESH_TOKEN"
}
```

The access token is used to access protected endpoints.

### 3. Access Protected Routes

Protected endpoints require the following HTTP header:

```http
Authorization: Bearer <ACCESS_TOKEN>
```

For example:

```bash
curl -i \
  http://127.0.0.1:8000/protected/profile \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

A valid token returns the authenticated user's information.

An invalid, expired, or missing token returns:

```text
401 Unauthorized
```

## Public Endpoint

The `/public/info` endpoint does not require authentication.

```bash
curl -i http://127.0.0.1:8000/public/info
```

Response:

```json
{
  "message": "Welcome stranger! This info is public."
}
```

## Protected Endpoints

### Profile

```text
GET /protected/profile
```

Returns information about the authenticated user.

### Dashboard

```text
GET /protected/dashboard
```

Returns dashboard information for the authenticated user.

Both endpoints require a valid Bearer token.

## Logout

The logout endpoint is protected and requires authentication:

```text
POST /auth/logout
```

Example:

```bash
curl -i -X POST \
  http://127.0.0.1:8000/auth/logout \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

A successful logout returns:

```text
204 No Content
```

## Error Handling

The API uses appropriate HTTP status codes for authentication operations:

| Status Code | Meaning                                           |
| ----------- | ------------------------------------------------- |
| `200`       | Successful login or protected request             |
| `201`       | User successfully created                         |
| `204`       | Successful logout                                 |
| `400`       | Missing or invalid input                          |
| `401`       | Missing, invalid, or expired authentication token |

## Swagger Documentation

FastAPI automatically generates interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

The Swagger UI provides an **Authorize** button for Bearer authentication.

To test protected endpoints:

1. Log in through `/auth/login`.
2. Copy the returned `access_token`.
3. Click **Authorize** in Swagger UI.
4. Enter the access token.
5. Execute `/protected/profile` or `/protected/dashboard`.

### Swagger Screenshot

Add your Swagger screenshot to the repository, for example:

```text
docs/swagger.png
```

Then include it here:

![Swagger UI](docs/swagger.png)

## Security

* Supabase handles user authentication and password management.
* JWT access tokens are verified through Supabase.
* Protected routes use a reusable FastAPI authentication dependency.
* Supabase credentials are stored in environment variables.
* `.env` is excluded from Git using `.gitignore`.
* Sensitive tokens and credentials should never be committed to the repository.

## Git Commit Stages

The project was developed incrementally according to the assignment stages:

```text
Stage 0: setup server and supabase client
Stage 1: signup and login routes working
Stage 2: public route and unverified protected route
Stage 3: profile route token verification
Stage 4: auth middleware and logout endpoint
Stage 5: Swagger UI documentation with bearer auth
Stage 6: publish to GitHub and write README
```

## Testing

The API can be tested using:

* Swagger UI at `/docs`
* `curl`
* FastAPI's interactive API documentation

Important authentication tests include:

```text
Signup with valid credentials       → 201
Login with valid credentials        → 200
Login with incorrect credentials    → 401
Protected route without token       → 401
Protected route with valid token    → 200
Protected route with invalid token  → 401
Logout with valid token             → 204
Public endpoint without token       → 200
```

## License

This project was created as part of a FlyRank AI assignment.
