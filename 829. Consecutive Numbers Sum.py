# The thought process goes like this- Given a number N, we can possibly write it as a sum of 2 numbers, 3 numbers, 4 numbers and so on. 
# Let's assume the fist number in this series be x. Hence, we should have
# x + (x+1) + (x+2)+...+ k terms = N
# kx + k*(k-1)/2 = N implies
# kx = N - k*(k-1)/2
# So, we can calculate the RHS for every value of k and if it is a multiple of k then we can construct a sum of N using k terms starting from x.
# Now, the question arises, till what value of k should we loop for? That's easy. In the worst case, RHS should be greater than 0. That is
# N - k*(k-1)/2 > 0 which implies
# k*(k-1) < 2N which can be approximated to
# k*k < 2N ==> k < sqrt(2N)
# Hence the overall complexity of the algorithm is O(sqrt(N))

# PS: OJ expects the answer to be 1 greater than the number of possible ways because it considers N as being written as N itself. 

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        count = 1;
        for k in range(2, int(sqrt(2 * N ))+1):
            if not ( N - ( k * ( k - 1 )/2) ) % k:
                count += 1
        return count
