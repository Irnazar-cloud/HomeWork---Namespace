calls = 0
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(string):
    count_calls()
    a = []
    a.extend([len(string), string.upper(), string.lower()])
    return a
def is_contains(string, *args):
    count_calls()
    list_to_search = args[0]
    match = False
    for i in list_to_search:
        if string.lower() == i.lower():
            match = True
            break
    return match
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)