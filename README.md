# portfolio

Behold My Awesome Production-ready Project!

## Portfolio Web Application
This is a portfolio web application created with Django as a framework. The purpose of this application is to allow users to register and create profiles that include further details about the user, such as a home address, phone number, and location where they live.

# Requirements
- Django: 3.2.8
- Python: > 3.10
- PostgreSQL
- Postgis Library (for PostgreSQL)
- GIS (for Geocoding)

## Features
The application includes the following features:

### User Profile:
- Users can create their own profiles with their personal information, including location (point geometry).
- User profile page and a page to edit the user’s profile.
- Users can log in from the default Django admin page.
- Users can only see their own profile page, but not others.
- Map:
- A full-screen map that shows all registered users’ locations.
When clicking on the user icon, it displays the user’s profile in a popup.
- Django Admin Page:
- Super user can access the Django admin page for all models.

### Bonus Features:
- Test cases.
- CI integration with the code repo to automatically test new code added via a PR.
- Sign up and sign in page using the auditlog library for non-super users able to log in.
- Log the user login/logout activity by showing who and when on the admin page using the auditlog library.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Installation

- Clone the repository from Github.
- Create a virtual environment and activate it.
- Install the required packages using the command pip install -r requirements/local.txt.
- Create a PostgreSQL database and update the DATABASES configuration in settings.py.
- Run the command python manage.py migrate to migrate the database.
- Create a super user using the command python manage.py createsuperuser.
- Run the command python manage.py runserver to start the development server.
Usage
- Log in to the Django admin page using the super user credentials.
- Create new users and add their profile information.
- Navigate to the map page to see all registered users' locations and their profile popups when clicked.
- Navigate to your own profile page to edit your personal information.

- The application is integrated with CI/CD pipeline with Github actions.
- Any new code added via a PR will be automatically tested and display an indicator as to whether the tests have passed or not.

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Main Routes
- home
- account_login
- account_signup
- users:detail
- map

### Type checks

Running type checks with mypy:

    $ mypy portfolio

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.
