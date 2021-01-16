from itertools import groupby as gb
from operator import itemgetter as ig
string_list=['look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
def split_char(string_list):
    for i,j in gb(string_list,key=ig(0)):
        print(i)
        for k in j:
            print(k)
            

split_char(string_list)