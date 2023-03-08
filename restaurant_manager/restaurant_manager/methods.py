import frappe
import json
from frappe.utils import today

orderslist = {}

@frappe.whitelist()
def get_all_orders():

    def get_order_names():

        order_names = frappe.db.get_all("Sales Order", 
        fields=["name"], 
        filters={'status': 'To Deliver and Bill', 
        'delivery_date': ['=', today()]},
        order_by='delivery_time asc',
        pluck='name', 
        page_length=20)
        return order_names

    newordernameslist = get_order_names()

    def orders_list():
        for ordername in newordernameslist:
            order = frappe.get_doc('Sales Order', ordername)
            orderslist.update({ordername:order})

    orders_list()
    return frappe.render_template("restaurant_manager/templates/pages/kds.html", {"orders": orderslist})

@frappe.whitelist()
def alert_new_order(arg1, arg2):
    ordername = arg1
    method = arg2
    frappe.publish_realtime("new_order", {"message": ordername})

@frappe.whitelist()
def get_new_order(order):
    new_order = json.loads(order)
    order = new_order['message']
    return frappe.render_template("restaurant_manager/templates/includes/order_single.html", {"order": order})