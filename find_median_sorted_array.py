def find_median_sorted_arrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        px = (low + high) // 2
        py = (x + y + 1) // 2 - px

        maxLX = float('-inf') if px == 0 else nums1[px - 1]
        minRX = float('inf') if px == x else nums1[px]

        maxLY = float('-inf') if py == 0 else nums2[py - 1]
        minRY = float('inf') if py == y else nums2[py]

        if maxLX <= minRY and maxLY <= minRX:
            if (x + y) % 2 == 0:
                return (max(maxLX, maxLY) + min(minRX, minRY)) / 2
            else:
                return max(maxLX, maxLY)
        elif maxLX > minRY:
            high = px - 1
        else:
            low = px + 1

# Example usage
nums1 = [1, 3]
nums2 = [2]

median = find_median_sorted_arrays(nums1, nums2)
print("Median:", median)