class Tree:

    def __init__(self, label, branches=[]):
        assert type(branches) == list
        self.label = label
        self.branches = branches
        self.is_leaf = not bool(branches)

    def get_label(self):
        return self.label

    def get_branches(self):
        return self.branches

    def get_branch(self, i):
        return self.branches[i]

    def print_tree(self, spacing=""):
        print(spacing + str(self.label))
        if self.is_leaf:
            return None
        for branch in self.branches:
            branch.print_tree(spacing=spacing+" ")

def create_tree(label, myFunc, max_rows=4):
    """Creates new tree based on a start label and relation function.
    The function myFunc should take in an integer and output a list of integers.
    int -> myFunc -> [int, int, ...]
    
    Ex:
        import random
        myFunc = lambda x: [random.randrange(x * 2) for i in range(random.randrange(x * 4))]
    """
    if max_rows <= 0:
        return Tree(label)
    next_labels = myFunc(label)
    tree = Tree(label, [create_tree(i, myFunc, max_rows=max_rows-1) for i in next_labels])
    return tree
