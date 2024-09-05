def getProfitablePairs(profit, implementationCost):
    # Get the number of elements
    n = len(profit)
    
    # Create an empty list for storing net profit
    netProfit = []
    
    # Calculate net profit for each pair of profit and implementation cost
    for i in range(n):
        netProfit.append(profit[i] - implementationCost[i])
    
    count = 0
    
    # Check for profitable pairs
    for i in range(n):
        for j in range(i + 1, n):
            if netProfit[i] + netProfit[j] > 0:
                count += 1
    
    return count

 
if __name__ == '__main__':
    # For now, let's avoid using os.environ and OUTPUT_PATH to simplify the code
    # Import the os module if needed
    # import os

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

    # Print the result directly for simplicity (you can write to a file if needed)
    print(result)
