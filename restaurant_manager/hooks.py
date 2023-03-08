from . import __version__ as app_version

app_name = "restaurant_manager"
app_title = "Restaurant Manager"
app_publisher = "ByteBot Tech"
app_description = "Restaurant Manager App for ERPNext"
app_email = "opensource@bytebottech.com"
app_license = "GNU General Public License (v3)"

doc_events = {
	"Sales Order": {
        "on_submit": "restaurant_manager.restaurant_manager.methods.alert_new_order",
    }
}

sounds = [
    {"name": "new_order", "src": "/assets/restaurant_managerngr/sounds/new_order.wav", "volume": 1}
]
