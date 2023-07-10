# Способ 1: Построение структуры каждого элементы и сравнение их между собой.
def same_structure_as(original,other):
    
    # check for a list
    def is_array(elem):
        return isinstance(elem, list)      
        
    # building the element structure
    def view_deep(elem):
        
        if not is_array(elem):
            return 'not_arr'
         
        struct_elem = []
        
        for i in elem:
            if not is_array(i):
                struct_elem.append('not_arr')
            else:
                struct_elem.append(view_deep(i))
        
        return struct_elem

    return view_deep(original) == view_deep(other)     

# Способ 2: Решение через zip.
def same_structure_as(original, other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for p1, p2 in zip(original, other):
            if not same_structure_as(p1, p2):
                return False
        else:
            return True
    else: return not isinstance(original, list) and not isinstance(other, list)      
    
# Способ 3: Рефакторинг способа 1.
def same_structure_as(original,other):          
    def view_deep(elem):        
        if not isinstance(elem, list): return 'not_arr'         
        struct_elem = []
        for i in elem: 
            if not isinstance(i, list): struct_elem.append('not_arr')
            else: struct_elem.append(view_deep(i))        
        return struct_elem
    return view_deep(original) == view_deep(other)   
