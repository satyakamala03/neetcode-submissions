class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A
        
        
        half = (len(A) + len(B)) // 2

        L, R = 0, len(A)
                
        while L <= R:
            M = (L + R)//2  # -> num elements from A
            i = M
            j = half - M

            Aleft = A[i - 1] if i > 0 else float('-inf')
            Bleft = B[j - 1] if j > 0 else float('-inf')
            Aright = A[i] if i < len(A) else float('inf')
            Bright = B[j] if j < len(B) else float('inf')

            if Aleft > Bright:
                R = M - 1
            elif Bleft > Aright:
                L = M + 1
            else: 
                if (len(A) + len(B))%2 != 0:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

        



        
