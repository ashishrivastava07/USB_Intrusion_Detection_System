import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from database import (
    initialize_database,
    get_recent_events
)

from usb_monitor import USBMonitor


class USBIDSDashboard:

    def __init__(self, root):

        self.root = root

        self.root.title("USB Intrusion Detection System")
        self.root.geometry("900x600")

        self.root.configure(bg="#111111")

        initialize_database()

        self.title_label = tk.Label(
            root,
            text="USB Intrusion Detection System",
            font=("Arial", 24, "bold"),
            fg="#00ff00",
            bg="#111111"
        )

        self.title_label.pack(pady=20)

        self.status_label = tk.Label(
            root,
            text="USB Status: Monitoring...",
            font=("Arial", 16),
            fg="white",
            bg="#111111"
        )

        self.status_label.pack(pady=10)

        self.device_label = tk.Label(
            root,
            text="No USB device detected",
            font=("Arial", 14),
            fg="white",
            bg="#111111"
        )

        self.device_label.pack(pady=10)

        self.log_title = tk.Label(
            root,
            text="USB Event Logs",
            font=("Arial", 18, "bold"),
            fg="#00ff00",
            bg="#111111"
        )

        self.log_title.pack(pady=10)

        self.log_box = tk.Text(
            root,
            width=100,
            height=18,
            bg="#1c1c1c",
            fg="white"
        )

        self.log_box.pack(padx=20, pady=10)

        self.monitor = USBMonitor(
            callback=self.handle_usb_event
        )

        self.monitor.start()

        self.refresh_logs()

    def handle_usb_event(
        self,
        device_name,
        device_id,
        status
    ):

        if status == "AUTHORIZED":

            self.status_label.config(
                text="USB Status: Authorized Device",
                fg="#00ff00"
            )

            self.device_label.config(
                text=f"Device: {device_name}"
            )

        else:

            self.status_label.config(
                text="USB Status: UNAUTHORIZED DEVICE",
                fg="red"
            )

            self.device_label.config(
                text=f"ALERT: {device_name}"
            )

            self.root.after(
                0,
                lambda: messagebox.showwarning(
                    "USB Security Alert",
                    f"Unauthorized USB device detected!\n\n"
                    f"Device: {device_name}"
                )
            )

        self.root.after(
            0,
            self.refresh_logs
        )

    def refresh_logs(self):

        events = get_recent_events()

        self.log_box.delete(
            "1.0",
            tk.END
        )

        for event in events:

            timestamp = event[0]
            device_name = event[1]
            device_id = event[2]
            status = event[3]
            event_type = event[4]

            line = (
                f"{timestamp} | "
                f"{device_name} | "
                f"{status} | "
                f"{event_type}\n"
            )

            self.log_box.insert(
                tk.END,
                line
            )

        self.root.after(
            3000,
            self.refresh_logs
        )


if __name__ == "__main__":

    root = tk.Tk()

    app = USBIDSDashboard(root)

    root.mainloop()
