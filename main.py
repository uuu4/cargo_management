import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QHBoxLayout, QMessageBox
)
from cargo_system import CargoSystem


class CargoSystemGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.cargo_system = CargoSystem()
        self.setWindowTitle("Cargo Tracking System")
        self.setGeometry(300, 100, 600, 500)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layouts
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Add Customer Section
        self.add_customer_layout = QHBoxLayout()
        self.layout.addLayout(self.add_customer_layout)

        self.customer_name_input = QLineEdit()
        self.customer_name_input.setPlaceholderText("Enter Customer Name")
        self.customer_id_input = QLineEdit()
        self.customer_id_input.setPlaceholderText("Enter Customer ID")
        self.add_customer_button = QPushButton("Add Customer")
        self.add_customer_button.clicked.connect(self.add_customer)

        self.add_customer_layout.addWidget(QLabel("Add Customer: "))
        self.add_customer_layout.addWidget(self.customer_name_input)
        self.add_customer_layout.addWidget(self.customer_id_input)
        self.add_customer_layout.addWidget(self.add_customer_button)

        # Add Shipment Section
        self.add_shipment_layout = QHBoxLayout()
        self.layout.addLayout(self.add_shipment_layout)

        self.shipment_customer_id_input = QLineEdit()
        self.shipment_customer_id_input.setPlaceholderText("Customer ID")
        self.shipment_id_input = QLineEdit()
        self.shipment_id_input.setPlaceholderText("Shipment ID")
        self.shipment_date_input = QLineEdit()
        self.shipment_date_input.setPlaceholderText("Date (YYYY-MM-DD)")
        self.shipment_delivery_input = QLineEdit()
        self.shipment_delivery_input.setPlaceholderText("Delivery Time (days)")
        self.shipment_status_input = QLineEdit()
        self.shipment_status_input.setPlaceholderText("Status")
        self.add_shipment_button = QPushButton("Add Shipment")
        self.add_shipment_button.clicked.connect(self.add_shipment)

        self.add_shipment_layout.addWidget(QLabel("Add Shipment: "))
        self.add_shipment_layout.addWidget(self.shipment_customer_id_input)
        self.add_shipment_layout.addWidget(self.shipment_id_input)
        self.add_shipment_layout.addWidget(self.shipment_date_input)
        self.add_shipment_layout.addWidget(self.shipment_delivery_input)
        self.add_shipment_layout.addWidget(self.shipment_status_input)
        self.add_shipment_layout.addWidget(self.add_shipment_button)

        # Display Shipments Section
        self.shipments_display = QTextEdit()
        self.shipments_display.setReadOnly(True)
        self.layout.addWidget(QLabel("All Shipments:"))
        self.layout.addWidget(self.shipments_display)

        self.display_button = QPushButton("Refresh Shipments")
        self.display_button.clicked.connect(self.display_shipments)
        self.layout.addWidget(self.display_button)

    def add_customer(self):
        name = self.customer_name_input.text()
        customer_id = self.customer_id_input.text()
        if name and customer_id:
            message = self.cargo_system.add_customer(customer_id, name)
            QMessageBox.information(self, "Info", message)
        else:
            QMessageBox.warning(self, "Warning", "Enter both Customer Name and ID")

    def add_shipment(self):
        customer_id = self.shipment_customer_id_input.text()
        shipment_id = self.shipment_id_input.text()
        date = self.shipment_date_input.text()
        delivery_time = self.shipment_delivery_input.text()
        status = self.shipment_status_input.text()

        if all([customer_id, shipment_id, date, delivery_time, status]):
            try:
                message = self.cargo_system.add_shipment(customer_id, shipment_id, date, int(delivery_time), status)
                QMessageBox.information(self, "Info", message)
            except ValueError:
                QMessageBox.warning(self, "Warning", "Invalid delivery time format.")
        else:
            QMessageBox.warning(self, "Warning", "Please fill all fields.")

    def display_shipments(self):
        self.shipments_display.clear()
        for customer in self.cargo_system.get_all_customers().values():
            self.shipments_display.append(f"Customer: {customer.name} (ID: {customer.customer_id})")
            for shipment in customer.get_shipments():
                self.shipments_display.append(str(shipment))
            self.shipments_display.append("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CargoSystemGUI()
    window.show()
    sys.exit(app.exec())
