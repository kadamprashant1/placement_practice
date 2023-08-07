#find count of each number in string and say it
#we solve it by just unordered map in cpp is given below
#IMP#
#%To determine how you “say” a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.%#
# here we are using //recursive approach// is asked and required for this code
class Solution:
  def countAndSay(self, n: int) -> str:
    ans = '1'

    for _ in range(n - 1):
      nxt = ''
      i = 0
      while i < len(ans):
        count = 1
        while i + 1 < len(ans) and ans[i] == ans[i + 1]:
          count += 1
          i += 1
        nxt += str(count) + ans[i]
        i += 1
      ans = nxt

    return ans

k =8
obj = Solution()
print(obj.countAndSay(k))
    