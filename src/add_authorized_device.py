from database import initialize_database, add_authorized_device
from usb_detector import get_usb_devices


initialize_database()

devices = get_usb_devices()

if not devices:

    print("No USB storage device detected.")

else:

    for device in devices:

        print("\nUSB Device Found")
        print("Name:", device["name"])
        print("ID:", device["id"])

        choice = input(
            "Authorize this device? (y/n): "
        )

        if choice.lower() == "y":

            add_authorized_device(
                device["id"],
                device["name"]
            )

            print("Device authorized successfully.")
