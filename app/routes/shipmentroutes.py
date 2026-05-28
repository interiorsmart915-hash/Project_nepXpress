from flask import Blueprint
from app.controllers.shipmentcontrollers import ShipmentController
class Shipmentroutes:
    def __init__(self):
        self.bp=Blueprint("shipment",__name__)
        self.controller=ShipmentController()

    def shipment(self):
        self.bp.route("/create-shipment", methods=["GET", "POST"])(
            self.controller.create_shipment
        )
        self.bp.route("/shipment-history", methods=["GET", "POST"])(
            self.controller.shipment_history
        )
        self.bp.route("/admin-agents", methods=["GET", "POST"])(
            self.controller.admin_agents
        )
        self.bp.route("/admin-users", methods=["GET", "POST"])(
            self.controller.admin_users
        )
        return self.bp
    


