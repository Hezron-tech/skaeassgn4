#generate an infinitecycle of elements from an iterable

list = [3, 5, 7, 9]
def infinite(list):
    for i in list:
        return infinite(list)

print(infinite(list))