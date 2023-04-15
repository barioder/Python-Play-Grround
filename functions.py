our_list = []
def push (times):
    for each in times:
        our_list.append("*")
        our_list.append(each)
    
    print(our_list)


value = range(1, 8)
print(value)
print(type(value))
push(value)