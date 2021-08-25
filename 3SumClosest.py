    def threeSumClosest(self, nums, target):
        res = []
        nums.sort()
        length = len(nums)
        closestSum = sys.maxsize;
        sum = 0
        for i in xrange(length-2): 
                
            if i>0 and nums[i]==nums[i-1]:
                continue 

            l, r = i+1, length-1
            while l<r:
                sum = nums[i] + nums[l] + nums[r]
                if (abs(target - sum) < abs(target - closestSum)) :
                    closestSum = sum;
                
                if (sum > target) :
                    r -= 1
                    
                else:
                    l += 1
        return closestSum






def threeSumClosest(self, nums, target):
        closest = 100000
        nums.sort()

        i=0 
        n=len(nums)

        closest_sum=sum(nums[:3])

        while i<n-2:
            left = i+1
            right = n-1 
            val1=nums[i]
            while left<right:
                val2=nums[left]
                val3=nums[right]

                search_val = val1+val2+val3
                temp = target-search_val

                if temp==0:
                    return search_val
                elif temp>0:
                    left+=1 
                else:
                    right-=1 

                if closest>abs(temp):
                    closest = abs(temp) 
                    closest_sum = search_val
            i+=1 

        return closest_sum 