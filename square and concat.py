def square_digits(num):
    # Your code here
    a = []
    for i in str(num):

        a.append(str(int(i)**2))
    c= ''.join(a)
    return c



square_digits(456)