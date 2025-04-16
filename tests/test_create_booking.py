import json

import pytest
from starlette.testclient import TestClient

from app.config import BOOKINGS_DB_PATH
from app.main import app
from tests.test_cases import BOOKING_REQUEST_BODY, BOOKING_REQUEST_INVALID_DATES_BODY, BOOKING_REQUEST_INVALID_CAR_BODY

client = TestClient(app)


def test_create_booking():
    # Get DB state
    with open(BOOKINGS_DB_PATH, 'r') as file:
        original_file = json.load(file)

    # POST booking
    response = client.post('/bookings', json=BOOKING_REQUEST_BODY)

    assert response.status_code == 200

    booking_id = response.json().get('id')

    # GET all bookings (would need to be tested separately)
    get_response = client.get('/bookings').json()

    # Verify new booking appears.
    assert booking_id in [booking['id'] for booking in get_response]

    # Restore DB state
    with open(BOOKINGS_DB_PATH, 'w') as file:
        json.dump(original_file, file, indent=2)


@pytest.mark.parametrize('body', [BOOKING_REQUEST_INVALID_DATES_BODY, BOOKING_REQUEST_INVALID_CAR_BODY])
def test_create_booking_negative(body):
    # Get DB state
    with open(BOOKINGS_DB_PATH, 'r') as file:
        original_file = json.load(file)

    # POST booking
    response = client.post('/bookings', json=BOOKING_REQUEST_BODY)

    assert response.status_code == 500

    booking_id = response.json().get('id')

    # GET all bookings (would need to be tested separately)
    get_response = client.get('/bookings').json()

    # Verify new booking doesn't appear.
    assert booking_id not in [booking['id'] for booking in get_response]

    # Restore DB state
    with open(BOOKINGS_DB_PATH, 'w') as file:
        json.dump(original_file, file, indent=2)
