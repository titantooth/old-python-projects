def descending_order(num):
    # Bust a move right here

    a = []
    for i in str(num):
        a.append(int(i))
    b =a.copy()
    b.sort(reverse=True)
    c = [str(i) for i in b]
    return "".join(c)


descending_order(1543453)