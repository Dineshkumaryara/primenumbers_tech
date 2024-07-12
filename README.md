# Django Dish Search Application

This is a Django-based search application that allows users to search for dishes by name. The application filters the dishes and displays the matching results.

## Features

- Search for dishes by name.
- Displays dish name, description, and price.

## Prerequisites

- Python
- Django 
- pip (Python package installer)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Dineshkumaryara/primenumbers_tech.git
    cd primenumbers_tech
    ```

2. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Apply the migrations**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Load initial data** (if you have a `fixtures` file or any other initial data file):

    ```bash
    python manage.py load_dishes.py
    ```

6. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

7. **Access the application**:

    Open your browser and go to `http://127.0.0.1:8000/` to use the application.

## Project Structure

- `restaurant_search/`
- `search_app/` - Contains the Django application code.
  - `management/` - Send data to database.
  - `migrations/` - Database migrations.
  - `templates/` - HTML templates.
  - `admin.py` - Django admin configuration.
  - `apps.py` - Application configuration.
  - `models.py` - Database models.
  - `views.py` - View functions.
  - `urls.py` - URL routing.
- `manage.py` - Django management script.
- `requirements.txt` - Python dependencies.
- `restaurants_small.csv`

## Usage

1. **Search for a dish**:

    - Enter the name of the dish in the search bar and click "Search".
    - The matching results will be displayed below the search bar.

## Customization

- **To add new dishes**:
  - Use the Django admin interface to add new dishes to the database.


