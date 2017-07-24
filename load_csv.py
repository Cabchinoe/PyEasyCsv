#encoding=utf8
__author__ = 'Cabchinoe'
import csv
''' 
    @Author:cabchinoe@gmail.com

    Load a CSV file with lib csv

'''
class LoadCsv:
    def __init__(self,file_obj,has_field=True,
                 False_type=None,decoding='gb18030',encoding='utf8'):
        self.False_type = False_type
        self.decoding = decoding
        self.encoding = encoding
        self.file_obj = file_obj
        self.has_field = has_field
        self.data = []
        if self.has_field:
            self.__load_with_field()
        else:
            self.__load_without_field()

    def __load_without_field(self):
        reader = csv.reader(self.file_obj)
        for line in reader:
            line_data = []
            for i in line:
                line_data.append(self.__convert_func(i))
            self.data.append(line_data)

    def __load_with_field(self):
        reader = csv.DictReader(self.file_obj)
        for line in reader:
            _d = {}
            for k,v in line.items():
                k = self.__convert_func(k)
                v = self.__convert_func(v)
                _d[k] = v
            self.data.append(_d)


    def return_list(self):
        return self.data

    def __convert_func(self,x):
        if x is '':
            return self.False_type
        if isinstance(x, unicode):
            return x.encode(self.encoding)
        return x.decode(self.decoding,'replace').encode(self.encoding,'replace')

