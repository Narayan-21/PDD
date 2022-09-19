# Cities Example
class Cities:
    def __init__(self):
        self._cities = ['Paris','Mumbai','Goa','Tokyo','Rome','Berlin','Moscow','New York','London']
    def __len__(self):
        return len(self._cities)
    def __iter__(self):
        return self.CityIterator(self)
    def __getitem__(self,s):
        return self._cities[s]
    class CityIterator:
        def __init__(self, city_obj):
            self._city_obj = city_obj
            self._index = 0
        def __iter__(self):
            return self
        def __next__(self):
            if self._index >= len(self._city_obj):
                raise StopIteration
            else:
                item = self._city_obj._cities[self._index]
                self._index += 1
                return item
