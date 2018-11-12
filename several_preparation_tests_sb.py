# Class to add element to dictionnary with unique keys


class UniqueDict(dict):
    def __setitem__(self, key, value):
        if key not in self:
            dict.__setitem__(self, key, value)
        else:
            raise KeyError("'" + key + "' Key already exists")


diction = UniqueDict()
print(diction)
diction.__setitem__("1", "val")
print(diction)
try:
    diction.__setitem__("1", "val2")
except KeyError as e:
    print(e)

