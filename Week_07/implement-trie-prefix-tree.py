class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 字符串空的不行
        self.root = {'#':True}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            if char in node:
                node = node[char]
            else:
                node[char] = {}
                node = node[char]
        node['#'] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char in node:
                node = node[char]
            else:
                return False
        return node.get('#',False)

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char in node:
                node = node[char]
            else:
                return False
        return True