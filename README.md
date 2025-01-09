# Fitness Tracker API

## Endpoints

### Exercise
- **GET** `/api/exercises/` - Get all exercises.
- **POST** `/api/exercises/` - Create a new exercise.
- **GET** `/api/exercises/<id>/` - Get a specific exercise.
- **PUT** `/api/exercises/<id>/` - Update a specific exercise.
- **DELETE** `/api/exercises/<id>/` - Delete a specific exercise.

### Activity
- **GET** `/api/activities/` - Get all activities.
- **POST** `/api/activities/` - Create a new activity.
- **GET** `/api/activities/<id>/` - Get a specific activity.
- **PUT** `/api/activities/<id>/` - Update a specific activity.
- **DELETE** `/api/activities/<id>/` - Delete a specific activity.

### Metrics
- **GET** `/api/activities/metrics/` - Get activity metrics (total duration, calories, distance, etc.).

## How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run migrations: `python manage.py migrate`.
4. Start the server: `python manage.py runserver`.
