class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val==None:
            self.val=val
        elif self.val==val:
            return
        elif self.val>val and self.left == None:
            self.left=BSTNode(val)
            return
        elif self.val>val:
            self.left.insert(val)
        elif self.val<val and self.right == None:
            self.right=BSTNode(val)
            return
        elif self.val<val:
            self.right.insert(val)
        
