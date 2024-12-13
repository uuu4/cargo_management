from cargo_routing.cargo_routing import Node, DeliveryTree
root = Node("Merkez", 1)

tree = DeliveryTree(root)

tree.add_city(1, "Şehir A", 2)
tree.add_city(1, "Şehir B", 3)
tree.add_city(2, "Şehir B", 4)

tree.display_tree()

all_paths = tree.calculate_paths()

for path, depth in all_paths:
    print(" -> ".join([f"{node.city_name} (ID: {node.city_id})" for node, _ in path]))
    print(f"Toplam Teslimat Süresi: {depth}")
