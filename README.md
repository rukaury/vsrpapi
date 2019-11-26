# VSRP REST API

API used for the virtual study room application. The API should allow users to register, login, logout and list or add necessary information regarding rooms, questions and answers.


## Usage
- [Getting Started](#getting-started)
- [API Documentation](#api-documentation)
    - [Users](#users)
    - [Events](#events)
    - [Tickets](#tickets)
    - [Guests](#guests)
- [Running the tests](#running-the-tests)
- [Deployment](#deployment)
- [Built with](#built-with)
- [Contributing](#contributing)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The API is built using a small python-based framework called Flask, therefore will require python to be installed.

### Installing

Once python is installed, a virtual environment can be used for development. 

These steps can be used to install a virtual environment: 

1. Install a virtual environment (Mac OS X): `sudo easy_install virtualenv` 

2. Activate the environment by running: `venv/Scripts/activate`

Creating a virtual environment for each application ensures that applications have access to only the packages that they use.

## API Documentation

### Users

#### User Registration [/auth/register]

##### Register a user [POST]

You can create a user by sending a json request with an email and password. The
password must be at least four(4) characters.

+ Request (application/json)

        {
            "email": "example@gmail.com",
            "password": "123456"
        }

+ Response 201 (application/json)

        {
            "auth_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MDM0ODQ5OTYsImlhdCI6MTUwMzM5ODU4Niwic3ViIjo1fQ.GC6IEOohdo_xrz9__UeugIlir0qtJdKbEzBtLgqjt5A",
            "message": "Successfully registered",
            "status": "success"
        }

+ Response 400 (application/json)

        {
            "message": "Missing or wrong email format or password length",
            "status": "failed"
        }

+ Response 400 (application/json)

        {
            "message": "Failed, User already exists, Please sign In",
            "status": "failed"
        }

+ Response 400 (application/json)

        {
          "message": "Content-type must be json",
          "status": "failed"
        }

#### Login [/auth/login]

##### Login a user [POST]

You can login a user by sending their email and password. Please take note
of the auth token for you will need it for all user requests.

+ Request (application/json)

        {
            "email": "example@gmail.com",
            "password": "123456"
        }

+ Response 201 (application/json)

        {
            "auth_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MDM0ODQ5OTYsImlhdCI6MTUwMzM5ODU4Niwic3ViIjo1fQ.GC6IEOohdo_xrz9__UeugIlir0qtJdKbEzBtLgqjt5A",
            "message": "Successfully registered",
            "status": "success"
        }

+ Response 400 (application/json)

        {
          "message": "Content-type must be json",
          "status": "failed"
        }

+ Response 401 (application/json)

        {
          "message": "Missing or wrong email format or password is less than four characters",
          "status": "failed"
        }

+ Response 401 (application/json)

        {
          "message": "User does not exist or password is incorrect",
          "status": "failed"
        }

#### Logout [/auth/logout]

##### Log out a user [POST]

You can log out a user by sending a request with their email and address. The
auth token will then be invalidated (blacklisted).

+ Request (application/json)

    + Headers

            Authorization: Bearer JWT Token

+ Response 200 (application/json)

        {
            "message": "Successfully logged out",
            "status": "success"
        }

+ Response 403 (application/json)

        {
          "message": "Provide a valid auth token",
          "status": "failed"
        }

+ Response 403 (application/json)

        {
          "message": "Provide an authorization header",
          "status": "failed"
        }

+ Response 401 (application/json)

        {
          "message": "Signature expired, Please sign in again",
          "status": "failed"
        }

+ Response 401 (application/json)

        {
          "message": "Invalid token. Please sign in again",
          "status": "failed"
        }

### Rooms

API documentation will be available soon. However, the endpoints were implemented.

### Questions

API documentation will be available soon. However, the endpoints were implemented.

### Answers

API documentation will be available soon. However, the endpoints were implemented.

## Running the tests

Before running the application tests, update your env variables.

    export  APP_SETTINGS=app.config.TestingConfig
    export DATABASE_URL_TEST=<postgres database url>


### Tests without coverage

Run this command from terminal

    python manage.py test

### Tests with coverage

Run this command from terminal

    nosetests --with-coverage --cover-package=app

## Deployment

Not ready for deployment yet.

## Built with

Frameworks used are listed in the *requirements.txt* file

## Contributing

Decisions has not been made yet on who can contribute to this repository.

## Versioning

Thinking of using semantic versioning, but decision has not been made yet. 

## Authors

* **Aury Rukazana** - *Initial work*

## License

This project is licensed under the MIT License.
