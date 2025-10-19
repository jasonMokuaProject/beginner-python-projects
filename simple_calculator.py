import operator
user_input = list(input("Enter two numbers: ").split(" "))

operation_used = input("enter the operation: ")

opp = {
    "+":operator.add,
    "-":operator.sub,
    "*":operator.mul,
    "/":operator.truediv


}

print(f"{user_input[0]}  {operation_used}  {user_input[1]} = {opp[operation_used](int(user_input[0]),int(user_input[1]))}")