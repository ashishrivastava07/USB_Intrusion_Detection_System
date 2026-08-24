import wmi


def get_usb_devices():
    """
    Returns currently connected USB storage devices.
    """

    computer = wmi.WMI()

    devices = []

    for disk in computer.Win32_DiskDrive(InterfaceType="USB"):

        device_name = disk.Caption or "Unknown USB Device"
        device_id = disk.PNPDeviceID or "Unknown"

        devices.append({
            "name": device_name,
            "id": device_id
        })

    return devices
