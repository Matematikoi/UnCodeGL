import queue

class TrieNode :
    def __init__(self, simbols): 
        self.children = {}
        for simbol in simbols:
            self.children[simbol]=None
  
        # is_end_of_word is True if node represent the end of the word 
        self.is_end_of_word = False

class Trie:
    """
    Data structure Trie.
    See more in :
    https://en.wikipedia.org/wiki/Trie#:~:text=In%20computer%20science%2C%20a%20trie,the%20keys%20are%20usually%20strings.
    """
    def __init__(self, simbols): 
        self.simbols = simbols
        self.root = self.getNode() 
  
    def getNode(self): 
        """Returns new trie node (initialized to NULLs) """
        return TrieNode(self.simbols)


    def insert(self, word): 
        """
        If not present, inserts key into trie 
        If the key is prefix of trie node,  
        just marks leaf node 
        """
        current_node = self.root 
        for current_simbol in word: 
            # if current character is not present 
            if not current_node.children[current_simbol]: 
                current_node.children[current_simbol] = self.getNode() 
            current_node = current_node.children[current_simbol] 
  
        # mark last node as leaf 
        current_node.is_end_of_word = True

    def search(self, word): 
        """  
        Search key in the trie 
        Returns true if key presents  
        in trie, else false 
        """
        current_node = self.root 
        for simbol in word: 
            if not current_node.children[simbol]: 
                return False
            current_node = current_node.children[simbol] 
  
        return current_node != None and current_node.is_end_of_word

    def is_prefix(self):
        """
        Search for prefixes of words
        """
        q = queue.Queue()
        q.put(self.root)
        while not q.empty() :
            current_node = q.get()
            has_childs = False
            for simbol in self.simbols:
                if current_node.children[simbol]  != None:
                    has_childs=True
                    q.put(current_node.children[simbol])
            if has_childs and current_node.is_end_of_word:
                return False

        return True