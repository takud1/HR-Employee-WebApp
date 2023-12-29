# HR-Employee-WebApp

## Project Overview

HR-Employee-WebApp is a web application that aims to ease the process of integrating an employee into the organization. It automates the most basic interaction of the new employee with the Human Resources team of the organization, such as submission of documents. It also allows the employee to obtain a schedule of other existing employees through the app, so as to meet these people at a convenient time and get properly oriented.

## Project Requirements

This web app is built using the Django Stack. The following technologies, frameworks, libraries, and tools are used:

- **Bootstrap**: A popular HTML, CSS, and JavaScript framework for developing responsive, mobile-first websites. It provides design templates and CSS classes for typography, forms, buttons, navigation, and other interface components.
- **Django**: A high-level Python web framework that follows the model-template-view (MTV) architectural pattern. It enables rapid development and clean, pragmatic design of web applications.
- **SQLite**: A lightweight, self-contained, and serverless relational database management system. It is embedded into the end program and stores data in a single file.

To run this web app, users need to have Python 3 and Django installed on their machines. They also need to have a web browser that supports HTML5, CSS3, and JavaScript.

## Installation and Usage

To install and run this web app locally, follow these steps:

1. Clone this repository to your local machine using `git clone https://github.com/takud1/HR-Employee-WebApp.git`.
2. Navigate to the project directory using `cd HR-Employee-WebApp`.
3. Install the required Python packages using `pip install -r requirements.txt`.
4. Run the Django migrations using `python manage.py migrate`.
5. Create a superuser account using `python manage.py createsuperuser` and follow the prompts.
6. Run the Django development server using `python manage.py runserver`.
7. Open your web browser and go to `http://127.0.0.1:8000/` to access the web app.
8. Log in with your superuser credentials or create a new user account.
9. Explore the features and functionality of the web app.
