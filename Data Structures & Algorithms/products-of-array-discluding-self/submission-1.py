class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProd=[1 for i in range(len(nums)+2)]
        postfixProd=[1 for i in range(len(nums)+2)]
        
        for i in range(0,len(nums),1):
            prefixProd[i+1]=prefixProd[i]*nums[i]

        for i in range(len(nums)-1,-1,-1):
            postfixProd[i+1]=postfixProd[i+2]*nums[i]
        
        result=[]

        print(prefixProd)
        print(postfixProd)
        for i in range(1,len(nums)+1,1):
            result.append(prefixProd[i-1]*postfixProd[i+1])
        
        return result
        
        
        
