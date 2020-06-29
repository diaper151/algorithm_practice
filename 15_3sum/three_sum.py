class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        f={}
        for i in nums:
            f[i]=f.get(i,0)+1
            
        n=sorted(f)
        a=[]
        for i,I in enumerate(n):
            if not I:
                if f[I]>2:
                    a.append((0,0,0))
            elif f[I]>1 and -2*I in f:
                a.append((I,I,-2*I))
            if I<0:
                t=-I
                l=bisect_left(n, t-n[-1], i+1)
                r=bisect_right(n, t//2, l)
                for J in n[l:r]:
                    K=t-J
                    if K in f and K!=J:
                        a.append((I,J,K))
        return a