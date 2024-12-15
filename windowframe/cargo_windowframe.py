from PySide6.QtWidgets import QApplication,QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QDialog, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QFontDatabase,QFont

# Müşteri Listesi
customer_list = []

# Ana Menü Penceresi
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Online Kargo Takip Sistemi')
        self.setGeometry(600, 200, 500, 450)

        # Ana Layout
        layout = QVBoxLayout()

        # Başlık
        font = QFont("Times New Roman", 36)  # Times New Roman yazı tipi, 36 px boyutunda
        font.setItalic(True)  # Yazıyı italik yapar
        label = QLabel("Ana Menü", self)
        label.setFont(font)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 70px; font-weight: bold; color: gray;")
        layout.addWidget(label)

        # Butonlar
        button1 = QPushButton("Yeni Müşteri Ekle", self)
        button1.clicked.connect(self.open_new_customer_window)

        button2 = QPushButton("Kargo Gönderimi Ekle", self)
        button2.clicked.connect(self.open_new_shipment_window)

        button3 = QPushButton("Kargo Durumu Sorgula", self)
        button3.clicked.connect(self.open_tracking_window)

        button4 = QPushButton("Gönderim Geçmişini Görüntüle", self)
        button4.clicked.connect(self.open_shipment_history_window)

        button5 = QPushButton("Tüm Kargoları Listele", self)
        button5.clicked.connect(self.show_customer_list)

        button6 = QPushButton("Teslimat Rotalarını Göster", self)
        button6.clicked.connect(self.open_route_visualization_window)

        # Butonlara stil ekleyelim
        button_style = "background-color: #4CAF50; color: white; font-size: 16px; border-radius: 10px; padding: 10px;"
        button1.setStyleSheet(button_style)
        button2.setStyleSheet(button_style)
        button3.setStyleSheet(button_style)
        button4.setStyleSheet(button_style)
        button5.setStyleSheet(button_style)
        button6.setStyleSheet(button_style)

        # Butonları ekleyelim
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)
        layout.addWidget(button6)

        self.setLayout(layout)

    def open_new_customer_window(self):
        self.new_customer_window = NewCustomerWindow()
        self.new_customer_window.exec()

    def open_new_shipment_window(self):
        self.new_shipment_window = NewShipmentWindow()
        self.new_shipment_window.exec()

    def open_tracking_window(self):
        self.tracking_window = TrackingWindow()
        self.tracking_window.exec()

    def open_shipment_history_window(self):
        self.shipment_history_window = ShipmentHistoryWindow()
        self.shipment_history_window.exec()

    def show_customer_list(self):
        if not customer_list:
            customer_list_text = "Müşteri Listesi Boş"
        else:
            customer_list_text = "\n".join([
                f"{customer.get('id', 'ID Yok')}: {customer.get('name', 'İsim Yok')} {customer.get('surname', 'Soyisim Yok')}"
                for customer in customer_list
            ])

        customer_list_dialog = QDialog(self)
        customer_list_dialog.setWindowTitle("Müşteri Listesi")
        layout = QVBoxLayout()

        label = QLabel(customer_list_text, self)
        label.setStyleSheet("font-size: 14px;")
        layout.addWidget(label)

        ok_button = QPushButton("Tamam", self)
        ok_button.clicked.connect(customer_list_dialog.accept)
        layout.addWidget(ok_button)

        customer_list_dialog.setLayout(layout)
        customer_list_dialog.exec()

    def open_route_visualization_window(self):
        self.route_visualization_window = RouteVisualizationWindow()
        self.route_visualization_window.exec()


# Yeni Müşteri Ekleme Penceresi
class NewCustomerWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yeni Müşteri Ekle")
        self.setGeometry(150, 150, 350, 250)

        layout = QVBoxLayout()

        label = QLabel("Müşteri Bilgilerini Girin", self)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("İsim")
        layout.addWidget(self.name_input)

        self.surname_input = QLineEdit(self)
        self.surname_input.setPlaceholderText("Soyisim")
        layout.addWidget(self.surname_input)

        self.id_input = QLineEdit(self)
        self.id_input.setPlaceholderText("Müşteri ID")
        layout.addWidget(self.id_input)

        save_button = QPushButton("Kaydet", self)
        save_button.clicked.connect(self.save_customer)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_customer(self):
        name = self.name_input.text()
        surname = self.surname_input.text()
        customer_id = self.id_input.text()

        if self.is_unique_id(customer_id):
            customer_list.append({"name": name, "surname": surname, "id": customer_id})
            self.accept()
        else:
            self.show_error("Bu ID zaten kullanılıyor!")

    def is_unique_id(self, customer_id):
        for customer in customer_list:
            if customer['id'] == customer_id:
                return False
        return True

    def show_error(self, message):
        error_dialog = QDialog(self)
        error_dialog.setWindowTitle("Hata")
        layout = QVBoxLayout()
        layout.addWidget(QLabel(message))
        ok_button = QPushButton("Tamam")
        ok_button.clicked.connect(error_dialog.accept)
        layout.addWidget(ok_button)
        error_dialog.setLayout(layout)
        error_dialog.exec()


# Yeni Kargo Gönderimi Ekleme Penceresi
class NewShipmentWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yeni Kargo Gönderimi")
        self.setGeometry(150, 150, 350, 300)

        layout = QVBoxLayout()

        label = QLabel("Kargo Bilgilerini Girin", self)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        self.id_input = QLineEdit(self)
        self.id_input.setPlaceholderText("Kargo ID")
        layout.addWidget(self.id_input)

        self.delivery_time_input = QLineEdit(self)
        self.delivery_time_input.setPlaceholderText("Tahmini Teslimat Süresi (Gün)")
        layout.addWidget(self.delivery_time_input)

        save_button = QPushButton("Kaydet", self)
        save_button.clicked.connect(self.save_shipment)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_shipment(self):
        shipment_id = self.id_input.text()
        delivery_time = self.delivery_time_input.text()

        print(f"Kargo ID: {shipment_id}, Teslimat Süresi: {delivery_time} gün")
        self.accept()


# Kargo Durumu Sorgulama Penceresi
class TrackingWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kargo Durumu Sorgula")
        self.setGeometry(150, 150, 350, 300)

        layout = QVBoxLayout()

        label = QLabel("Kargo ID'sini Girin", self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(label)

        self.tracking_input = QLineEdit(self)
        self.tracking_input.setPlaceholderText("Kargo ID")
        self.tracking_input.setStyleSheet("font-size: 14px; padding: 10px; border: 1px solid #ccc;")
        layout.addWidget(self.tracking_input)

        search_button = QPushButton("Sorgula", self)
        search_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 14px; border-radius: 8px; padding: 8px;")
        search_button.clicked.connect(self.search_tracking)
        layout.addWidget(search_button)

        self.result_label = QLabel("Kargo Durumu: ", self)
        layout.addWidget(self.result_label)

        self.history_label = QLabel("Kargo Geçmişi: ", self)
        layout.addWidget(self.history_label)

        self.setLayout(layout)

    def search_tracking(self):
        tracking_id = self.tracking_input.text()
        kargo_durumu = "Teslim Edildi"
        kargo_gecmisi = ["1. Adım: Teslim Alındı", "2. Adım: Dağıtıma Çıktı", "3. Adım: Teslim Edildi"]

        self.result_label.setText(f"Kargo Durumu: {kargo_durumu}")
        self.history_label.setText(f"Kargo Geçmişi:\n" + "\n".join(kargo_gecmisi))


# Gönderim Geçmişi Penceresi
class ShipmentHistoryWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gönderim Geçmişi")
        self.setGeometry(150, 150, 400, 300)

        layout = QVBoxLayout()

        label = QLabel("Gönderim Geçmişi", self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(label)

        self.filter_input = QLineEdit(self)
        self.filter_input.setPlaceholderText("Filtrele (Tarih veya Durum)")
        layout.addWidget(self.filter_input)

        filter_button = QPushButton("Filtrele", self)
        filter_button.clicked.connect(self.filter_history)
        layout.addWidget(filter_button)

        self.history_label = QLabel("Gönderim Geçmişi:")
        layout.addWidget(self.history_label)

        self.setLayout(layout)

    def filter_history(self):
        filtered_history = ["Kargo 1: Teslim Edildi", "Kargo 2: Teslim Edilmedi"]
        self.history_label.setText("Filtrelenmiş Gönderim Geçmişi:\n" + "\n".join(filtered_history))


# Teslimat Rotalarını Görselleştirme Penceresi
class RouteVisualizationWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Teslimat Rotalarını Göster")
        self.setGeometry(150, 150, 600, 400)

        layout = QVBoxLayout()

        label = QLabel("Teslimat Rotalarını Görselleştir", self)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        layout.addWidget(self.view)

        self.setLayout(layout)


# Uygulamayı başlat
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()