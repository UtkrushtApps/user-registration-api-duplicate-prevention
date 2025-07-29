# User Registration API - Duplicate Prevention

## Task Overview
A growing SaaS platform is onboarding new users through a public registration form. However, the current backend implementation allows multiple user records to be created with the same email address, causing confusion and security issues. The business needs to ensure that each email address is registered exactly once, and that attempts to register an existing email are clearly rejected with a user-friendly error.

## Guidance
This project is a FastAPI backend connected to a PostgreSQL database using SQLAlchemy's async ORM. You will work within an existing code structure that follows best practices for separation of routers, models, services, and database sessions. All database access should be performed asynchronously, and environment variables are used for configuration. The API must handle attempts to register the same email more than once gracefully, using database-level constraints and clear error messages. Containerization is provided via Docker and Docker Compose, with all credentials and ports managed through environment variables. Review the business logic and ensure that your implementation enforces uniqueness at the database layer and provides appropriate HTTP responses for duplicate registration attempts.

## Objectives
- Implement a user registration endpoint that prevents duplicate registrations using the same email address.
- Add a unique constraint on the 'email' field at the database level for the users table.
- Ensure the API responds with a clear and appropriate error message and HTTP status code when a duplicate email is submitted.
- All API/database interactions must be asynchronous and follow FastAPI patterns.
- Adhere to the provided project structure, using Pydantic for request and response models.
- Use Docker and Docker Compose to run the full stack with environment-based configuration.

## How to Verify
- Registering a new user with a unique email address returns a 201 Created status and the user data.
- Attempting to register a user with an email that already exists returns a 400 Bad Request (or similar) with a clear error message.
- The users table in PostgreSQL does not contain duplicate emails under any circumstances.
- All containers start successfully using Docker Compose, and the API is accessible.
