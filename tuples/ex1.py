def tuple_demo():

    # 1️⃣ Creating Tuples
    t1 = (10, 20, 30, 40)
    t2 = (1, "Python", 3.5, True)

    print("Tuple 1:", t1)
    print("Tuple 2 (mixed data types):", t2)

    # 2️⃣ Accessing Elements
    print("First element:", t1[0])
    print("Last element:", t1[-1])

    # 3️⃣ Slicing
    print("Sliced tuple (1:3):", t1[1:3])

    # 4️⃣ Length
    print("Length of tuple:", len(t1))

    # 5️⃣ Looping
    print("Looping through tuple:")
    for i in t1:
        print(i)

    # 6️⃣ Concatenation
    t3 = t1 + (50, 60)
    print("After concatenation:", t3)

    # 7️⃣ Repetition
    print("Tuple repeated twice:", t1 * 2)

    # 8️⃣ Membership
    print("Is 20 in tuple?", 20 in t1)

    # 9️⃣ Count and Index
    t4 = (1, 2, 2, 3, 4)
    print("Count of 2:", t4.count(2))
    print("Index of 3:", t4.index(3))

    # 🔟 Single Element Tuple
    single = (5,)
    print("Single element tuple:", single)

    # 1️⃣1️⃣ Immutable Example
    try:
        t1[0] = 100
    except TypeError as e:
        print("Error (Tuple is immutable):", e)

tuple_demo()