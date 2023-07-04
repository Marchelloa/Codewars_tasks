import time

tree = [0, 0, 0, 1, 3, 3, 2] 
#Решение на основе обхода с помощью while
def count_skills_while(tree: list[int], required):
    
    if not required: 
        return 0

    branch_name_included = []
    sort_list_name = sorted(required, reverse=True)
          
    for single_name in sort_list_name:
        prev_skill = tree[single_name]
        
        while single_name != 0 and single_name not in branch_name_included:
            branch_name_included.append(single_name)    
            single_name = prev_skill
            prev_skill = tree[single_name]

    return len(branch_name_included)

# Решение на основе рекурсивного обхода (медленнее чем while в несколько раз)
def count_skills(tree, required):
    
    if not required: 
        return 0
    
    total = 1
    branch_name_included = []
    sort_list_name = sorted(required, reverse=True)
         
    def count_branch(single_name):    
        nonlocal total, branch_name_included, tree
        prev_skill = tree[single_name]
        
        if single_name != 0 and single_name not in branch_name_included:
            branch_name_included.append(single_name)    
            total += 1
            count_branch(prev_skill)
        else:
            return 0

    for single_name in sort_list_name:
        count_branch(single_name)

    return total

def timer(func, amount_repeat, *args):
    """Замер выполнения разных способов"""
    start = time.perf_counter()
    for i in range(amount_repeat):
        func(*args)
    return time.perf_counter() - start

print('While: ', timer(count_skills_while, 10000, tree, {4, 3, 2} ))
print('Recursion: ', timer(count_skills, 10000, tree, {4, 3, 2} ))
