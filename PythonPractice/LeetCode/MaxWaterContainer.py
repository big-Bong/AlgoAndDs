def maxArea(height):
    start = 1
    end = len(height)
    maxArea = 0

    while(start<end):
        if(height[start-1] <= height[end-1]):
            area = height[start-1]*(end-start)
            start += 1
        else:
            area = height[end-1]*(end-start)
            end -= 1
	
        maxArea = max(area,maxArea)
    
    return maxArea

height = [1,8,6,5,4,8,3,7]
print(maxArea(height))