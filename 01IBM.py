def getProfitablePairs(profit, implementationCost):
    # Get the number of elements
    n = len(profit)
    
    # Create a list for net profits
    netProfit = []
    
    # Calculate the net profit for each pair of profit and implementation cost
    for i in range(n):
        netProfit.append(profit[i] - implementationCost[i])
    
    # Sort the netProfit list for two-pointer technique
    netProfit.sort()
    
    count = 0
    left = 0
    right = n - 1
    
    # Use two-pointer technique to count the profitable pairs
    while left < right:
        # If the sum of net profits is positive, count all pairs from left to right
        if netProfit[left] + netProfit[right] > 0:
            count += (right - left)  # All pairs between left and right are profitable
            right -= 1  # Move the right pointer leftwards
        else:
            left += 1  # Move the left pointer rightwards to increase the sum
    
    return count


if __name__ == '__main__':
    # Reading the input values
    profit_count = int(input().strip())

    profit = []
    for _ in range(profit_count):
        profit_item = int(input().strip())
        profit.append(profit_item)

    implementationCost_count = int(input().strip())

    implementationCost = []
    for _ in range(implementationCost_count):
        implementationCost_item = int(input().strip())
        implementationCost.append(implementationCost_item)

    # Call the function to get the result
    result = getProfitablePairs(profit, implementationCost)

    # Print the result directly for simplicity
    print(result)
