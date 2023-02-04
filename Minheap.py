class MinHeap:
    def __init__(self):
        self.heap = []  # Stores contents of the heap
 
    def insert(self, element):
        self.heap.append(element)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):    # Handle new element insertion
        parent = (index - 1) // 2   # Get parent index (E.g., 13 -> 16, 31 -> 41, 51, 100, 41)
        if index > 0 and self.heap[index] < self.heap[parent]:  # If the current element is smaller than its parent, swap them
            self.swap(index, parent)
            self.heapify_up(parent) # Recursively go up the tree and swap elements until the new element reaches its correct position
 
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i] # Swap when the current element is smaller than its parent

    def extract_min(self):
        if self.is_empty():
            return None

        if len(self.heap) == 1: # If there is only one element in the heap, simply take that element out
            return self.heap.pop()
        
        minimum = self.heap[0]
        self.heap[0] = self.heap.pop()  # Replace the root element with the last element in the heap. Will be sorted in next line
        self.heapify_down(0)
        return minimum
 
    def heapify_down(self, index):
        smallest = index
        left = 2 * index + 1  # Get left and right child indices
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]: # If the left child is smaller than the current element, set the smallest element to the left child
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]: # Will only be executed if index is greater than left child. If previous if statement is executed, this code block will not run
            smallest = right

        if smallest != index:
            self.swap(index, smallest)
            self.heapify_down(smallest) # Recursively go down the tree and swap elements until the new element reaches its correct position
 
    def is_empty(self):
        return len(self.heap) == 0

    def clear(self):
        self.heap = []

if __name__ == '__main__':
    min_heap = MinHeap()
    elements = [3, 2, 1, 7, 8, 4, 10, 16, 12]
    print("Inserting elements:", elements)
    for element in elements:
        min_heap.insert(element)
    print("Min heap after inserting elements:", min_heap.heap)
    print("Extracting minimum element:", min_heap.extract_min())
    print("Min heap after extracting minimum:", min_heap.heap)