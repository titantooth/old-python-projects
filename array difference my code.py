def smallest_diff(a1, a2, target):
    sort_a1 = sorted(a1)
    sort_a2 = sorted(a2)
    target = target
    print(sort_a1)
    print(sort_a2)
    print(a1)
    print(a2)
    i = 0
    j = len(sort_a2) - 1
    answers =[]


    while i <= len(sort_a1) and j > 0 :
        current_differ = sort_a1[i] + sort_a2[j] - target
        smallest_differ = 0
        if current_differ == 0:
            answers.append('{0},{1}'.format(sort_a1[i],sort_a2[j]))
            print('the  answers are: {answers}'.format(answers=answers))
            j -=1
        else:
            if sort_a1[i] + sort_a2[j] < target:
                i += 1
                current_differ = sort_a1[i] + sort_a2[j] - target
                if current_differ in [1,2,3]:
                    answers.append('{0},{1}'.format(sort_a1[i], sort_a2[j]))
                    print('the closest answers are: {answers}'.format(answers=answers))
            elif sort_a1[i] + sort_a2[j] > target:
                j -= 1
                current_differ = sort_a1[i] + sort_a2[j] - target
                if current_differ in [1, 2, 3]:
                    answers.append('{0},{1}'.format(sort_a1[i], sort_a2[j]))
                    print('the closest answers are: {answers}'.format(answers=answers))






smallest_diff([5,8,1,15,2,3], [8,4,23,1,19,21], 20)