# Shiba
## The users microservice

The **users service** is a backend API designed to handle user authentication, registration, and management for shiba application. It is built using FastAPI and provides a set of RESTful endpoints to create, update, retrieve, and delete user information. The service is equipped with secure user authentication mechanisms such as JWT (JSON Web Token) and OAuth, ensuring that users' data is protected.

This service includes the following features:

  - [x] **User Registration**: Allows new users to create accounts.
  - [ ] **User Login**: Authenticates users and provides them with a secure access token (JWT).
  - [ ] **Profile Management**: Users can update their personal details and manage their settings.
  - [ ] **Password Reset**: Provides a mechanism for users to reset their password securely.
  - [ ] **Secure Authentication**: Integrates with OAuth providers (e.g., Google, GitHub) for social login options.

The User Service is built to scale and integrate seamlessly with other microservices, making it an ideal solution for modern applications requiring robust user management capabilities.

To boostrap the service:
```shell
docker compose up --build
```
