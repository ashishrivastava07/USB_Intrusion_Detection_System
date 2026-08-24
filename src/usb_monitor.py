import time
import threading
import wmi

from database import (
    initialize_database,
    is_authorized,
    log_event
)


class USBMonitor:

    def __init__(self, callback=None):
        self.callback = callback
        self.running = False
        self.known_devices = set()

    def get_current_devices(self):
        computer = wmi.WMI()

        devices = {}

        for disk in computer.Win32_DiskDrive(InterfaceType="USB"):
            device_id = disk.PNPDeviceID or "Unknown"

            devices[device_id] = {
                "name": disk.Caption or "Unknown USB Device",
                "id": device_id
            }

        return devices

    def process_device(self, device):
        device_id = device["id"]
        device_name = device["name"]

        authorized = is_authorized(device_id)

        if authorized:
            status = "AUTHORIZED"
            event_type = "USB_CONNECTED"

        else:
            status = "UNAUTHORIZED"
            event_type = "SECURITY_ALERT"

        log_event(
            device_name,
            device_id,
            status,
            event_type
        )

        if self.callback:
            self.callback(
                device_name,
                device_id,
                status
            )

    def monitor(self):

        initialize_database()

        self.running = True

        while self.running:

            try:
                current_devices = self.get_current_devices()

                current_ids = set(current_devices.keys())

                new_devices = current_ids - self.known_devices

                for device_id in new_devices:

                    device = current_devices[device_id]

                    self.process_device(device)

                self.known_devices = current_ids

                time.sleep(2)

            except Exception as error:

                print(f"Monitoring error: {error}")

                time.sleep(3)

    def start(self):

        monitor_thread = threading.Thread(
            target=self.monitor,
            daemon=True
        )

        monitor_thread.start()

    def stop(self):

        self.running = False
