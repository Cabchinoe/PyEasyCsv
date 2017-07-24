# encoding=utf8
__author__ = 'Cabchinoe'
import csv, StringIO

'''
    @Author:cabchinoe@gmail.com
    version:0.3
    Make a CSV file with lib csv

    data: list or tuple type like [[...],[...],[...],..] or ((...),(...),(...),...) or complex
    None_type: define what a None type value to write into csv
    exclude_type: types in this tuple will not decoded or encoded
    decoding & encoding: define the charset to decode and encode
'''


class ExportCsv:
    def __init__(self, data, None_type='', exclude_type=(), decoding='utf8', encoding='gb18030'):
        self.None_type = None_type
        self.__exclude_type = [int, long, float,]
        self.exclude_type = exclude_type
        if len(self.exclude_type) != 0:
            self.__exclude_type.extend(list(self.exclude_type))
        self.decoding = decoding
        self.encoding = encoding
        self.data = data
        self.IO = StringIO.StringIO()
        self.__export()

    def return_body(self):
        self.IO.seek(0)
        return self.IO.read()

    def return_IOHandler(self):
        self.IO.seek(0)
        return self.IO


    def __export(self):
        try:
            self.IO.seek(0)
            writer = csv.writer(self.IO)
            res = []
            for i in self.data:
                res.append(map(self.__convert_func, i))
            writer.writerows(res)
        except Exception as e:
            print 'Export err', str(e)

    def __convert_func(self, x):
        if isinstance(x, unicode):
            return x.encode(self.encoding, 'replace')
        if x is None:
            return self.None_type
        if type(x) in self.__exclude_type:
            return x
        return x.decode(self.decoding, 'replace').encode(self.encoding, 'replace')
