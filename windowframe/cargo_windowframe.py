import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QDialog, QLabel, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QWidget

# Modülleri import ediyoruz
from customer_management import CustomerManagement, Cargo
from cargo_routing import DeliveryTree, Node
from cargo_prioritization import PriorityQueue


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kargo Yönetim Sistemi")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(layout)

        # Yeni müşteri ekleme
        add_customer_btn = QPushButton("Yeni Müşteri Ekle", self)
        add_customer_btn.clicked.connect(self.open_add_customer_dialog)
        layout.addWidget(add_customer_btn)

        # Kargo ekleme
        add_cargo_btn = QPushButton("Kargo Ekle", self)
        add_cargo_btn.clicked.connect(self.open_add_cargo_dialog)
        layout.addWidget(add_cargo_btn)

        # Kargo sorgulama
        search_cargo_btn = QPushButton("Kargo Durumu Sorgula", self)
        search_cargo_btn.clicked.connect(self.open_search_cargo_dialog)
        layout.addWidget(search_cargo_btn)

        # Gönderim geçmişi
        view_history_btn = QPushButton("Gönderim Geçmişini Görüntüle", self)
        view_history_btn.clicked.connect(self.open_view_history_dialog)
        layout.addWidget(view_history_btn)

        # Tüm kargoları listeleme
        list_all_cargos_btn = QPushButton("Tüm Kargoları Listele", self)
        list_all_cargos_btn.clicked.connect(self.open_list_all_cargos_dialog)
        layout.addWidget(list_all_cargos_btn)

        # Teslimat rotalarını gösterme
        show_routes_btn = QPushButton("Teslimat Rotalarını Göster", self)
        show_routes_btn.clicked.connect(self.open_show_routes_dialog)
        layout.addWidget(show_routes_btn)

        # Yönetim sınıfları
        self.customer_management = CustomerManagement()
        self.delivery_tree = DeliveryTree(Node("Merkez", 0))

    def open_add_customer_dialog(self):
        dialog = AddCustomerDialog(self.customer_management)
        dialog.exec()

    def open_add_cargo_dialog(self):
        dialog = AddCargoDialog(self.customer_management)
        dialog.exec()

    def open_search_cargo_dialog(self):
        dialog = SearchCargoDialog(self.customer_management)
        dialog.exec()

    def open_view_history_dialog(self):
        dialog = ViewHistoryDialog(self.customer_management)
        dialog.exec()

    def open_list_all_cargos_dialog(self):
        dialog = ListAllCargosDialog(self.customer_management)
        dialog.exec()

    def open_show_routes_dialog(self):
        dialog = ShowRoutesDialog(self.delivery_tree)
        dialog.exec()


# Dialog sınıflarını tanımlayalım

class AddCustomerDialog(QDialog):
    def __init__(self, customer_management):
        super().__init__()
        self.setWindowTitle("Yeni Müşteri Ekle")
        self.setGeometry(150, 150, 400, 300)
        self.customer_management = customer_management

        layout = QVBoxLayout()

        self.id_input = QLineEdit(self)
        self.id_input.setPlaceholderText("Müşteri ID")
        layout.addWidget(self.id_input)

        self.first_name_input = QLineEdit(self)
        self.first_name_input.setPlaceholderText("İsim")
        layout.addWidget(self.first_name_input)

        self.last_name_input = QLineEdit(self)
        self.last_name_input.setPlaceholderText("Soyisim")
        layout.addWidget(self.last_name_input)

        add_button = QPushButton("Müşteri Ekle")
        add_button.clicked.connect(self.add_customer)
        layout.addWidget(add_button)

        self.setLayout(layout)

    def add_customer(self):
        customer_id = self.id_input.text()
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()

        if customer_id and first_name and last_name:
            self.customer_management.add_customer(customer_id, first_name, last_name)
            self.accept()


class AddCargoDialog(QDialog):
    def __init__(self, customer_management):
        super().__init__()
        self.setWindowTitle("Kargo Ekle")
        self.setGeometry(150, 150, 400, 400)
        self.customer_management = customer_management

        layout = QVBoxLayout()

        self.customer_id_input = QLineEdit(self)
        self.customer_id_input.setPlaceholderText("Müşteri ID")
        layout.addWidget(self.customer_id_input)

        self.cargo_id_input = QLineEdit(self)
        self.cargo_id_input.setPlaceholderText("Kargo ID")
        layout.addWidget(self.cargo_id_input)

        self.send_date_input = QLineEdit(self)
        self.send_date_input.setPlaceholderText("Gönderim Tarihi (YYYY-MM-DD)")
        layout.addWidget(self.send_date_input)

        self.delivery_time_input = QLineEdit(self)
        self.delivery_time_input.setPlaceholderText("Teslimat Süresi (gün)")
        layout.addWidget(self.delivery_time_input)

        self.status_input = QLineEdit(self)
        self.status_input.setPlaceholderText("Durum (Teslim Edildi/Teslim Edilmedi)")
        layout.addWidget(self.status_input)

        add_button = QPushButton("Kargo Ekle")
        add_button.clicked.connect(self.add_cargo)
        layout.addWidget(add_button)

        self.setLayout(layout)

    def add_cargo(self):
        customer_id = self.customer_id_input.text()
        cargo_id = self.cargo_id_input.text()
        send_date = self.send_date_input.text()
        delivery_time = self.delivery_time_input.text()
        status = self.status_input.text()

        customer = self.customer_management.get_customer(customer_id)
        if customer:
            cargo = Cargo(cargo_id, int(delivery_time), status)
            customer.add_cargo(cargo)
            self.accept()


class SearchCargoDialog(QDialog):
    def __init__(self, customer_management):
        super().__init__()
        self.setWindowTitle("Kargo Sorgula")
        self.setGeometry(150, 150, 400, 300)
        self.customer_management = customer_management

        layout = QVBoxLayout()

        self.customer_id_input = QLineEdit(self)
        self.customer_id_input.setPlaceholderText("Müşteri ID")
        layout.addWidget(self.customer_id_input)

        self.cargo_id_input = QLineEdit(self)
        self.cargo_id_input.setPlaceholderText("Kargo ID")
        layout.addWidget(self.cargo_id_input)

        search_button = QPushButton("Ara")
        search_button.clicked.connect(self.search_cargo)
        layout.addWidget(search_button)

        self.result_label = QLabel(self)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def search_cargo(self):
        customer_id = self.customer_id_input.text()
        cargo_id = self.cargo_id_input.text()

        customer = self.customer_management.get_customer(customer_id)
        if customer:
            cargo = customer.search_delivered_cargo(cargo_id)
            if cargo:
                self.result_label.setText(str(cargo))
            else:
                self.result_label.setText("Kargo bulunamadı.")
        else:
            self.result_label.setText("Müşteri bulunamadı.")


class ViewHistoryDialog(QDialog):
    def __init__(self, customer_management):
        super().__init__()
        self.setWindowTitle("Gönderim Geçmişi")
        self.setGeometry(150, 150, 400, 300)
        self.customer_management = customer_management

        layout = QVBoxLayout()

        self.customer_id_input = QLineEdit(self)
        self.customer_id_input.setPlaceholderText("Müşteri ID")
        layout.addWidget(self.customer_id_input)

        view_button = QPushButton("Geçmişi Görüntüle")
        view_button.clicked.connect(self.view_history)
        layout.addWidget(view_button)

        self.result_label = QLabel(self)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def view_history(self):
        customer_id = self.customer_id_input.text()
        customer = self.customer_management.get_customer(customer_id)
        if customer:
            customer.display_cargo_history()
        else:
            self.result_label.setText("Müşteri bulunamadı.")


class ListAllCargosDialog(QDialog):
    def __init__(self, customer_management):
        super().__init__()
        self.setWindowTitle("Tüm Kargoları Listele")
        self.setGeometry(150, 150, 600, 400)
        self.customer_management = customer_management

        layout = QVBoxLayout()

        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Kargo ID", "Teslimat Süresi", "Durum", "Müşteri ID"])
        layout.addWidget(self.table)

        self.populate_table()

        self.setLayout(layout)

    def populate_table(self):
        self.table.setRowCount(0)
        for customer in self.customer_management.customers.values():
            for cargo in customer.cargo_history:
                row_position = self.table.rowCount()
                self.table.insertRow(row_position)
                self.table.setItem(row_position, 0, QTableWidgetItem(cargo.cargo_id))
                self.table.setItem(row_position, 1, QTableWidgetItem(str(cargo.delivery_time)))
                self.table.setItem(row_position, 2, QTableWidgetItem(cargo.delivery_status))
                self.table.setItem(row_position, 3, QTableWidgetItem(customer.customer_id))


class ShowRoutesDialog(QDialog):
    def __init__(self, delivery_tree):
        super().__init__()
        self.setWindowTitle("Teslimat Rotaları")
        self.setGeometry(150, 150, 600, 400)
        self.delivery_tree = delivery_tree

        layout = QVBoxLayout()

        self.tree_widget = QTreeWidget(self)
        self.tree_widget.setHeaderLabels(["Şehir Adı", "Şehir ID"])
        layout.addWidget(self.tree_widget)

        self.display_routes()

        self.setLayout(layout)

    def display_routes(self):
        def add_nodes_to_tree(node, tree_item):
            for child in node.children:
                child_item = QTreeWidgetItem([child.city_name, str(child.city_id)])
                tree_item.addChild(child_item)
                add_nodes_to_tree(child, child_item)

        root_item = QTreeWidgetItem([self.delivery_tree.root.city_name, str(self.delivery_tree.root.city_id)])
        self.tree_widget.addTopLevelItem(root_item)
        add_nodes_to_tree(self.delivery_tree.root, root_item)


# Uygulamayı başlatmak için aşağıdaki kodu ekliyoruz:
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()  # Ana pencereyi başlatıyoruz
    window.show()  # Ana pencereyi gösteriyoruz
    sys.exit(app.exec())  # Uygulamanın çalışmasını başlatıyoruz
