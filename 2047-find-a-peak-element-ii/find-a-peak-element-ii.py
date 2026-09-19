class Solution(object):
    def max_index(self,mat,n,col):
        max = -1
        index = -1
        for i in range(n):
            if mat[i][col] > max :
                max = mat[i][col]
                index = i
        return index
    def findPeakGrid(self, mat):
        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m - 1
        while( low <= high ):

            mid = ( low + high ) // 2
            max_row = self.max_index(mat,n,mid)

            left = mat[max_row][mid - 1] if mid - 1 >= 0 else -1
            right = mat[max_row][mid + 1] if mid + 1 < m else -1

            if mat[max_row][mid] > left and mat[max_row][mid] > right :
                return [max_row , mid]
            elif mat[max_row][mid] < left :
                high = mid - 1
            else :
                low = mid + 1
        



        