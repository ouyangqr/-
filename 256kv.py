from copy import copy


class Bucket(object):
    l = [None] * 257

    def __init__(self):
        self._table = copy(Bucket.l)

    def add(self, key, values):
        ascii_data = key.encode('utf8')
        t1 = self._recursion(ascii_data)
        t1[256] = values

    def _recursion(self, ascii_data):
        _len = len(ascii_data)
        t1 = self._table
        for i in ascii_data:
            i = int(i)
            if isinstance(t1[i], list):
                t1 = t1[i]
                continue
            t1[i] = copy(Bucket.l)
            t1 = t1[i]
        return t1

    def get(self, key):
        ascii_data = key.encode('utf8')
        # _len = len(ascii_data)
        t1 = self._table
        for i in ascii_data:
            t1 = t1[i]
            if not isinstance(t1, list):
                raise KeyError()
        return t1[256]


if __name__ == '__main__':
    b = Bucket()
    for j in range(1, 11):
        for i in range(ord('a'), ord('z')):
            b.add(chr(i)*j, chr(i+1))
