import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QDialog, QLineEdit, QLabel, QTableWidget, QTableWidgetItem, QWidget, QTreeWidget, QTreeWidgetItem
from PySide6.QtWidgets import QListWidget,QComboBox
from PySide6.QtGui import QFont,QPixmap, QPainter
from PySide6.QtCore import Qt
# Backend modüllerini import ediyoruz
from customer_management import CustomerManagement, Cargo
from cargo_prioritization import PriorityQueue



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kargo Yönetim Sistemi")
        self.setGeometry(100, 120, 900, 650)

        # Backend sınıfları
        self.customer_management = CustomerManagement()
        self.priority_queue = PriorityQueue()

        # Ana layout
        layout = QVBoxLayout()
        # arka plan resmi
        image_path = os.path.join(os.path.dirname(__file__), "", "kargo.png")
        pixmap = QPixmap(image_path)
        print("Resim yolu:", image_path)
        self.background_label = QLabel(self)
        self.background_label.setPixmap(pixmap)
        self.background_label.setGeometry(0, 0, self.width(), self.height())  # Resmin boyutlarını pencereye göre ayarla
        self.background_label.setAlignment(Qt.AlignCenter)
        self.background_label.setScaledContents(True)
#C:\Users\Emir Başak Sunar\Documents\GitHub\cargo_management\windowframe\kargo.png
        # Ana Widget (tüm içerik)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(layout)

        def resizeEvent(self, event):
            # Pencere boyutları değiştiğinde resmin boyutlarını ayarlıyoruz
            self.background_label.setGeometry(0, 0, self.width(), self.height())
            super().resizeEvent(event)

        # Başlık
        title_label = QLabel("Kargo Yönetim Sistemi")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 28, QFont.Bold))
        title_label.setStyleSheet("color: #aaaaaa; padding: 10px; background-color: #transparent;")
        layout.addWidget(title_label)

        # Butonlar
        add_customer_btn = QPushButton("Yeni Müşteri Ekle", self)
        add_customer_btn.clicked.connect(self.open_add_customer_dialog)
        add_customer_btn.setFont(QFont("Arial", 14))
        add_customer_btn.setStyleSheet("""
                        QPushButton {
                            background-color: #gray;
                            color: #FFFFFF;
                            border: 2px solid #9455f4;
                            border-radius: 10px;
                            padding: 10px;
                            margin: 8px;
                        }
                        QPushButton:hover {
                           background-color: #9455f4;
                        }
                        QPushButton:pressed {
                            background-color: #444444;
                        }
                    """)
        layout.addWidget(add_customer_btn)

        add_cargo_btn = QPushButton("Kargo Ekle", self)
        add_cargo_btn.clicked.connect(self.open_add_cargo_dialog)
        add_cargo_btn.setFont(QFont("Arial", 14))
        add_cargo_btn.setStyleSheet("""
                                QPushButton {
                                    background-color: #gray;
                                                            color: #FFFFFF;
                                                            border: 2px solid #9455f4;
                                                            border-radius: 10px;
                                                            padding: 10px;
                                                            margin: 8px;
                                }
                                QPushButton:hover {
                                    background-color: #9455f4;
                                }
                                QPushButton:pressed {
                                    background-color: #444444;
                                }
                            """)
        layout.addWidget(add_cargo_btn)

        search_cargo_btn = QPushButton("Kargo Durumu Sorgula", self)
        search_cargo_btn.clicked.connect(self.open_search_cargo_dialog)
        search_cargo_btn.setFont(QFont("Arial", 14))
        search_cargo_btn.setStyleSheet("""
                                        QPushButton {
                                            background-color: #gray;
                                                            color: #FFFFFF;
                                                            border: 2px solid #9455f4;
                                                            border-radius: 10px;
                                                            padding: 10px;
                                                            margin: 8px;
                                        }
                                        QPushButton:hover {
                                             background-color: #9455f4;
                                        }
                                        QPushButton:pressed {
                                            background-color: #444444;
                                        }
                                    """)
        layout.addWidget(search_cargo_btn)

        view_history_btn = QPushButton("Gönderim Geçmişini Görüntüle", self)
        view_history_btn.clicked.connect(self.open_view_history_dialog)
        view_history_btn.setFont(QFont("Arial", 14))
        view_history_btn.setStyleSheet("""
                                                QPushButton {
                                                    background-color: #gray;
                                                            color: #FFFFFF;
                                                            border: 2px solid #9455f4;
                                                            border-radius: 10px;
                                                            padding: 10px;
                                                            margin: 8px;
                                                }
                                                QPushButton:hover {
                                                     background-color: #9455f4;
                                                }
                                                QPushButton:pressed {
                                                    background-color: #444444;
                                                }
                                            """)
        layout.addWidget(view_history_btn)

        list_all_cargos_btn = QPushButton("Tüm Kargoları Listele", self)
        list_all_cargos_btn.clicked.connect(self.open_list_all_cargos_dialog)
        list_all_cargos_btn.setFont(QFont("Arial", 14))
        list_all_cargos_btn.setStyleSheet("""
                                                        QPushButton {
                                                            background-color: #gray;
                                                            color: #FFFFFF;
                                                            border: 2px solid #9455f4;
                                                            border-radius: 10px;
                                                            padding: 10px;
                                                            margin: 8px;
                                                        }
                                                        QPushButton:hover {
                                                            background-color: #9455f4;
                                                        }
                                                        QPushButton:pressed {
                                                            background-color: #444444;
                                                        }
                                                    """)
        layout.addWidget(list_all_cargos_btn)

        show_routes_btn = QPushButton("Teslimat Rotalarını Göster", self)
        show_routes_btn.clicked.connect(self.open_show_routes_dialog)
        show_routes_btn.setFont(QFont("Arial", 14))
        show_routes_btn.setStyleSheet("""
                                                                QPushButton {
                                                                    background-color: #gray;
                                                            color: #FFFFFF;
                                                            border: 2px solid #9455f4;
                                                            border-radius: 10px;
                                                            padding: 10px;
                                                            margin: 8px;
                                                                }
                                                                QPushButton:hover {
                                                                     background-color: #9455f4;
                                                                }
                                                                QPushButton:pressed {
                                                                    background-color: #444444;
                                                                }
                                                            """)

        layout.addWidget(show_routes_btn)

    # Seçenekler için dialogları açıyoruz
    def open_add_customer_dialog(self):
        dialog = AddCustomerDialog(self.customer_management)
        dialog.exec()

    def open_add_cargo_dialog(self):
        dialog = AddCargoDialog(self.customer_management, self.priority_queue)
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
        dialog = ShowRoutesDialog()
        dialog.exec()


# Diğer dialog sınıfları
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

        add_button = QPushButton("Ekle", self)
        add_button.clicked.connect(self.add_customer)
        layout.addWidget(add_button)

        self.setLayout(layout)

    def add_customer(self):
        customer_id = self.id_input.text()
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        self.customer_management.add_customer(customer_id, first_name, last_name)
        self.accept()


class AddCargoDialog(QDialog):
    def __init__(self, customer_management, priority_queue):
        super().__init__()
        self.setWindowTitle("Kargo Ekle")
        self.setGeometry(150, 150, 400, 400)
        self.customer_management = customer_management
        self.priority_queue = priority_queue

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

        # Nereden ve Nereye için ComboBox
        self.from_city_input = QComboBox(self)
        self.from_city_input.addItems(self.get_city_list())
        self.from_city_input.setPlaceholderText("Nereden")
        layout.addWidget(self.from_city_input)

        self.to_city_input = QComboBox(self)
        self.to_city_input.addItems(self.get_city_list())
        self.to_city_input.setPlaceholderText("Nereye")
        layout.addWidget(self.to_city_input)

        add_button = QPushButton("Ekle", self)
        add_button.clicked.connect(self.add_cargo)
        layout.addWidget(add_button)

        self.setLayout(layout)

    def get_city_list(self):
        return [
            "İstanbul", "Ankara", "İzmir", "Antalya", "Adana", "Afyon", "Ağrı", "Aksaray", "Amasya",
            "Artvin", "Balıkesir", "Bartın", "Batman", "Bayburt", "Bilecik", "Bingöl", "Bitlis",
            "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır",
            "Düzce", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep",
            "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Iğdır", "Isparta", "Kahramanmaraş",
            "Karabük", "Karaman", "Kars", "Kastamonu", "Kayseri", "Kırıkkale", "Kırklareli",
            "Kırşehir", "Kilis", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Mardin",
            "Mersin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Osmaniye", "Rize", "Sakarya",
            "Samsun", "Siirt", "Sinop", "Sivas", "Şanlıurfa", "Şırnak", "Tekirdağ", "Tokat",
            "Trabzon", "Tunceli", "Uşak", "Van", "Yalova", "Yozgat", "Zonguldak"
        ]

    def add_cargo(self):
        customer_id = self.customer_id_input.text()
        cargo_id = self.cargo_id_input.text()
        send_date = self.send_date_input.text()
        delivery_time = int(self.delivery_time_input.text())
        from_city = self.from_city_input.currentText()
        to_city = self.to_city_input.currentText()

        customer = self.customer_management.get_customer(customer_id)
        if customer:
            cargo = Cargo(cargo_id, send_date, "Yolda", delivery_time, from_city, to_city)
            customer.add_cargo(cargo)
            self.priority_queue.add_cargo(cargo)
            self.accept()


class ShowRoutesDialog(QDialog):
    def __init__(self, customer_management):
        super().__init__()
        self.setWindowTitle("Teslimat Rotaları")
        self.setGeometry(150, 150, 600, 400)
        self.customer_management = customer_management

        layout = QVBoxLayout()

        self.tree_widget = QTreeWidget(self)
        self.tree_widget.setHeaderLabels(["Kargo ID", "Nereden", "Nereye"])
        layout.addWidget(self.tree_widget)

        self.populate_tree()

        self.setLayout(layout)

    def populate_tree(self):
        self.tree_widget.clear()
        for customer in self.customer_management.customers.values():
            for cargo in customer.cargo_history:
                root_item = QTreeWidgetItem([cargo.cargo_id, cargo.from_city, cargo.to_city])
                self.tree_widget.addTopLevelItem(root_item)



class SearchCargoDialog(QDialog):
    def __init__(self, customer_management):
        super().__init__()
        self.setWindowTitle("Kargo Durumu Sorgula")
        self.setGeometry(150, 150, 400, 300)
        self.customer_management = customer_management

        layout = QVBoxLayout()

        self.customer_id_input = QLineEdit(self)
        self.customer_id_input.setPlaceholderText("Müşteri ID")
        layout.addWidget(self.customer_id_input)

        self.cargo_id_input = QLineEdit(self)
        self.cargo_id_input.setPlaceholderText("Kargo ID")
        layout.addWidget(self.cargo_id_input)

        search_button = QPushButton("Sorgula", self)
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
                cargo_info = (
                    f"Kargo ID: {cargo.cargo_id}, Durum: {cargo.delivery_status}, "
                    f"Süre: {cargo.delivery_time} gün, Nereden: {cargo.source}, Nereye: {cargo.destination}"
                )
                self.result_label.setText(cargo_info)
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

        view_button = QPushButton("Göster", self)
        view_button.clicked.connect(self.view_history)
        layout.addWidget(view_button)

        # Geçmişi göstereceğimiz QLabel yerine bir QListWidget kullanalım
        self.history_list = QListWidget(self)
        layout.addWidget(self.history_list)

        self.setLayout(layout)

    def view_history(self):
        self.history_list.clear()  # Önceden var olan öğeleri temizle
        customer_id = self.customer_id_input.text()
        customer = self.customer_management.get_customer(customer_id)
        if customer:
            # Her bir gönderimi bir liste öğesi olarak ekleyelim
            for cargo in customer.cargo_history:
                cargo_info = f"Kargo ID: {cargo.cargo_id}, Durum: {cargo.delivery_status}, Tarih: {cargo.send_date}, Süre: {cargo.delivery_time} gün"
                self.history_list.addItem(cargo_info)
        else:
            self.history_list.addItem("Müşteri bulunamadı.")



class ListAllCargosDialog(QDialog):
    def __init__(self, customer_management):
        super().__init__()
        self.setWindowTitle("Tüm Kargolar")
        self.setGeometry(150, 150, 600, 400)
        self.customer_management = customer_management

        layout = QVBoxLayout()
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Müşteri ID", "Kargo ID", "Durum"])
        layout.addWidget(self.table)

        self.populate_table()

        self.setLayout(layout)

    def populate_table(self):
        self.table.setRowCount(0)
        for customer in self.customer_management.customers.values():
            for cargo in customer.cargo_history:
                row_position = self.table.rowCount()
                self.table.insertRow(row_position)
                self.table.setItem(row_position, 0, QTableWidgetItem(customer.customer_id))
                self.table.setItem(row_position, 1, QTableWidgetItem(cargo.cargo_id))
                self.table.setItem(row_position, 2, QTableWidgetItem(cargo.delivery_status))


class ShowRoutesDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Teslimat Rotaları")
        self.setGeometry(150, 150, 600, 400)

        layout = QVBoxLayout()

        self.tree_widget = QTreeWidget(self)
        self.tree_widget.setHeaderLabels(["Şehir Adı", "Şehir ID"])
        layout.addWidget(self.tree_widget)
        self.populate_tree()
        self.setLayout(layout)
    def populate_tree(self):
        root_item = QTreeWidgetItem(["Merkez", "0"])
        self.tree_widget.addTopLevelItem(root_item)
        # Örnek veri eklenebilir:
        child_item = QTreeWidgetItem(["İstanbul", "1"])
        root_item.addChild(child_item)
        child_item = QTreeWidgetItem(["Elazığ", "2"])
        root_item.addChild(child_item)
        child_item = QTreeWidgetItem(["Çanakkale", "3"])
        root_item.addChild(child_item)
        child_item = QTreeWidgetItem(["Isparta", "4"])
        root_item.addChild(child_item)
        child_item = QTreeWidgetItem(["Afyon", "5"])
        root_item.addChild(child_item)
        child_item = QTreeWidgetItem(["Ankara", "6"])
        root_item.addChild(child_item)
        child_item = QTreeWidgetItem(["Bursa", "7"])
        root_item.addChild(child_item)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
