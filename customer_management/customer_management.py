class Cargo:
    def __init__(self, cargo_id, send_date, delivery_status, delivery_time):
        self.cargo_id = cargo_id  # Gönderi ID
        self.send_date = send_date  # Gönderi Tarihi
        self.delivery_status = delivery_status  # Teslim Durumu ("Teslim Edildi", "Teslim Edilmedi")
        self.delivery_time = delivery_time  # Teslim Süresi (gün)

    def __repr__(self):
        return f"[ID: {self.cargo_id}, Tarih: {self.send_date}, Durum: {self.delivery_status}, Süre: {self.delivery_time} gün]"


class Customer:
    def __init__(self, customer_id, first_name, last_name):
        self.customer_id = customer_id  # Müşteri ID
        self.first_name = first_name  # İsim
        self.last_name = last_name  # Soyisim
        self.cargo_history = []  # Gönderim Geçmişi (Liste olarak)

    def add_cargo(self, cargo):
        self.cargo_history.append(cargo)
        self.cargo_history.sort(key=lambda x: x.send_date)  # Tarih sırasına göre sıralama

    def display_cargo_history(self):
        if not self.cargo_history:
            print("Bu müşteri için gönderim geçmişi bulunmamaktadır.")
        else:
            print(f"{self.first_name} {self.last_name} için gönderim geçmişi:")
            for cargo in self.cargo_history:
                print(cargo)

    def __repr__(self):
        return f"[ID: {self.customer_id}, Ad: {self.first_name}, Soyad: {self.last_name}]"


class CustomerManagement:
    def __init__(self):
        self.customers = {}  # Müşteri ID'ye göre müşterileri saklayan bir sözlük

    def add_customer(self, customer_id, first_name, last_name):
        if customer_id in self.customers:
            print("Bu ID'ye sahip bir müşteri zaten mevcut.")
        else:
            new_customer = Customer(customer_id, first_name, last_name)
            self.customers[customer_id] = new_customer
            print(f"Müşteri {first_name} {last_name} başarıyla eklendi.")

    def get_customer(self, customer_id):
        return self.customers.get(customer_id, None)

    def display_all_customers(self):
        if not self.customers:
            print("Henüz müşteri eklenmedi.")
        else:
            print("Tüm Müşteriler:")
            for customer in self.customers.values():
                print(customer)


# Test ve Konsol Menüsü
def main():
    cm = CustomerManagement()

    while True:
        print("\n1. Yeni müşteri ekle")
        print("2. Müşteri bilgisi al ve kargo gönderimi ekle")
        print("3. Müşteri gönderim geçmişini görüntüle")
        print("4. Tüm müşterileri görüntüle")
        print("5. Çıkış")
        choice = int(input("Seçiminizi yapın: "))

        if choice == 1:
            customer_id = input("Müşteri ID'sini girin: ")
            first_name = input("İsim: ")
            last_name = input("Soyisim: ")
            cm.add_customer(customer_id, first_name, last_name)

        elif choice == 2:
            customer_id = input("Müşteri ID'sini girin: ")
            customer = cm.get_customer(customer_id)
            if customer:
                cargo_id = input("Kargo ID'sini girin: ")
                send_date = input("Gönderi Tarihi (YYYY-MM-DD): ")
                delivery_status = input("Teslim Durumu (Teslim Edildi/Teslim Edilmedi): ")
                delivery_time = int(input("Teslim Süresi (gün): "))
                new_cargo = Cargo(cargo_id, send_date, delivery_status, delivery_time)
                customer.add_cargo(new_cargo)
                print("Kargo gönderimi başarıyla eklendi.")
            else:
                print("Bu ID'ye sahip bir müşteri bulunamadı.")

        elif choice == 3:
            customer_id = input("Müşteri ID'sini girin: ")
            customer = cm.get_customer(customer_id)
            if customer:
                customer.display_cargo_history()
            else:
                print("Bu ID'ye sahip bir müşteri bulunamadı.")

        elif choice == 4:
            cm.display_all_customers()

        elif choice == 5:
            break

        else:
            print("Geçersiz seçim. Tekrar deneyin.")


if __name__ == "__main__":
    main()
