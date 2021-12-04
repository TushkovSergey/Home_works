nested_list = [
	['a', 'b', 'c', 'x'],
	['d', 'e', 'f'],
	[1, 2, 2, 5, 2, None],
    5,
    [5, [2, [2, 5]], 3, 'q']]

def convert_list(input_list):
    for item in input_list:
        if type(item) == list:
            for item in convert_list(item):
                yield item
        else:
            yield item

def myrange(input_list):
    list_numbers = len(input_list)
    cursor_list = 0
    while cursor_list < list_numbers:
        value = input_list[cursor_list]
        yield value
        cursor_list += 1

iterator = iter(myrange(list(convert_list(nested_list))))

while True:
    print(next(iterator))

