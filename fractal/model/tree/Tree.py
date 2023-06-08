from model.tree.components.Node import Node


class Tree:
    def __init__(self):
        self.root: Node = Node()

    def generate_fractal_tree(self, base_offset_radians: float, num_layers: int):
        if type(base_offset_radians) is not float:
            raise TypeError("base_offset_radians must be float")
        if type(num_layers) is not int:
            raise TypeError("num_layers must be int")

        first_node = Node(0.0, 1.0, layer=1)
        first_node.parent = self.root
        self.root.left = first_node

        queue: list[Node] = [first_node]
        while len(queue) != 0:
            curr: Node = queue.pop(0)
            if curr.layer < num_layers:
                curr.set_left(base_offset_radians)
                curr.set_right(base_offset_radians)

                queue.append(curr.left)
                queue.append(curr.right)

    def get_root(self) -> Node:
        return self.root
