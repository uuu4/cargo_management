import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTreeWidget, QTreeWidgetItem, QMessageBox
)
from cargo_system import CargoSystem


class CargoSystemTreeGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.cargo_system = CargoSystem()
        self.setWindowTitle("Cargo Tracking System with Tree View")
        self.setGeometry(300, 100, 800, 600)

        # Ana widget ve layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Müşteri ekleme
        self.customer_layout = QHBoxLayout()
        self.customer_name_input = QLineEdit()
        self.customer_name_input.setPlaceholderText("Müşteri Adı")
        self.customer_id_input = QLineEdit()
        self.customer_id_input.setPlaceholderText("Müşteri ID")
        self.add_customer_button = QPushButton("Müşteri Ekle")
        self.add_customer_button.clicked.connect(self.add_customer)

        self.customer_layout.addWidget(QLabel("Müşteri Ekle:"))
        self.customer_layout.addWidget(self.customer_name_input)
        self.customer_layout.addWidget(self.customer_id_input)
        self.customer_layout.addWidget(self.add_customer_button)
        self.layout.addLayout(self.customer_layout)

        # Gönderi ekleme
        self.shipment_layout = QHBoxLayout()
        self.shipment_customer_id_input = QLineEdit()
        self.shipment_customer_id_input.setPlaceholderText("Müşteri ID")
        self.shipment_id_input = QLineEdit()
        self.shipment_id_input.setPlaceholderText("Gönderi ID")
        self.shipment_date_input = QLineEdit()
        self.shipment_date_input.setPlaceholderText("Tarih (YYYY-MM-DD)")
        self.shipment_delivery_input = QLineEdit()
        self.shipment_delivery_input.setPlaceholderText("Teslim Süresi (gün)")
        self.shipment_status_input = QLineEdit()
        self.shipment_status_input.setPlaceholderText("Durum")
        self.add_shipment_button = QPushButton("Gönderi Ekle")
        self.add_shipment_button.clicked.connect(self.add_shipment)

        self.shipment_layout.addWidget(QLabel("Gönderi Ekle:"))
        self.shipment_layout.addWidget(self.shipment_customer_id_input)
        self.shipment_layout.addWidget(self.shipment_id_input)
        self.shipment_layout.addWidget(self.shipment_date_input)
        self.shipment_layout.addWidget(self.shipment_delivery_input)
        self.shipment_layout.addWidget(self.shipment_status_input)
        self.shipment_layout.addWidget(self.add_shipment_button)
        self.layout.addLayout(self.shipment_layout)

        # Ağaç görünümü
        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabels(["Müşteri/Gönderi Bilgisi", "Detaylar"])
        self.layout.addWidget(QLabel("Müşteri ve Gönderi Ağaç Görünümü:"))
        self.layout.addWidget(self.tree_widget)

        # Refresh Button
        self.refresh_button = QPushButton("Yenile")
        self.refresh_button.clicked.connect(self.update_tree)
        self.layout.addWidget(self.refresh_button)

    def add_customer(self):
        name = self.customer_name_input.text()
        customer_id = self.customer_id_input.text()
        if name and customer_id:
            message = self.cargo_system.add_customer(customer_id, name)
            QMessageBox.information(self, "Bilgi", message)
            self.update_tree()
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen müşteri adı ve ID girin.")

    def add_shipment(self):
        customer_id = self.shipment_customer_id_input.text()
        shipment_id = self.shipment_id_input.text()
        date = self.shipment_date_input.text()
        delivery_time = self.shipment_delivery_input.text()
        status = self.shipment_status_input.text()

        if all([customer_id, shipment_id, date, delivery_time, status]):
            try:
                message = self.cargo_system.add_shipment(
                    customer_id, shipment_id, date, int(delivery_time), status
                )
                QMessageBox.information(self, "Bilgi", message)
                self.update_tree()
            except ValueError:
                QMessageBox.warning(self, "Uyarı", "Geçerli bir teslim süresi girin.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")

    def update_tree(self):
        self.tree_widget.clear()
        customers = self.cargo_system.get_all_customers()
        for customer in customers.values():
            customer_item = QTreeWidgetItem([f"{customer.name} (ID: {customer.customer_id})", ""])
            self.tree_widget.addTopLevelItem(customer_item)
            for shipment in customer.get_shipments():
                shipment_item = QTreeWidgetItem([
                    f"Gönderi ID: {shipment.shipment_id}",
                    f"Tarih: {shipment.date.date()}, Teslim: {shipment.delivery_time} gün, Durum: {shipment.status}"
                ])
                customer_item.addChild(shipment_item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CargoSystemTreeGUI()
    window.show()
    sys.exit(app.exec())

####