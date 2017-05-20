def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    a_score = 0
    b_score = 0
    a = (a0, a1, a2)
    b = (b0, b1, b2)
    for i in range(3):
        if a[i] > b[i]:
            a_score += 1 
        elif a[i] < b[i]:
            b_score += 1
    print(a_score, b_score)
result = solve(5, 6, 7, 3, 6, 10)
