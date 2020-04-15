def func():
    print("func() in one.py")

print("TOP LEVEL ONE.PY")

if __name__ == "__main__":
    print("one.py is being run direclty")
else:
    print("one.py has been imported")