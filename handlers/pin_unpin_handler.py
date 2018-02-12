from handlers.base_handler import BaseHandler
import logging


class PinUnpinHandler(BaseHandler):
    def post(self):
        try:
            pinned_cities = self.request.cookies.get("cities")
            pinned_cities_list = pinned_cities.split(",")

            pin_unpin_city = self.request.get("city")

            action = self.request.get("action")

            if action == "pin":
                pinned_cities_list.append(pin_unpin_city)
            else:
                pinned_cities_list.remove(pin_unpin_city)

            update_cookie = ",".join(pinned_cities_list)

            self.response.set_cookie("cities", update_cookie)
        except:
            first_pinned_city = self.request.get("city")
            self.response.set_cookie("cities", first_pinned_city)

        return self.redirect("/")
