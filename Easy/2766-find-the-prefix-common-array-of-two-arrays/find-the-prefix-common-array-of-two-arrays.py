class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        # n=len(A)
        # C=[]
        # seen=set()
        # common_count=0

        # for i in range(n):
        #     if A[i] in seen:
        #         common_count+=1
        #     else:
        #         seen.add(A[i])
            
        #     if B[i] in seen:
        #         common_count+=1
        #     else:
        #         seen.add(B[i])


        n=len(A)
        seen_A=set()
        seen_B=set()
        C=[]
        
        for i in range(n):
            seen_A.add(A[i])
            seen_B.add(B[i])

            common_count= len(seen_A.intersection(seen_B))
            C.append(common_count)

        return C


            
                


        
                    
        