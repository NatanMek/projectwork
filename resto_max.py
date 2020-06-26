def change_max(change):
    float(change)
    print(change//2, "da 2€")
    change = change % 2
    print(change // 1, "da 1€")
    change = change % 1
    print(change//50, "da 50 cent")
    change = change % 50
    print(change // 20, "da 20 cent")
    change = change % 20
    print(change // 10, "da 10 cent")
    change = change % 10
    print(change // 5, "da 5 cent")
    change = change % 5
    print(change // 2, "da 2 cent")
    change = change % 2
    print(change // 1, "da 1 cent")
    return change


change_max()