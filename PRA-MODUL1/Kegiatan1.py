def kurang(value1,value2):
    return value1 - value2

def kali(value1,value2):
    return value1 * value2

def bagi(value1,value2):
    return value1/value2

def add(value1,value2):
    return value1 + value2

def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        operator, left_operand, right_operand = node
        if operator == '+' :
            return add(tree(left_operand), tree(right_operand))
        elif operator == '-':
            return kurang(tree(left_operand),tree(right_operand))
        elif operator == '*' :
            return kali(tree(left_operand), tree(right_operand))
        elif operator == '/':
            return bagi(tree(left_operand), tree(right_operand))



# x = input("Enter operator : ")
# temp = ()
# temp2 = ()
# for i in range(0, 3):
#    y = input("masukkan : ")
#    temp += (y,)
# for i in range(0, 3):
#    y = input("masukkan : ")
#    temp2 += (y,)
# test = (x,(temp),(temp2))
# print(test)
    
expression_tree = ('*',('+',2,3),('-',5,1))

result = tree(expression_tree)

print(result)

