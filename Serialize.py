import json


class Serialize(object):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def __getitem__(self, key):
        if hasattr(self, key):
            return getattr(self, key)

    def parse(self):
        return dict(self)

    def get_attribute(self):
        for key in vars(self).keys():
            yield key

    def keys(self):
        if not hasattr(self, 'key'):
            return self.get_attribute()
        key = getattr(self, 'key')
        if not isinstance(key, list):
            return self.get_attribute()
        return key

    def serialize(self):
        return json.dumps(self.parse())


if __name__ == '__main__':
    a = Serialize(a=1, b=[1], key=['b'])
    print(a.parse())
    print(a.serialize())
