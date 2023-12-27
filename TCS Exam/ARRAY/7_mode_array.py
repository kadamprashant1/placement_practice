from collections import Counter
import statistics
def find_mode(numbers):
   count = Counter(numbers)
   mode = [k for k,v in count.items() if  v== max(count.values())]
   #return int(''.join(map(str, mode)))
   return statistics.mode(numbers)

if __name__=="__main__":
    arr = input()
    arr = list(map(int,arr.split()))
    print(find_mode(arr))