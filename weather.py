import json
import requests
import api
import time

class Weather:
    def __init__(self, **kwargs):
        self.api = api.API("https://api.weather.gov/")
        self.coordinate = kwargs["coordinates"]
        station_data = json.loads(self.api.get("/points/{}".format(self.coordinate)).text)
        self.gridId = station_data["properties"]["gridId"]
        self.gridX = station_data["properties"]["gridX"]
        self.gridY = station_data["properties"]["gridY"]
        self.cacheTime = 0
        if "cacheTTL" in kwargs:
            self.cacheTTL = float(kwargs["cacheTTL"]) * 60
        else:
            self.cacheTTL = 1800
        self.cache = {}

    def _validate_cache(self):
        curtime = time.time()
        if self.cacheTime - curtime < 0:
            self.cache = self.api.get("/gridpoints/{}/{},{}/forecast".format(self.gridId, self.gridX, self.gridY)).json()
            self.cacheTime = curtime + self.cacheTTL

    def get_forecast_raw(self):
        self._validate_cache()
        return self.cache["properties"]

    def get_weather_current(self):
        self._validate_cache()
        for forecast in self.cache["properties"]["periods"]:
            start = time.strptime(forecast["startTime"],"%Y-%m-%dT%H:%M:%S%z")
            end = time.strptime(forecast["endTime"],"%Y-%m-%dT%H:%M:%S%z")
            if start < time.gmtime() < end:
                return forecast

        return self.cache["properties"]["weather"]["values"][0]["value"][0]
