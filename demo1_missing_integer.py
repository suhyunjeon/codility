
# Task description
# This is a demo task.
# 
# Write a function:
# 
# def solution(A)
# 
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# 
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# 
# Given A = [1, 2, 3], the function should return 4.
# 
# Given A = [−1, −3], the function should return 1.
# 
# Assume that:
# 
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# Complexity:
# 
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
# Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
# 
# https://app.codility.com/demo/results/demoZWDBUY-UJD/

def solution(A):
  missing = 1
  for i in sorted(A):
    if i == missing:
      missing += 1
    if i > missing:
      break
      
  return missing
  
print solution([1,4,5,45,2])
