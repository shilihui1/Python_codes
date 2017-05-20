def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    a = (a0, a1, a2)
    b = (b0, b1, b2)
    score = [1 if x > y else 0 if x == y else -1 for x, y in zip(a, b)]

    print(score.count(1), score.count(-1))
result = solve(5, 6, 7, 3, 6, 10)
