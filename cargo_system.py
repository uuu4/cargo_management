from shipment import Shipment
from customer import Customer

class CargoSystem:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer_id, name):
        if customer_id not in self.customers:
            self.customers[customer_id] = Customer(customer_id, name)
            return f"Customer {name} added successfully."
        else:
            return "Customer ID already exists."

    def add_shipment(self, customer_id, shipment_id, date, delivery_time, status):
        if customer_id in self.customers:
            shipment = Shipment(shipment_id, date, delivery_time, status)
            self.customers[customer_id].add_shipment(shipment)
            return "Shipment added successfully."
        else:
            return "Customer ID not found."

    def get_all_customers(self):
        return self.customers
