# 题目描述
> 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

```java
class Trie {
    public class TrieNode {
        public int path;
        public int end;
        public TrieNode[] map;
        
        public TrieNode() {
            path = 0;
            end = 0;
            map = new TrieNode[26];
        }
    }
    
    private TrieNode root;

    /** Initialize your data structure here. */
    public Trie() {
        root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        if(word == null) return;
        TrieNode node = root;
        int idx = 0;
        char[] chs = word.toCharArray();
        for(int i = 0; i < chs.length; i++) {
            idx = chs[i] - 'a';
            if(node.map[idx] == null) {
                node.map[idx] = new TrieNode();
            }
            node = node.map[idx];
            node.path++;
        }
        node.end ++;
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        if(word == null) return false;
        
        char[] chs = word.toCharArray();
        TrieNode node = root;
        int idx = 0;
        for(int i = 0; i < chs.length; i++) {
            idx = chs[i] - 'a';
            if(node.map[idx] == null) {
                return false;
            }
            node = node.map[idx];
        }
        return node.end != 0;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        if(prefix == null) return false;
        
        char[] chs = prefix.toCharArray();
        TrieNode node = root;
        int idx = 0;
        for(int i = 0; i < chs.length; i++) {
            idx = chs[i] - 'a';
            if(node.map[idx] == null) {
                return false;
            }
            node = node.map[idx];
        }
        return node.path != 0;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
```