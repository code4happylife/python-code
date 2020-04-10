cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the reverse alphabetical list:")
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)

print("\nShows the usage of sorted() and sorted(,reverse=True)")

num = [18, 2, 3, 8, 9, 10]
print("\nHere is the original number list:")
print(num)

print("\nHere is the sorted number list:")
print(sorted(num))

'''
    Find out two numbers from num which add up to 'target'
'''


def solution(nums, target):
    if len(nums) < 2:
        return
    else:
        for i in range(0, len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j, nums[i], nums[j]]


print(solution(num, 17))


'''
    New solution
'''


def solution_new(nums, target):
    if len(nums) < 2:
        return
    else:
        dict_test = {}
        for i in range(0, len(nums)):
            findout = target-nums[i]
            if findout not in dict_test:
                dict_test[nums[i]] = i
            else:
                return dict_test[findout], i, findout, nums[i]


print(solution_new(num, 17))
