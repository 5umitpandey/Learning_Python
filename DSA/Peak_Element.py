class Solution:
    def peakElement(self, arr):
        return self.findPeakElement(arr, 0, len(arr) - 1, len(arr))

    def findPeakElement(self, arr, low, high, n):
        mid = low + (high - low) // 2

        # Check if mid is a peak element
        if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
            return mid

        # Check left half
        if mid > 0 and arr[mid - 1] > arr[mid]:
            return self.findPeakElement(arr, low, mid - 1, n)

        # Check right half
        return self.findPeakElement(arr, mid + 1, high, n)
