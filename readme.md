# Symptom Checker

Symptom Checker is a Django web application that helps users identify possible diseases based on their symptoms and provides suggestions for relevant doctors.

## Features

- Users can input their name, gender, age, and select their symptoms.
- The application analyzes the symptoms and matches them with relevant diseases.
- It suggests doctors specialized in treating the identified diseases.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MehediMK/symptom-checker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd symptom-checker
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Load fixtures for initial data:

   ```bash
   python manage.py loaddata patient_fixture.json
   python manage.py loaddata symptom_fixture.json
   python manage.py loaddata disease_fixture.json
   python manage.py loaddata doctor_fixture.json
   ```

6. Create a superuser to access the Django admin:

    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

8. Visit http://localhost:8000/ in your web browser to access the symptom checker application.

## Usage

1. Access the symptom checker form by visiting the homepage.
2. Enter your name, gender, age, and select your symptoms.
3. Click the "Check Symptoms" button.
4. View the results page to see matching diseases and suggested doctors.

## Contributing

Contributions are welcome! Here's how you can contribute to the project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Credits

This project was created by [Mehedi Khan](https://github.com/MehediMK).




