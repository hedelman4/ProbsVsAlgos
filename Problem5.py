from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

## Represents a single node in the Trie
class TrieNode(object):
    def __init__(self, char = ''):
        self.children = {}
        self.char = char
        ## Initialize this node in the Trie

    def suffixes(self, suffix = '', suffixList = []):
        if len(self.children) > 1:
            for _ in self.children:
                #if suffix != '':
                suffix1 = suffix + _
                self.children[_].suffixes(suffix1)

        elif len(self.children) == 1:
            for _ in self.children:
                suffix += _
                self.children[_].suffixes(suffix)

        else:
            suffixList.append(suffix)
        return suffixList


        ## Recursive function that collects the suffix for
        ## all complete words below this point

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()
        ## Initialize this Trie (add a root node)

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode(char)
            current_node = current_node.children[char]
        ## Add a word to the Trie

    def find(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node
        ## Find the Trie node that represents this prefix


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

print(MyTrie.find('a').suffixes())
print(MyTrie.find('f').suffixes())
print(MyTrie.find('t').suffixes())
