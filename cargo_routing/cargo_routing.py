# node structure for each city
class Node:
    def __init__(self,city_name,city_id):
        self.city_name = city_name
        self.city_id = city_id
        self.children = []

    def add_child(self,child_node):
        self.children.append(child_node)


# tree structure for delivery
class DeliveryTree:
    def __init__(self,root):
        self.root = root

    def find_city(self,city_id,node=None):
        if node is None:
            node = self.root
        if node.city_id == city_id:
            return node
        for child in node.children:
            result = self.find_city(city_id,child)
            if result:
                return result
        return None

    def calculate_paths(self, node=None, current_depth=0, current_path=[], all_paths=[]):
        if node is None:
            node = self.root

        current_path.append((node, current_depth))

        if not node.children: # if node has no children then save it to all_paths
            all_paths.append((current_path, current_path[-1][1]))  # path, depth
        else:
            for child in node.children:
                self.calculate_paths(child, current_depth + 1, current_path[:], all_paths)

        return all_paths

    def display_tree(self,node=None,level =0):
        if node is None:
            node = self.root
        print(" " * level * 4 + f"{node.city_name} (ID: {node.city_id})")
        for child in node.children:
            self.display_tree(child, level + 1)

    def add_city(self, parent_id, city_name, city_id):
        parent_node = self.find_city(parent_id)
        if not parent_node:
            raise ValueError(f"Parent city with ID {parent_id} not found.")

        new_city = Node(city_name, city_id)
        parent_node.add_child(new_city)

