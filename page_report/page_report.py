#!/usr/bin/env python
from string import join
from string import find
from string import index
import sys


def cutter(line=str, line_no=int):
    http_index_to=find(line,'HTTP/')-1
    http_index_from=find(line,'http:')+7                   #### checks where http and HTTP will be found
    find_question_mark=find(line[0:http_index_to],'?')    #### checks if they are request send by http address
    if find_question_mark > -1:                           #### if they are deletes them
        http_index_to=find_question_mark
    if line[http_index_to-1] == '/':
        http_index_to-=1
    if http_index_to>-2 and http_index_from>6:
        return line[http_index_from:http_index_to]       #### if http is correct add them to list
    else:                                                           #### if not send information "Invalid..."
        return 'Invalid log lines: %s' %(line_no)

#### function "only_http" is deletes all information except the http address
def only_http(log_file):
    list_http = []
    line_no = 1
    file=open(log_file,'r')
    for line in file:
        list_http.append(cutter(line, line_no))
        line_no+=1
    file.close()
    return list_http

#### function "log_out" is count the number of repeats in the records
def log_out(list_http):
    http_dict = dict()
    for i in list_http:
        key=i
        if "Invalid" in key: 
            http_dict[key]= 0
        elif key in http_dict:
            http_dict[key] += 1
        else:
            http_dict[key] = 1
    return http_dict

if __name__ == "__main__":
    log = str(sys.argv[1])
    http_dict=log_out(only_http(log))   
    for i in [k for k, v in sorted(http_dict.iteritems(), key=lambda(k, v): (-v, k))]:     ### loop sort address first by number of repeats and secend lexicographically.
        if "Invalid" in i: 
            print ('"%s"' %i)
        else:
            print('"%s",%s' %(i,http_dict[i]))
    sys.exit()

