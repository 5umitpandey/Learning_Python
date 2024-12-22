#https://www.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1?page=1&difficulty=School,Basic&sortBy=submissions

def rotate(self, arr):
        if not arr:
            return arr
        rotated_arr = [arr[-1]] + arr[:-1]
        arr[:] = rotated_arr
