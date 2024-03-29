# User Form Project

This project is a Django-based web application that allows users to submit their details through a form. The submitted data is validated and saved to the database. Additionally, upon successful submission, a confirmation email is sent to the user's email address.

## Features

- Users can submit their details (name, date of birth, email, phone number) through a form.
- Frontend validation is performed for name, email, and date of birth fields.
- Backend validation ensures that the user is at least 18 years old and performs phone number validation.
- Submitted data is saved to the database.
- Confirmation email is sent to the user upon successful submission.
- Users can view all submitted forms on a separate page.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/nikhilrai-tech/Storlyy.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd user-form-project
    ```

3. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Start the Django development server:**

    ```bash
    python manage.py runserver
    ```
