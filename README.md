
# Healthcare API

This is a Django REST API backend for a healthcare application. It provides endpoints for user registration, login (using JWT), patient and doctor management, and mapping patients to doctors. The project is also Dockerized and uses PostgreSQL as its database.

## Features

- **User Authentication:** Register and login using JWT.
- **Patient Management:** Create, list, update, and delete patient records.
- **Doctor Management:** Create, list, update, and delete doctor records.
- **Mapping:** Assign doctors to patients.
- **API Documentation:** Swagger UI available at `/swagger/`.
- **Dockerized:** Runs in Docker containers with PostgreSQL.

## Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Quick Start


1. **Create a `.env` File:**

   Create a `.env` file in the project root with the following variables (adjust as needed):

   ```
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=db
   DB_PORT=5432
   ```

2. **Build and Run the Containers:**

   ```bash
   docker-compose up --build
   ```

3. **Run Migrations:**

   In a new terminal, run:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. **Access the API:**

   - API Base URL: [http://localhost:8000](http://localhost:8000)
   - Swagger UI: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

## API Endpoints

- **Authentication:**
  - `POST /api/auth/register/` - Register a new user.
  - `POST /api/auth/login/` - Login and get a JWT token.
- **Patients:**
  - `POST /api/patients/` - Add a new patient.
  - `GET /api/patients/` - Retrieve patients.
  - `GET /api/patients/<id>/` - Get patient details.
  - `PUT /api/patients/<id>/` - Update a patient.
  - `DELETE /api/patients/<id>/` - Delete a patient.
- **Doctors:**
  - `POST /api/doctors/` - Add a new doctor.
  - `GET /api/doctors/` - Retrieve doctors.
  - `GET /api/doctors/<id>/` - Get doctor details.
  - `PUT /api/doctors/<id>/` - Update a doctor.
  - `DELETE /api/doctors/<id>/` - Delete a doctor.
- **Mappings:**
  - `POST /api/mappings/` - Assign a doctor to a patient.
  - `GET /api/mappings/` - Retrieve all mappings.
  - `GET /api/mappings/<patient_id>/` - Get mappings for a specific patient.
  - `DELETE /api/mappings/<id>/` - Remove a mapping.
