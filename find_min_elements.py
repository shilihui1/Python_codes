class solution:
    def find_min_elements(a):
        a_min = min(a)

        #index_min = list()
        index_min = []
        for key, value in enumerate(a):
            if value == a_min:
                index_min.append(key)
        return index_min
print(solution.find_min_elements([1, 2, 1, 4, 5]))
