from shipment import ShipmentHistory

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.shipment_history = ShipmentHistory()

    def add_shipment(self, shipment):
        self.shipment_history.add_shipment(shipment)

    def get_shipments(self):
        return self.shipment_history.display_shipments()
