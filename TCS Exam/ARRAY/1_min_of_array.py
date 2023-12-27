from typing import List

def min_of_list(lst: List[int])->None:
    print(min(lst))

if __name__=="__main__":
    print("input:")
    ele = input()
    lst = list(map(int,ele.split()))
    min_of_list(lst)

