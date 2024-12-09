import time
for i in range(1, 101):
    time.sleep(0.1)
    print(f"( {"#"*i} ) {i}%", end="\r")

message = "( *** download is complete *** "
_string = str()
for x in range(3):
    _string = str()
    for i in message:
        _string += i
        print(_string, end="\r")
        time.sleep(0.1)
    _string = str()
    for y in message.upper():
        _string += y
        print(_string, end="\r")
        time.sleep(0.1)

print(_string)



