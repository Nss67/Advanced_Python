import Import_Test_Name
print(Import_Test_Name)
print(__name__)
if __name__ == "__main__":
    print("this a main file")
    for i in dir():
        print(f"{i}: {help(i)}")




