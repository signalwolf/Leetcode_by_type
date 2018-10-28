class NrayTreeNode(object):
    def __init__(self, name):
        self.name = name
        self.death = False
        self.child = []

class Solution(object):
    def __init__(self):
        self.root = NrayTreeNode('King')
        self.name_dict = {'King': self.root}
        self.order = ['King']

    def birth(self, name, child_name):
        new_node = NrayTreeNode(child_name)
        self.name_dict[child_name] = new_node
        self.name_dict[name].child.append(new_node)
        self.order.insert(self.order.index(name) + len(self.name_dict[name].child), child_name)

    def death(self, name):
        self.name_dict[name].death = True
        self.order.remove(name)

    def rank(self):
        return self.order


king_family = Solution()
king_family.birth('King','1')
king_family.birth('King', '2')
king_family.birth('1', '11')
king_family.birth('1','12')
king_family.birth('2','21')
king_family.death('1')
king_family.death('King')
print king_family.rank()
