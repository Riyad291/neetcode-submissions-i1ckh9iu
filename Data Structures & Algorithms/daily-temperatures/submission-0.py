class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) # this is the result array of the day time to to have higher
        stack = [] #pair: [ temp, index ]

        for i, t in enumerate(temperatures): # in this loop we are tracing all the temperature one by one 
            while stack and t > stack[-1][0]: # here we see if the stack is empty and temperatur is bigger than previus one 
                stackT, stackInd = stack.pop() # we pop the temp and the index of form the staack
                res[stackInd] = (i - stackInd) # then subtrack the previus ind from the new to to cal the day
            stack.append([t, i]) # and the we append the temp and the index in the stack
        return res # at last we return the result array and Alhumdulliah may Allah accept me and give me baraka what i am learing insaAllah