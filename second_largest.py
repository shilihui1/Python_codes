class solution:
    def second_largest(a):
        a_sorted = sorted(a)
        max_value = max(a)
        for index, value in enumerate(a):
            if value == max_value:
                a_sorted.pop()
        return max(a_sorted)
print(solution.second_largest([2, 3, 6, 6, 5]))
