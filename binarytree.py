class BSTNode:

    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
class BST:
    def __init__(self):
        self.root = None

    def find_recursive(self, node, key):
        if None == node or key == node.key:
            return node
        elif key < node.key:
            return self.find_recursive(node.left, key)
        else:
            return self.find_recursive(node.right, key)
    def search(self, key):
       
        return self.find_recursive(self.root, key)
    def insert(self, key):

        if None == self.root:
            self.root = BSTNode(key)
            return True

        current_node = self.root
        while current_node:
            if key == current_node.key:
                print "The key does exist!"
                return False
            elif key < current_node.key:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = BSTNode(key, current_node)
                    return True
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = BSTNode(key, current_node)
                    return True
    def replace_node(self, node, new_node):
        
        if node == self.root:
            self.root = new_node
            return
        parent = node.parent
        if parent.left and parent.left == node:
            parent.left = new_node
        elif parent.right and parent.right == node:
            parent.right = new_node
        else:
            print "Incorrect parent-children relation!"
            raise RuntimeError
    def remove_node(self, node):
        
        if node.left and node.right:    # the node has two children

            # Find its in-order successor
            successor = node.right
            while successor.left:
                successor = successor.left
            # Copy the node
            node.key = successor.key
            # Remove the successor
            self.remove_node(successor)
        elif node.left:     # the node only has a left child
            self.replace_node(node, node.left)
        elif node.right:    # the node only has a right child
            self.replace_node(node, node.right)
        else:               # the node has no children
            self.replace_node(node, None)

    def delete(self, key):
        node = self.search(key)
        if node:
            self.remove_node(node)
	else:
	    print"node not found"

    def preorder(self, node):
        if node != None:
            print node.key
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node != None:
            self.inorder(node.left)
            print node.key
            self.inorder(node.right)

    def postorder(self, node):
        if node != None:
            self.inorder(node.left)
            self.inorder(node.right)
	    print node.key
    def traversal(self,choice):
        if choice == 1:
            self.preorder(self.root)
        elif choice == 2:
            self.inorder(self.root)
        elif choice == 3:
            self.postorder(self.root)
    def isempty(self):
	if(root==None):
	    return False
	else:
	    return True
tree=BST()
while(1):	
    choice = input("press 1 to insert in bst\npress 2 to delete from bst\npress 3 for preorder traversal \npress 4 for inorder traversal\npress 5 for postorder traversal\npress 6 to search a node\npress 7 to check whether BST is empty or no?\npress 8 to exit")
    if(choice==1):
        number=input("enter the number to insert in BST")
        if(tree.insert(number)==True):
	    print"add successfully"
        else:
	    print"adding not success"
    elif(choice==2):
        number=input("enter the number to delete node in BST")
        tree.delete(number)
    elif(choice==3):
	print"preorder"
        tree.traversal(1)
    elif(choice==4):
	print"inorder"
        tree.traversal(2)
    elif(choice==5):
	print"postorder"
        tree.traversal(3)
    elif(choice==6):
        number=input("enter the number to search in BST")
        if(tree.search(number)!=None):
            print"node found"
        else:
	    print"node not found"
    elif(choice==7):
	if(tree.root==None):
	    print"Empty"
	else:
	    print"Not Empty"
    elif(choice==8):
	exit(1)
