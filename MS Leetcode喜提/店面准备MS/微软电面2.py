# coding=utf-8

# 给俩没sorted 的array, 每个array和俩array之间都有可能出现重复数字。要求merge这俩array 做到sort 和去重

def merge(A1, A2):
    return sorted(list(set(A1).union(set(A2))))

print merge([1,23,4423,55,1,2], [1,3,4,6,7,8,12,3,6])