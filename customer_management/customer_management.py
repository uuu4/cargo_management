# Kargo bilgilerini tutmak için bir sınıf
class Cargo:
    def __init__(self, cargo_id, delivery_time, status):
        self.cargo_id = cargo_id  # Kargo ID'si
        self.delivery_time = delivery_time  # Teslim süresi (gün olarak)
        self.status = status  # Kargo durumu (\"İşleme Alındı\", \"Teslimatta\", \"Teslim Edildi\")

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, cargo):
        # Kargoyu teslim süresine göre sıraya ekle
        self.queue.append(cargo)
        self.queue.sort(key=lambda x: x.delivery_time)

    def dequeue(self):
        # En öncelikli kargoyu sıradan çıkar
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Sıra boş.")
            return None

    def display(self):
        print("Sıradaki kargolar:")
        for cargo in self.queue:
            print(f"ID: {cargo.cargo_id}, Teslim Süresi: {cargo.delivery_time}, Durum: {cargo.status}")

# Örnek işlevler
def add_cargo(priority_queue):
    cargo_id = input("Kargo ID'sini girin: ")
    delivery_time = int(input("Teslim süresini (gün) girin: "))
    status = "İşleme Alındı"
    new_cargo = Cargo(cargo_id, delivery_time, status)
    priority_queue.enqueue(new_cargo)
    print(f"Kargo {cargo_id} sıraya eklendi.")

def process_priority_cargo(priority_queue):
    processed_cargo = priority_queue.dequeue()
    if processed_cargo:
        print(f"Kargo işleniyor: ID: {processed_cargo.cargo_id}, Teslim Süresi: {processed_cargo.delivery_time}")

# Test kodu
def main():
    queue = PriorityQueue()
    while True:
        print("\n1. Yeni kargo ekle")
        print("2. Öncelikli kargoyu işle")
        print("3. Sırayı görüntüle")
        print("4. Çıkış")
        choice = int(input("Seçiminizi yapın: "))

        if choice == 1:
            add_cargo(queue)
        elif choice == 2:
            process_priority_cargo(queue)
        elif choice == 3:
            queue.display()
        elif choice == 4:
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
