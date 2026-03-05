def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for i in range(1, len(intervals)):
        last_merged_start, last_merged_end = merged[-1]
        current_start, current_end = intervals[i]
        if current_start <= last_merged_end:
            merged[-1][1] = max(last_merged_end, current_end)
        else:
            merged.append(intervals[i])
            
    return merged

intervals_input = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(f"Input:  {intervals_input}")
print(f"Merged: {merge(intervals_input)}")