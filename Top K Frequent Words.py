# node for storing word and its frequency value
class Node:
    def __init__(self,word,val):
        self.word = word
        self.val = val

class heap:
    def __init__(self,arr):
        self.arr = arr
        self.heap_len = len(arr)
        for i in range((len(self.arr)/2)-1,-1,-1):
            self.heapify(i)
           
    def heapify(self,parent):
        left = 2*parent+1
        right = 2*parent+2
        largest = parent
        
        if left < self.heap_len:
            if self.arr[left].val>self.arr[parent].val:
                largest = left
            # if left and parent values are equal
            if self.arr[left].val==self.arr[parent].val:
                if self.arr[left].word<self.arr[parent].word:
                    largest = left
        if right < self.heap_len:
            if self.arr[right].val>self.arr[largest].val:
                largest = right
            if self.arr[right].val==self.arr[largest].val:
                if self.arr[right].word<self.arr[largest].word:
                    largest = right
        if largest != parent:
            self.arr[largest],self.arr[parent] = self.arr[parent],self.arr[largest]
            self.heapify(largest)
    
    # returns the most frequent element
    def extract_max(self):
        if self.heap_len <= 0:
            return -1
        
        m = self.arr[0]
        self.arr[0] = self.arr[self.heap_len-1]
        self.heap_len -= 1
        self.heapify(0)
        
        return m

class Solution(object):
    def topKFrequent(self, words, k):
        d = dict()
        words_l = list()
        for word in words:
            d.setdefault(word,0)
            d[word] += 1
        
        for i in d:
            words_l.append(Node(i,d[i]))

        #building word heap
        word_heap = heap(words_l)
        
        result = []
        for i in range(0,k):
            a = word_heap.extract_max()
            result.append(a.word)
            
        return result