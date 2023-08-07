def mergeIntervals(intervals):
    intervals.sort(key=lambda x: x[0]) #interval list is sorted using sort function
    # here lambda x: x[0]  this sorts interval based on their start value, in ascending order
    merged = [] # empty list merged intialized. Which store merged intervals
    for interval in intervals:
        #check merged array is empty // or // end value of last interval is in merged is less than start value of current interval
        if not merged or merged[-1][1] < interval[0]: 
            merged.append(interval)
        else:#above not true it means overlaps with previous merged intervals.
            #then merged is updared to max value betn its current end value
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
result = mergeIntervals(arr)
print("The Merged Intervals are:", result)
