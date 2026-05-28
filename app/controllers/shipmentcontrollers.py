from flask import render_template
class ShipmentController:

    def create_shipment(self):
        return render_template('create-shipment.html')
    
    def shipment_history(self):
        return render_template('shipment-history.html')
     
    def admin_agents(self):
        return render_template('admin-agents.html')
    
    def admin_users(self):
        return render_template('admin-users.html')