import json
from google.appengine.api import urlfetch

from handlers.base_handler import BaseHandler


class MainHandler(BaseHandler):
    def get(self):
        url = "http://api.openweathermap.org/data/2.5/group?id=3196359,3195506,3202781,792680,6058560,2950159,2988507,524901,3054643,264371&units=metric&appid=9dfaa34265bbac3dca2eecb1f9222db9"
        data = urlfetch.fetch(url).content

        json_data = json.loads(data)

        try:
            pinned_cities = self.request.cookies.get("cities")
            pinned_cities_list = pinned_cities.split(",")
        except:
            pinned_cities = []

        context = {
            "json_data": json_data,
            "pinned_cities": pinned_cities
        }
        return self.render_template("home.html", context)
