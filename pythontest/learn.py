testDict = {"aaa": "bbb"}

def test( *args ) :
    if any(args):
        return 0
    else:
        return -1

test = test(testDict)

print(test)