candidates_input = input("Введите элементы массива (через пробел): ")
target_input = input("Введите целевое значение: ")
def array(candidates, target):
    candidates.sort()
    results = []
    def backtrack(start, path, target):
        if target == 0:
            results.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            backtrack(i + 1, path + [candidates[i]], target - candidates[i])
    backtrack(0, [], target)
    return results
candidates = list(map(int, candidates_input.split()))
target = int(target_input)
result = array(candidates, target)
print("Уникальные комбинации:", result)
