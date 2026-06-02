from app.models.BaseModel import BaseModel
from app.models.database import Database, execute_query
import random


class Shipment(BaseModel):
    """
    Teammate's Shipment class — kept exactly as-is.
    Used by the customer-facing create-shipment page.
    """
    table = "shipments"

    def __init__(self):
        self.id = None

    @staticmethod
    def generate_tracking_id():
        """Generate a unique tracking ID in format NXP-NNNN-NNNN."""
        db = Database()
        while True:
            tid = f"NXP-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
            existing = db.fetch_one(
                "SELECT id FROM shipments WHERE tracking_id=%s", (tid,)
            )
            if not existing:
                db.close()
                return tid

    def create(self, data):
        """Insert a new shipment. `data` is a dict of column->value."""
        db = Database()
        query = (
            "INSERT INTO shipments "
            "(tracking_id, customer_id, destination, status, amount, notes) "
            "VALUES (%s,%s,%s,%s,%s,%s)"
        )
        db.execute(query, (
            data["tracking_id"], data["user_id"],
            data["sender_name"], data["sender_phone"], data["sender_address"], data["sender_city"], data["sender_district"],
            data["receiver_name"], data["receiver_phone"], data["receiver_address"], data["receiver_city"], data["receiver_district"],
            data["package_type"], data["weight"], data["estimated_value"],
            data["length_cm"], data["width_cm"], data["height_cm"], data["instructions"],
            data["delivery_type"], data["payment_method"], data["status"],
        ))
        db.close()

    def find_by_user(self, user_id):
        """Get all shipments for a user, newest first."""
        db = Database()
        results = db.fetch_all(
            "SELECT * FROM shipments WHERE customer_id=%s ORDER BY created_at DESC",
            (user_id,)
        )
        db.close()
        return results