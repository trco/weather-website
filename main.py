# imports
import webapp2

# local imports
from handlers.main_handler import MainHandler
from handlers.pin_unpin_handler import PinUnpinHandler

# url routes
app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/pin-unpin', PinUnpinHandler),
], debug=True)
