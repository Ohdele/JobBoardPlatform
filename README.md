# Job Board Platform

# Project Setup

## Overview
Create a job board where users can post job listings and apply for jobs. This project includes:
- **Backend**: Python (Flask)
- **Frontend**: JavaScript (React)
- **Additional Features**: Java (notifications, advanced search)

## Project Structure
- `frontend`: Contains React application code.
- `backend`: Contains Flask application code.
- `java-services`: Contains Java code for additional features.

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/Ohdele/JobBoardPlatform.git




## Backend Development (Flask)

### Overview
I focused on setting up the backend for the JobBoardPlatform project using Flask. This involved initializing a Flask project, configuring the environment, developing API endpoints, and testing them. 

### Backend Setup

1. **Initialize Flask Project:**
   - Created a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activated the virtual environment:
     ```bash
     venv\Scripts\activate
     ```
   - Installed Flask:
     ```bash
     pip install Flask
     ```

2. **Database Setup:**
   - Installed necessary packages:
     ```bash
     pip install SQLAlchemy psycopg2-binary
     ```
   - Configured PostgreSQL/MySQL.
   - Created models for Users, Job Listings, and Applications.

3. **API Development:**
   - Implemented CRUD endpoints for:
     - User Registration/Login
     - Create/Read/Update/Delete Job Listings
     - Apply for Jobs
   - Secured endpoints with JWT authentication:
     ```bash
     pip install Flask-JWT-Extended
     ```

4. **Testing:**
   - Wrote unit tests using `pytest`.
   - Wrote integration tests for API endpoints.

### Route Workflow

- **User Registration/Login:**
  - **Endpoint:** `POST /login`
  - **Description:** Authenticate a user and return a JWT token.

- **Create Job Listing:**
  - **Endpoint:** `POST /jobs`
  - **Description:** Create a new job listing.

- **Read Job Listings:**
  - **Endpoint:** `GET /jobs`
  - **Description:** Retrieve a list of job listings.

- **Update Job Listing:**
  - **Endpoint:** `PUT /jobs/<job_id>`
  - **Description:** Update a specific job listing.

- **Delete Job Listing:**
  - **Endpoint:** `DELETE /jobs/<job_id>`
  - **Description:** Delete a specific job listing.
