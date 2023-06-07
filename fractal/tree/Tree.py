from tree.components.Node import Node


class Tree:
    def __init__(self, base_offset_radians: float, num_layers: int):
        self.base_offset_radians: float = base_offset_radians
        self.num_layers: int = num_layers
        self.root: Node = Node()
        self.generate_fractal_tree()

    def generate_fractal_tree(self):
        first_node = Node(0.0, 1.0, layer=1)
        first_node.parent = self.root
        self.root.left = first_node

        queue: list[Node] = [first_node]
        while len(queue) != 0:
            curr: Node = queue.pop(0)
            if curr.layer < self.num_layers:
                curr.set_left(self.base_offset_radians)
                curr.set_right(self.base_offset_radians)

                queue.append(curr.left)
                queue.append(curr.right)

    def set_base_offset_radians(self, base_offset_radians: float):
        if type(base_offset_radians) is not float:
            raise TypeError("base_offset_radians must be float")
        self.base_offset_radians = base_offset_radians

    def set_num_layers(self, num_layers: int):
        if type(num_layers) is not int:
            raise TypeError("num_layers must be int")
        self.num_layers = num_layers

    def get_fractal_tree(self) -> Node:
        return self.root
