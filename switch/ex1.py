def switch_example(value):
    match value:
        case 1:
            print("You selected One")
        case 2:
            print("You selected Two")
        case 3:
            print("You selected Three")
        case _:
            print("Invalid choice")

switch_example(2)