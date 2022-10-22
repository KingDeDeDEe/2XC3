import rbt

red_black_tree = rbt.RBTree()

for i in range(10):
    red_black_tree.insert(i)

print(red_black_tree)
rbt.print_tree(red_black_tree)