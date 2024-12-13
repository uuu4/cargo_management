import heapq
import json

# Cargo class
class Cargo:
    def __init__(self, cargo_id, delivery_time, status):
        self.cargo_id = cargo_id
        self.delivery_time = delivery_time
        self.status = status

    def __lt__(self, other):
        return self.delivery_time < other.delivery_time

    def __str__(self):
        return f"KargoID: {self.cargo_id}, Teslimat süresi: {self.delivery_time}, Durum: {self.status}"

# Priority Queue class
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def add_cargo(self, cargo):
        heapq.heappush(self.queue, cargo)
        print(f"Eklendi: {cargo}")

    def process_next_cargo(self):
        if not self.queue:
            print("İşlenecek kargo yok.")
            return None
        next_cargo = heapq.heappop(self.queue)
        next_cargo.status = "Teslim edildi"
        print(f"İşleniyor: {next_cargo}")
        return next_cargo

    def update_cargo_status(self, cargo_id, new_status):
        for cargo in self.queue:
            if cargo.cargo_id == cargo_id:
                cargo.status = new_status
                print(f"Güncellendi: {cargo}")
                return
        print(f"KargoID {cargo_id} kuyrukta bulunamadı.")

    def search_cargo(self, cargo_id):
        for cargo in self.queue:
            if cargo.cargo_id == cargo_id:
                print(f"Bulundu: {cargo}")
                return cargo
        print(f"KargoID {cargo_id} bulunamadı.")
        return None

    def report_statistics(self):
        total_cargos = len(self.queue)
        if total_cargos == 0:
            print("Kuyrukta kargo bulunmamaktadır.")
            return

        average_delivery_time = sum(cargo.delivery_time for cargo in self.queue) / total_cargos
        print(f"Toplam Kargo: {total_cargos}")
        print(f"Ortalama teslimat süresi: {average_delivery_time:.2f} gün")

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            cargos = [cargo.__dict__ for cargo in self.queue]
            json.dump(cargos, f)
        print(f"Kuyruk {filename} dosyasına kaydedildi.")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                cargos = json.load(f)
                self.queue = [Cargo(**cargo) for cargo in cargos]
            print(f"Kuyruk {filename} dosyasından yüklendi.")
        except FileNotFoundError:
            print(f"Dosya {filename} bulunamadı.")

    def print_queue(self):
        if not self.queue:
            print("Kuyruk boş.")
        else:
            print("Mevcut Kuyruk:")
            for cargo in self.queue:
                print(cargo)

# Test
if __name__ == "__main__":
    pq = PriorityQueue()

    # Add new cargos
    pq.add_cargo(Cargo("C1", 2, "Kargo yolda"))
    pq.add_cargo(Cargo("C2", 5, "Kargo yolda"))
    pq.add_cargo(Cargo("C3", 1, "Kargo yolda"))

    # Print the queue
    pq.print_queue()

    # Process next cargos
    pq.process_next_cargo()

    # Update cargo status
    pq.update_cargo_status("C2", "Kargo teslimata çıktı")

    # Search for a cargo
    pq.search_cargo("C3")

    # Reporting
    pq.report_statistics()

    # Save the queue to a file
    pq.save_to_file("queue.json")

    # Load the queue from a file
    pq.load_from_file("queue.json")

    # Print the queue
    pq.print_queue()
