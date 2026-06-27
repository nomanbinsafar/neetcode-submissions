class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        product=1
        zeroCnt=0
        for num in nums:
            if num==0:
                zeroCnt+=1

        if zeroCnt>1:
            return [0 for i in range(len(nums))]
        
        elif(zeroCnt==1):
            for num in nums:
                if num!=0:
                    product*=num
            for i in nums:
                if i==0:
                    res.append(product)
                else:
                    res.append(0)
            return res

        else:
            for num in nums:
                product*=num
            for i in nums:
                res.append(int(product/i))
            return res

            
        
        
