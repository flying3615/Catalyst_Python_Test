for i in range(1, 101):
    if i % 15 == 0:
        print("foobar"),
        continue
    if i % 3 == 0:
        print("foo"),
        continue
    if i % 5 == 0:
        print("bar"),
        continue
    print i,
