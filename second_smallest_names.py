class solution:
    def second_smallest(score_list):
        name = list()
        score = list()
        for index, value in enumerate(score_list):
            name.append(value[0])
            score.append(value[1])
        score_min = min(score)

        index_remove = list()
        for index, value in enumerate(score_list):
            if value[1] == score_min:
                index_remove.append(index)
        score_list = [v for i, v in enumerate(score_list) if i not in index_remove]
        print(score_list)
        
        name = list()
        score = list()
        for index, value in enumerate(score_list):
            name.append(value[0])
            score.append(value[1])
        score_second_min = min(score)
        
        name_result = list()
        for index, value in enumerate(score_list):
            if value[1] == score_second_min:
                name_result.append(value[0])
        name_result = sorted(name_result)
        #print('\n'.join(name_result))
        return name_result 
print(solution.second_smallest([['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]))
