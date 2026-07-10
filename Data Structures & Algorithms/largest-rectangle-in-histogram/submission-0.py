class Solution:
    # time - O(n), space - O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(0)
        for i in range(len(heights)):
            start = i
            while stack and heights[i] < stack[-1][1]:
                popIndex, curHeight = stack.pop()
                width = i - popIndex
                area = curHeight * width
                maxArea = max(maxArea, area)
                start = popIndex
            stack.append((start, heights[i]))
        return maxArea