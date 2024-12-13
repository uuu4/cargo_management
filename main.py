# Creating root city
from cargo_routing.cargo_routing import Node, DeliveryTree
root = Node("Merkez", 1)

# Create tree
tree = DeliveryTree(root)

# Adding child cities
tree.add_city(1, "Şehir A", 2)
tree.add_city(1, "Şehir B", 3)
tree.add_city(2, "Şehir B", 4)

# Display the tree structure
tree.display_tree()

# Calculate all paths from root
all_paths = tree.calculate_paths()

# Output paths and their delivery times
for path, depth in all_paths:
    print(" -> ".join([f"{node.city_name} (ID: {node.city_id})" for node, _ in path]))
    print(f"Toplam Teslimat Süresi: {depth}")
