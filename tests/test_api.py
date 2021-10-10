from datetime import datetime, timedelta
from qrono.util import pprint_response
import qrono


class TestAPI:
    def test_list_item(self):
        response = qrono.Item.list()
        print(pprint_response(response))

    def test_create_item(self):
        response = qrono.Item.create(
            name="Apartment 1",
            handle="apartment1",
            booking_interval="hourly",
            default_available=True,
            description="The first of my apartments",
            metadata={
                "key": "value",
            },
            account="",
        )
        print(pprint_response(response))

    def test_list_booking(self):
        start_time = datetime.now()
        end_time = datetime.now() + timedelta(days=3)

        response = qrono.Booking.create(
            item="itm_XL5yrLR",
            start=start_time,
            end=end_time,
            description="Congrats on your first booking!",
        )
        print(pprint_response(response))
