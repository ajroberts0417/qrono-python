# Qrono Python Library

The Qrono Python library allows you to connect to the Qrono Bookings API.

## Documentation

[Python API docs](https://docs.qrono.dev)

## Installation

```sh
pip install qrono
```

### Requirements

- Python 3 currently is required.

## Usage

Get your Qrono API key from your account dashboard.

Set `qrono.api_key` to its value:

```python
import qrono
qrono.api_key = "<YOUR_API_KEY>"

# list bookings
bookings = qrono.Bookings.list()

# print the first booking's description
print(bookings.results[0].description)

# retrieve specific Booking
booking = qrono.Booking.retrieve("booking123235")

# print that customer's email
print(booking.email)
```
