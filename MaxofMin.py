from collections import deque
def printMaxOfMin(nums, n):
    output_array = []
    queue = deque()
    for index, ele in enumerate(nums):
        if queue and  (index - queue[0]) >= n :
            queue.popleft() 
        while queue and nums[queue[-1]] > ele:
            queue.pop()
        queue.append(index)    
        if index+1 >= n:
            output_array.append(nums[queue[0]])  
    return max(output_array)
space=[1,3,-1,-3,5,3,6,7]
n=3
print(printMaxOfMin(space,n))
