calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    stroka = str(string)
    result = (len(stroka), stroka.upper(), stroka.lower())
    count_calls()
    return result


def is_contains(string, list_to_seach):
    string = str(string).lower()
    list_to_seach = list(list_to_seach)
    count_calls()
    for i in range(len(list_to_seach)):
        if str(list_to_seach[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result


print(string_info('Internet'))
print(string_info('cocunber'))
print(is_contains('Urban', ['ban', 'urBAn']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
