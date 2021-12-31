class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        remainder = 0
        for length_N in range(1,K+1):
            remainder = (remainder*10+1) % K

            if remainder == 0:
                return length_N
        return -1


'''
Why can we discard the previous number and can just keep track of the remainders?
Take k = 17 as an example, and let's just consider one random case with n = 111.
The remainder will be 9: 111 % 17 = (6 * 17 + 9) % 17 = 9. Notice how 6 * 17 can be just ignored here and does not influence the remainder itself.
The next n will be 1111 * 10 + 1 = 11111. If we replace 1111 with 6 * 17 + 9, we get n = (6 * 17 + 9) * 10 + 1. Let's open the brackets: [6 * 17 * 10] + [9 * 10] + [1]. So we need to figure out the remainder of this whole number that consists of three sums. But 6 * 17 * 10 already has a k in it, 6 * 10 of them in fact. So we can just take 6 * 17 * 10 and ignore it completely, and then we're left with previous remainder 9 in place of the old number 111, so now 9 * 10 + 1 is what we need to be divisible by 17.
If you're unsure why we can get away with ignoring part of the sum that is divisible by k, consider a modulo of any sum. For example, what's remainder of (5 + 2 + 1) % 3?
We can just calculate the sum in the brackets and find the modulo of the result:
5 + 2 + 1 = 8
8 % 3 = 2
But we can also get to 2 by considering modulo of each of the numbers in the sum:
5 % 3 = 2
2 % 3 = 2
1 % 3 = 1
If you sum them up,
2 + 2 + 1 = 5
It's bigger than 3, so we need to modulo it one last time
5 % 3 = 2
And you get to the same modulo of 2.
So modulo of sum (a + b + c) % k = ([a % k] + [b % k] + [c % k]) % k

'''
