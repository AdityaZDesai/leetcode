def answer(input):
    left = 0
    right = len(input) - 1
    result = []
    while left != right:
        print(left, right)
        if input[left] < input[right]: 
            result.append(input[left] * (right - left))
            left += 1
        else:
            result.append(input[right] * (right - left))
            right -= 1

    return max(result)


print(answer([1,1]))
                                                                                   