import math

def solution(indices, K):
    answer = []
    all_fold = []
    num_ele_fold = math.ceil(len(indices)/K)

    mini_fold = []
    for index,element in enumerate(indices):
        mini_fold.append(element)
        if index % num_ele_fold == num_ele_fold-1 and index !=0:
            all_fold.append(mini_fold)
            not_mini_fold = [train for index_train, train in enumerate(indices) if train not in mini_fold]
            answer.append(mini_fold)
            answer.append(not_mini_fold)
            mini_fold = []
        elif index == len(indices)-1:
            all_fold.append(mini_fold)
            not_mini_fold = [train for index_train, train in enumerate(indices) if train not in mini_fold]
            answer.append(mini_fold)
            answer.append(not_mini_fold)
            mini_fold = []
    return answer

A = [1, 2, 3, 4, 5]
B = [1, 2, 3]
C = [1, 2, 3, 4, 5, 6, 7, 8]
K = 2
print(solution(A,K))
print(solution(B,K))
print(solution(C,3))
