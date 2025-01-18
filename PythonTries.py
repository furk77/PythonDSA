# Tries aka prefix trees
class TrieNode:
    def __init__(self):
        """
        Initializes an empty TrieNode.
        
        children: A dictionary of children nodes, where each key is a character and each value is a TrieNode {'char': TrieNode}.
        endOfWord: A boolean indicating whether the node is the end of a word.
        """
        self.children = {}
        self.endOfWord = False
    
    def __str__(self) -> str:
        return f"children: {self.children}, endOfWord: {self.endOfWord}"

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word):
        """
        Inserts a word into the Trie. If the word does not exist, it adds the necessary nodes to represent the word.
        Marks the last node as the end of a word.
        
        word: The word to be inserted into the Trie.
        """
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]

        current.endOfWord = True
    
    def search(self, word):
        """
        Searches for a given word in the Trie and returns True if it exists, False otherwise.
        """
        current = self.root

        for c in word:
            if c not in current.children:
                return False

            current = current.children[c]

        return current.endOfWord
    
    def startsWith(self, prefix):
        """
        Returns True if there is any word in the Trie that starts with the given prefix, and False otherwise.
        
        prefix: The prefix to search for in the Trie.
        """
        current = self.root

        for c in prefix:
            if c not in current.children:
                return False

            current = current.children[c]

        return True


trie = Trie()
trie.insert("apple")
trie.insert("pear")
print(trie.root)
print(trie.startsWith("app"))
print(trie.search("appl"))
