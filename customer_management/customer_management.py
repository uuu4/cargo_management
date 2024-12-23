class Cargo:
    def __init__(self, cargo_id, send_date, delivery_status, delivery_time, source, destination):
        self.cargo_id = cargo_id
        self.send_date = send_date
        self.delivery_status = delivery_status
        self.delivery_time = delivery_time
        self.source = source
        self.destination = destination

    def __repr__(self):
        return f"ID: {self.cargo_id}, Tarih: {self.send_date}, Durum: {self.delivery_status}, Süre: {self.delivery_time} gün, Nereden: {self.source}, Nereye: {self.destination}"

    def __lt__(self, other):
        # Assuming the priority is based on the `id`
        return self.cargo_id < other.cargo_id


class LinkedListNode:
    def __init__(self, cargo):
        self.cargo = cargo
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def quick_sort(self, cargos):
        if len(cargos) <= 1:
            return cargos
        pivot = cargos[len(cargos) // 2]
        left = [cargo for cargo in cargos if cargo.delivery_time < pivot.delivery_time]
        middle = [cargo for cargo in cargos if cargo.delivery_time == pivot.delivery_time]
        right = [cargo for cargo in cargos if cargo.delivery_time > pivot.delivery_time]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    def add_sorted(self, cargo):
        # Convert the linked list to a list for sorting
        cargos = self.to_list()

        # Add the new cargo
        cargos.append(cargo)

        # Sort the list based on delivery_time using Quick Sort
        sorted_cargos = self.quick_sort(cargos)

        # Rebuild the linked list from the sorted cargos
        self.head = None
        for cargo in sorted_cargos[::-1]:
            self.add_to_head(cargo)

    def add_to_head(self, cargo):
        new_node = LinkedListNode(cargo)
        new_node.next = self.head
        self.head = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.cargo
            current = current.next

    def display(self):
        return "\n".join([str(cargo) for cargo in self])

    def search(self, cargo_id):
        for cargo in self:
            if cargo.cargo_id == cargo_id:
                return cargo
        return None

    def to_list(self):
        return [cargo for cargo in self]


class Customer:
    def __init__(self, customer_id, first_name, last_name):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.cargo_history = LinkedList()  # Gönderim geçmişi LinkedList olarak tutulur.
        self.cargo_stack = []  # Yığın (Stack) yapısı son 5 gönderimi tutar.

    def add_cargo(self, cargo):
        # Bağlı listeye kargo ekleme
        self.cargo_history.add_sorted(cargo)

        # Yığına son gönderimi ekleme
        self.cargo_stack.append(cargo)
        if len(self.cargo_stack) > 5:
            self.cargo_stack.pop(0)

    def search_delivered_cargo(self, cargo_id):
        # Teslim edilen kargolar arasında ara
        current = self.cargo_history.head
        while current:
            if current.cargo.cargo_id == cargo_id:
                return current.cargo
            current = current.next
        return None

    def display_last_5_cargos(self):
        if not self.cargo_stack:
            print("Bu müşteri için gönderim geçmişi bulunmamaktadır.")
        else:
            print(f"{self.first_name} {self.last_name} için son 5 gönderim:")
            for cargo in reversed(self.cargo_stack):
                print(cargo)

    def search_cargo(self, cargo_id):
        return self.cargo_history.search(cargo_id)

    def display_cargo_history(self):
        history = self.cargo_history.display()
        if not history:
            return "Bu müşteri için gönderim geçmişi bulunmamaktadır."
        return history

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
            return "Henüz müşteri eklenmedi."
        return "\n".join([str(customer) for customer in self.customers.values()])

    def __repr__(self):
        return f"Müşteri Sayısı: {len(self.customers)}"


# Test ve Konsol Menüsü
def main():
    cm = CustomerManagement()

    while True:
        print("\n1. Yeni müşteri ekle")
        print("2. Müşteri bilgisi al ve kargo gönderimi ekle")
        print("3. Müşteri gönderim geçmişini görüntüle")
        print("4. Müşteri son 5 gönderimi görüntüle")
        print("5. Tüm müşterileri görüntüle")
        print("6. Çıkış")
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
                delivery_time = int(input("Teslim Süresi (gün): "))
                source = input("Nereden (Şehir): ")
                destination = input("Nereye (Şehir): ")
                new_cargo = Cargo(cargo_id, send_date, delivery_time, source, destination)
                customer.add_cargo(new_cargo)
                print("Kargo gönderimi başarıyla eklendi.")
            else:
                print("Bu ID'ye sahip bir müşteri bulunamadı.")

        elif choice == 3:
            customer_id = input("Müşteri ID'sini girin: ")
            customer = cm.get_customer(customer_id)
            if customer:
                print(customer.display_cargo_history())
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
            print(cm.display_all_customers())

        elif choice == 6:
            break

        else:
            print("Geçersiz seçim. Tekrar deneyin.")


if __name__ == "__main__":
    main()
