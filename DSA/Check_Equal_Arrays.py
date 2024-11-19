from collections import defaultdict

    def check(self, arr1, arr2):
        if len(arr1) != len(arr2):
            return False
        
        count_map = defaultdict(int)
        
        for i in range(len(arr1)):
            count_map[arr1[i]] += 1
            count_map[arr2[i]] -= 1
        
        for count in count_map.values():
            if count != 0:
                return False
        
        return True
