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
        self.cargo_stack = []  # Yığın (Stack) için liste



    def add_cargo(self, cargo):
        self.cargo_history.append(cargo)
        self.cargo_history = self.sort_by_date(self.cargo_history)  # Tarih sırasına göre sıralama

        # Yeni gönderimi yığına ekle (son 5 gönderim tutulur)
        self.cargo_stack.append(cargo)
        if len(self.cargo_stack) > 5:
            self.cargo_stack.pop(0)

    def sort_by_date(self, cargos):
        for i in range(len(cargos)):
            for j in range(0, len(cargos) - i - 1):
                if cargos[j].send_date > cargos[j + 1].send_date:
                    cargos[j], cargos[j + 1] = cargos[j + 1], cargos[j]
        return cargos

    def display_last_5_cargos(self):
        if not self.cargo_stack:
            print("Bu müşteri için gönderim geçmişi bulunmamaktadır.")
        else:
            print(f"{self.first_name} {self.last_name} için son 5 gönderim:")
            for cargo in reversed(self.cargo_stack):
                print(cargo)

    def search_delivered_cargo(self, cargo_id):
        delivered_cargos = [cargo for cargo in self.cargo_history if cargo.delivery_status == "Teslim Edildi"]
        delivered_cargos = self.sort_by_id(delivered_cargos)  # Kargo ID'ye göre sıralama

        # Binary Search
        left, right = 0, len(delivered_cargos) - 1
        while left <= right:
            mid = (left + right) // 2
            if delivered_cargos[mid].cargo_id == cargo_id:
                return delivered_cargos[mid]
            elif delivered_cargos[mid].cargo_id < cargo_id:
                left = mid + 1
            else:
                right = mid - 1
        return None

    def sort_by_id(self, cargos):
        for i in range(len(cargos)):
            for j in range(0, len(cargos) - i - 1):
                if cargos[j].cargo_id > cargos[j + 1].cargo_id:
                    cargos[j], cargos[j + 1] = cargos[j + 1], cargos[j]
        return cargos

    def sort_undelivered_cargos(self):
        undelivered_cargos = [cargo for cargo in self.cargo_history if cargo.delivery_status == "Teslim Edilmedi"]

        def quick_sort(array):
            if len(array) <= 1:
                return array
            pivot = array[0]
            less = [cargo for cargo in array[1:] if cargo.delivery_time <= pivot.delivery_time]
            greater = [cargo for cargo in array[1:] if cargo.delivery_time > pivot.delivery_time]
            return quick_sort(less) + [pivot] + quick_sort(greater)

        return quick_sort(undelivered_cargos)

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
        print("4. Müşteri son 5 gönderimi görüntüle")
        print("5. Teslim edilmiş kargoyu ID ile ara")
        print("6. Teslim edilmemiş kargoları sırala")
        print("7. Tüm müşterileri görüntüle")
        print("8. Çıkış")
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
            customer_id = input("Müşteri ID'sini girin: ")
            customer = cm.get_customer(customer_id)
            if customer:
                customer.display_last_5_cargos()
            else:
                print("Bu ID'ye sahip bir müşteri bulunamadı.")

        elif choice == 5:
            customer_id = input("Müşteri ID'sini girin: ")
            customer = cm.get_customer(customer_id)
            if customer:
                cargo_id = input("Aramak istediğiniz Kargo ID'sini girin: ")
                result = customer.search_delivered_cargo(cargo_id)
                if result:
                    print("Bulunan Kargo:", result)
                else:
                    print("Teslim edilmiş bu ID'ye sahip kargo bulunamadı.")
            else:
                print("Bu ID'ye sahip bir müşteri bulunamadı.")

        elif choice == 6:
            customer_id = input("Müşteri ID'sini girin: ")
            customer = cm.get_customer(customer_id)
            if customer:
                sorted_cargos = customer.sort_undelivered_cargos()
                print("Sıralanmış Teslim Edilmemiş Kargolar:")
                for cargo in sorted_cargos:
                    print(cargo)
            else:
                print("Bu ID'ye sahip bir müşteri bulunamadı.")

        elif choice == 7:
            cm.display_all_customers()

        elif choice == 8:
            break

        else:
            print("Geçersiz seçim. Tekrar deneyin.")

if __name__ == "__main__":
    main()
