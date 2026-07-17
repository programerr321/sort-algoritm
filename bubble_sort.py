from typing import List


def bubble_sort(list: List[int]) -> List[int]:
    """
    Sorts a list using Bubble Sort algorithm

    :param list: The list to be sorted
    :type list: List[int]
    :return: The sorted list
    :rtype: List[int]
    """
    n = len(list)  #3
    for i in range(n): #i=0 ,1,2
        for j in range(0, n - i - 1): #0x
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

if __name__ == "__main__":
    
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]
    print(bubble_sort([3,1,2,2345,32545,56,245,65,345654,457]))
# [1,2,3]