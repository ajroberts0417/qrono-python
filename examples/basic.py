import qrono

bookings = qrono.Booking.list()

print(bookings)

qrono.Booking.create(
    item="itm_XL5yrLR",
    start=start_time,
    end=end_time,
    description="Congrats on your first booking!",
)
