import requests


class API:
    def __init__(self, hostname):
        self.hostname = hostname + "/"

    def get(self, path, **kwargs):
        return requests.get(
            self.hostname + path,
            headers={
                "User-Agent": "(WeatherBuddy, conner.bondurant@triptych.me)"
            },
            **kwargs)
