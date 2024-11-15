while True:
    s = input()
    if s == '.': break
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i]) 
        elif s[i] == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        elif s[i] == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop() 
            else:
                stack.append(']')
                break
                     
    if len(stack) == 0 : print('yes')
    else: print('no')