def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    x = 0
    y = 0
    if a>0:
        x+=1
    if a<0:
        y+=1
    if b>0:
        x+=1
    if b<0:
        y+=1
    if c>0:
        x+=1
    if c<0:
        y+=1
    
    if x>y:
        print ('here are a lot of positive numbers')
    if x<y:
        print ('there are a lot of negative numbers')

    return x,y
print(main(2,4,6))