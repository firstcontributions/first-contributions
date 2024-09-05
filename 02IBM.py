def findOptimalResources(arr, k):
    n = len(arr)
    
    # If k is greater than the length of the array, it's impossible
    if k > n:
        return -1
    
    # Variables to keep track of the current window and maximum sum
    max_sum = -1
    current_sum = 0
    left = 0
    seen = set()
    
    # Sliding window approach
    for right in range(n):
        while arr[right] in seen:  # Remove duplicates by moving the left pointer
            seen.remove(arr[left])
            current_sum -= arr[left]
            left += 1
        
        # Add current element to the window
        seen.add(arr[right])
        current_sum += arr[right]
        
        # If window size equals k, check the sum
        if right - left + 1 == k:
            max_sum = max(max_sum, current_sum)
            
            # Slide the window forward by removing the leftmost element
            seen.remove(arr[left])
            current_sum -= arr[left]
            left += 1
    
    return max_sum if max_sum != -1 else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    result = findOptimalResources(arr, k)

    fptr.write(str(result) + '\n')

    fptr.close()