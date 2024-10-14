from algorithms.tree.tree_node import TreeNode 
class PlotableTree:
    def __init__(self):
        self.root = None
    
    def iterativeInsert(self, x):
        if self.root == None: 
            self.root = TreeNode(x)
        else:
            current = self.root
            while (True):
                if (x<=current.value):
                    if current.left == None:
                        current.left = TreeNode(x)
                        return
                    current = current.left
                else:
                    if current.right == None:
                        current.right = TreeNode(x)
                        return
                    current = current.right
    
    def recursiveInsert(self, x):
        if self.root == None: 
            self.root = TreeNode(x)
            return self.root
        else: return self.recursionInsert(x, self.root)

    def recursionInsert(self, x, current = None):
        if current == None: return current
        if x <= current.value:
            if current.left == None:
                current.left = TreeNode(x)
                return current.left
            self.recursionInsert(x, current.left)
        else: 
            if current.right == None:
                current.right = TreeNode(x)
                return current.right
            self.recursionInsert(x, current.right)

    def iterativeSearch(self, x):
        if self.root != None:
            current = self.root
            while (True):
                if current == None: return -1
                if x < current.value:
                    current = current.left
                elif x > current.value:
                    current = current.right
                else: return current
        return -1
               

    def recursiveSearch(self, x):
        if self.root != None:
            return self.recursionSearch(x, self.root)
        return -1
    
    def recursionSearch(self, x, current = None):
        if current == None: return -1
        if x < current.value:
            return self.recursionSearch(x, current.left)
        elif x > current.value:
            return self.recursionSearch(x, current.right)
        else: return current

    def iterativeDelete(self, x):
        if self.root != None:
            current = self.root
            previous = None
            while (True):
                if current == None: return -1
                if x < current.value:
                    previous = current
                    current = current.left
                elif x > current.value:
                    previous = current
                    current = current.right
                else: 
                    if current.value <= previous.value:
                        previous.left = current.left
                    else:
                        previous.right = current.right
                    current = None
                    return 0
        return -1

    def recursiveDelete(self, x):
        if self.root != None:
            return self.recursionDelete(x, None, self.root)
    
    def recursionDelete(self, x, previous = None, current = None):
         if current == None: return -1
         if x < current.value: self.recursionDelete(x, current, current.left)
         elif x > current.value: self.recursionDelete(x, current, current.right)
         else: 
            if current.value <= previous.value:
                previous.left = current.left
            else:
                previous.right = current.right
                current = None
                return 0

    def toString(self): raise NotImplementedError("Método toString não implementado!")
