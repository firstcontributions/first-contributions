## Kadane’s Algorithm (Maximum Subarray Sum)

Kadane’s Algorithm is an efficient technique used to find the maximum sum of a contiguous subarray within a one-dimensional array of integers.

### Why Kadane’s Algorithm?
A brute-force approach checks all possible subarrays, which takes **O(n²)** time.  
Kadane’s Algorithm optimizes this by using a dynamic programming approach, reducing the time complexity to **O(n)**.

---

### Core Idea
At every index, we decide:
- Either extend the current subarray
- Or start a new subarray from the current element

This decision is based on whether adding the current element increases the sum.

---

### Algorithm Steps
1. Initialize two variables:
   - `currentSum` → stores the maximum subarray sum ending at the current index
   - `maxSum` → stores the maximum subarray sum found so far
2. Traverse the array from left to right.
3. For each element:
   - Update `currentSum` as the maximum of:
     - the current element
     - `currentSum + current element`
   - Update `maxSum` if `currentSum` is greater.
4. Return `maxSum`.

---

### Java Implementation

```java
public static int maxSubArray(int[] nums) {
    int currentSum = nums[0];
    int maxSum = nums[0];

    for (int i = 1; i < nums.length; i++) {
        currentSum = Math.max(nums[i], currentSum + nums[i]);
        maxSum = Math.max(maxSum, currentSum);
    }
    return maxSum;
}

