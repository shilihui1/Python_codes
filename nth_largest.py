class Solution:
    def kth_largest(input_list, k):
    # initialize the top_k list to first k elements and sort descending
        top_k = input_list[0:k]
        top_k.sort(reverse = True)

        for i in input_list[k:]:
            if i > top_k[-1]:
                top_k.pop() # remove the lowest of the top k elements
                top_k.append(i) # add the new element
                top_k.sort(reverse = True) # re-sort the list
        return top_k[-1] # return the kth largest

print(Solution.kth_largest([11, 2, 4, 4, 5, 6, 10, 8, -12], 3))
