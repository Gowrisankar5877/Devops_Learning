try:
    print(10/0)
except TypeError:
    print("Type Error arises")
except ValueError:
    print("Value Error Arises")
except ZeroDivisionError:
    print("Zero Division Error")
finally:
    print("Always executes")