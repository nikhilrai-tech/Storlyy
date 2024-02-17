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
    git clone https://github.com/your-username/user-form-project.git
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

7. **Start Celery worker (in a separate terminal):**

    ```bash
    celery -A user_form_project worker -l info
    ```

8. **(Optional) Start RabbitMQ server if not already running:**

    ```bash
    rabbitmq-server
    ```

## Usage

1. Access the web application at http://localhost:8000/user-form/.
2. Fill out the form with your details and submit it.
3. Upon successful submission, you will receive a confirmation email at the provided email address.
4. To view all submitted forms, navigate to http://localhost:8000/user-form/list_forms/.

## Deployment

This project can be deployed to a production environment using platforms like Heroku, PythonAnywhere, or any other cloud server provider. Make sure to configure the necessary environment variables for production settings, including database and email configurations.

## Contributing

Contributions are welcome! If you would like to contribute to this project, feel free to submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
