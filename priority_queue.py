from heapq import heappush, heappop

class Priority_Queue:
    def __init__(self):
        self.elements = []
    
    def isEmpty(self):
        return len(self.elements) == 0

    def sort(self):
        def merge(left, right):
            left_index = 0
            right_index = 0
            result = []
            while left_index < len(left) and right_index < len(right):
                if left[left_index] < right[right_index]:
                    result.append(left[left_index])
                    left_index += 1
                else:
                    result.append(right[right_index])
                    right_index += 1

            result += left[left_index:]
            result += right[right_index:]
            return result


        def merge_sort(elements):
            if len(elements) <= 1:
                return elements

            half = len(elements) // 2
            left = merge_sort(elements[:half])
            right = merge_sort(elements[half:])

            return merge(left, right)

        self.elements = merge_sort(self.elements)
    
    def push(self, x):
        #self.elements.append(x)
        #sort()
        heappush(self.elements, x)
    
    def pop(self):
        #return self.elements.pop()
        return heappop(self.elements)
        
