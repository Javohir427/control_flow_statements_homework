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
    x = 'there are a lot of positive numbers'
    y = 'there are a lot of negative numbers'
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
    
    

    return (x,y)
print(main(2,4,6))