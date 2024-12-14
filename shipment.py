import heapq
from datetime import datetime

class Shipment:
    def __init__(self, shipment_id, date, delivery_time, status):
        self.shipment_id = shipment_id
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.delivery_time = delivery_time
        self.status = status

    def __lt__(self, other):
        return self.delivery_time < other.delivery_time

    def __str__(self):
        return f"Shipment ID: {self.shipment_id}, Date: {self.date.date()}, Delivery Time: {self.delivery_time} days, Status: {self.status}"

class ShipmentHistory:
    def __init__(self):
        self.history = []

    def add_shipment(self, shipment):
        heapq.heappush(self.history, shipment)

    def display_shipments(self):
        return sorted(self.history, key=lambda x: x.date)
