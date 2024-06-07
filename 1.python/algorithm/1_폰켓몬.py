# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    selectNum = len(nums) / 2
    typeNum = len(set(nums)) 
    return selectNum if selectNum <= typeNum else typeNum

ex = [3,3,3,2,2,1,2,3,4,2]
print(solution(ex))