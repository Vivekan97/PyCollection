def palin(n):
    initial = n.lower()
    initial = (initial.split(" "))
    initial1 = ""
    for i in initial:
        initial1 += i
    # print(initial1,type(initial1))
    final = initial1[::-1]
    # print(final,type(final))
    return initial1 == final

print(palin("Nurses Run"))