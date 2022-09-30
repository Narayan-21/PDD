# Creating a ListMaker by creating a context manager.

class ListMaker:
    def __init__(self, title, prefix = '- ', indent=3):
        self.title = title
        self.prefix = prefix
        self.indent = indent
        self.current_indent = 0
        print(title)
    def __enter__(self):
        self.current_indent += self.indent
        return self
    def __exit__(self, typ, val, tb):
        self.current_indent -= self.indent
        return False
    def print_item(self, arg):
        s = ' '*self.current_indent + self.prefix + str(arg)
        print(s)

with ListMaker('items') as lm:
    lm.print_item('Item-1')
    with lm:
        lm.print_item('SubItem-11')
        lm.print_item('SubItem-12')
    lm.print_item('Item-2')
    with lm:
        lm.print_item('SubItem-21')
        lm.print_item('SubItem-22')
