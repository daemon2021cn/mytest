class Trie:
    # dictionary solution
    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        cur_node = self.tree

        for i in word:
            if i not in cur_node:
                cur_node[i] = {}
            cur_node = cur_node[i]

        cur_node['is_word'] = {}

    def search(self, word: str) -> bool:
        cur_node = self.tree

        for i in word:
            if i not in cur_node:
                return False
            cur_node = cur_node[i]

        return 'is_word' in cur_node

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.tree

        for i in prefix:
            if i not in cur_node:
                return False
            cur_node = cur_node[i]

        return True

    # binary tree solution
    #def __init__(self):
    #    self.elem = None
    #    self.l_child = None
    #    self.r_child = None
    #    self.tree = None

    #def insert(self, word: str) -> None:
    #    if self.tree is None:
    #        self.tree = Trie()
    #        self.tree.elem = word
    #        self.tree.l_child = Trie()
    #        self.tree.r_child = Trie()
    #    else:
    #        if word < self.tree.elem:
    #            self.tree.l_child.insert(word)
    #        else:
    #            self.tree.r_child.insert(word)

    #def search(self, word: str) -> bool:
    #    if self.tree is None:
    #        return False
    #    if self.tree.elem == word:
    #        return True
    #    else:
    #        if word < self.tree.elem:
    #            return self.tree.l_child.search(word)
    #        else:
    #            return self.tree.r_child.search(word)

    #def startsWith(self, prefix: str) -> bool:
    #    if self.tree is None:
    #        return False
    #    if self.tree.elem.startswith(prefix):
    #        return True
    #    else:
    #        if prefix < self.tree.elem:
    #            return self.tree.l_child.startsWith(prefix)
    #        else:
    #            return self.tree.r_child.startsWith(prefix)

    #def printTree(self):
    #    if self.tree:
    #        print(self.tree.elem)
    #        self.tree.l_child.printTree()
    #        self.tree.r_child.printTree()

# Your Trie object will be instantiated and called as such:
#obj = Trie()
#word = "apple"
#prefix = "app"
#obj.insert(word)
#param_2 = obj.search(word)
#param_3 = obj.startsWith(prefix)
#word = "app"
#obj.insert(word)
#param_4 = obj.search("app")
#param_5 = obj.startsWith(prefix)
#print(param_2,param_3,param_4,param_5)

#obj.insert("1")
#obj.insert("2")
#obj.insert("3")
#obj.printTree()
