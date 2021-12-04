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

class My_iterator:
    def __init__(self, input_list):
        self.input_list = input_list
        self.list_numbers = len(self.input_list)
        self.cursor_list = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor_list == self.list_numbers - 1:
            raise StopIteration
        self.cursor_list += 1
        self.value = self.input_list[self.cursor_list]
        return self.value


MyClass = iter(My_iterator(list(convert_list(nested_list))))
while True:
    print(next(MyClass))