# node structure for each city
class Node:
    def __init__(self,city_name,city_id,delivery_time=0):
        self.city_name = city_name
        self.city_id = city_id
        self.delivery_time = delivery_time
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

    def calculate_delivery_time(self,city_id,node=None):
        if node is None:
            node = self.root

        total_time = node.delivery_time
        for child in node.children:
            total_time += self.calculate_delivery_time(city_id,child)
        return total_time


