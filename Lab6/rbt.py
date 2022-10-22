import sys

class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
         return "(" + str(self.value) + "," + self.colour + ")"

    def recolor(self):
        if self.is_red:
            self.make_black
        else:
            self.make_red

class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, node):
        #You may alter code in this method if you wish, it's merely a guide.
        if node.parent == None:
            node.make_black()
        while node != None and node.parent != None and node.parent.is_red(): 
            p = node.parent
            gp = node.parent.parent
            if (p == gp.left):
                if node.get_uncle() != None and  node.get_uncle().is_red():
                    gp.make_red()
                    p.make_black()
                    node.get_uncle().make_black()
                    node = gp
                else:
                    if node == p.right:
                        self.rotate_left(p)
                        node = p
                        p = node.parent
                    self.rotate_right(gp)  
                    temp = p.colour
                    p.colour = gp.colour
                    gp.colour = temp
                    node = p
            else:
                if node.get_uncle() != None and  node.get_uncle().is_red():
                    gp.make_red()
                    p.make_black()
                    node.get_uncle().make_black()
                    node = gp
                else:
                    if node == p.left:
                        self.rotate_right(p)
                        node = p
                        p = node.parent
                    self.rotate_left(gp)      
                    temp = p.colour
                    p.colour = gp.colour
                    gp.colour = temp
                    node = p
        self.root.make_black()                  
    
    def rotate_left(self, node):
        r = node.right
        node.right = r.left
        if node.right != None:
            node.right.parent = node
        r.parent = node.parent
        if node.parent == None:
            self.root = r
        elif node == node.parent.left:
            node.parent.left = r
        else:
            node.parent.right = r
        r.left = node
        node.parent = r

    def rotate_right(self, node):
        l = node.right
        node.left = l.right
        if node.left != None:
            node.left.parent = node
        l.parent = node.parent
        if node.parent == None:
            self.root = l
        elif node == node.parent.left:
            node.parent.left = l
        else:
            node.parent.right = l
        l.right = node
        node.parent = l
        
    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"

    def __print_helper(self, node, indent, last):
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.item) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)


    def print_tree(self):
        self.__print_helper(self.root, "", True)
