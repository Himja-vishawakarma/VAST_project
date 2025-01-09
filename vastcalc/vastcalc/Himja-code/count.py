

def count(a, b):
    count = 0
    for item in a:
        if item == b:
            count += 1
    return count


a = "himjavishwakarma"
b = "a"
print(count(a, b))