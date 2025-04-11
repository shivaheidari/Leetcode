"""
Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals and return an array of non-overlapping intervals.

Example:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Intervals [1,3] and [2,6] overlap → merged into [1,6]


"""

def intervals(arr):
   
    arr.sort(key=lambda x: x[0])
    merged = []
    print(arr)
    for i in range(len(arr)-1):
        print("i", i)
        j = i + 1
        current_start = arr[i][0]
        current_end = arr[i][1]
        print("j", j)
        while j < len(arr):
            print("in J ", j)
            next_start = arr[j][0]
            next_end = arr[j][1]

            if next_start <= current_end : #in the interval
                merged_start = min(next_start, current_start)
                merged_end = max(next_end, current_end)
                merged.append([merged_start, merged_end])
                arr[i] = [merged_start, merged_end]
                if j+1<=len(arr)-1:
                   arr[j] = arr[j+1]
            j += 1
    return arr
       


print(intervals([[0,1],[9,10], [1,4], [3,12]]))