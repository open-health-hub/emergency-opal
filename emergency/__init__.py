"""
emergency - Our OPAL Application
"""
from opal.core import application

class Application(application.OpalApplication):
    flow_module   = 'emergency.flow'
    javascripts   = [
        'js/emergency/routes.js',
        'js/opal/controllers/discharge.js',
        # Uncomment this if you want to implement custom dynamic flows.
        # 'js/emergency/flow.js',
    ]

    menuitems = [
        dict(
            href='pathway/#/booking', display='Book In', icon='fa fa-plus',
            activepattern = 'pathway/#/booking'
            )
    ]