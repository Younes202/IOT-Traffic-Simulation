import subprocess


class ConnectServer:
    def __init__(self):
        pass

    def start_cse(self):
        acme_command = ["gnome-terminal", "--", "bash", "-c", "cd tools/ACME && python3 -m acme --headless"]
        subprocess.Popen(acme_command)

    def start_introduction(self):
        introduction_command = ["gnome-terminal", "--", "bash", "-c", "cd src && python3 init.py introduction"]
        subprocess.Popen(introduction_command)

    def start_notification_server(self):
        notification_server_command = ["gnome-terminal", "--", "bash", "-c", "cd tools/NotificationServer && python3 NotificationServer.py"]
        subprocess.Popen(notification_server_command)
