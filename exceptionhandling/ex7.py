try:
    f = open("test.txt", "r")
    print(f.read())
except:
    print("File not found!")
finally:
    print("Closing program...")