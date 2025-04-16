Sample application for a car rental service API.

This API has two main objects with its specific endpoints (docs can be checked at localhost/docs when running the API).

- Cars:
    - /cars/ GET all cars.
    - /cars/available/{date} GET only available cars for the given date.

- Bookings:
    - /bookings/ GET all bookings.
    - /bookings/ POST create a new booking.

The endpoints not specified in the instructions for this task have been developed to help test and complete basic
functionalities. As to design principles the project is divided in:

- app: files to hold the API
    - crud: operations to read/write to the database (JSON file in this case).
    - data: sample data to perform basic requests, but modifiable through /bookings/ POST request.
    - models: classes/models to define Cars and Booking objects.
    - routes: definition of the logic and the API endpoints.
    - utils: other functions and loggers used in the project.

- tests:
    - test_create_booking: file with positive and negative test cases for the POST /bookings/ endpoint. The tests are
      very simple and more would be needed but are not in scope for this project.
      To run them, it is enough to have pytest installed and run the tests in your editor or with the 'pytest' command.

- Dockerfile and requirements.txt:
  They are needed to build the Docker image to run the API. In order to do so, run the following commands on the
  project root:
    - docker build -t car-rental-api .
    - docker run -d --name car-rental-api-container -p 80:80 car-rental-api

The API does not support many logical functionalities such as creating a new car, deleting a booking, managing clients,
etc. Also, only the basic checks have been made on the /bookings/ endpoint (invalid car_id or already booked car). Other
logic such as pricing or using real ids have not been taken into account for simplicity purposes.

The tests should not be reliant on the real database but rather have their own test data, but this would overcomplicate
things and this was not the purpose of the project.

One of the biggest challenges faced, although common in Python API projects, is elegantly switching between snake_case
for Python models and camelCase as is standard for JSON files.