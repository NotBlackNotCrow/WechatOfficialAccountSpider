import os
import pandas as pd


lis_fakeid = []
lis_appmsg_token = []
lis_cookie = []

lines = open(r'WithToken\filter.txt').readlines()
count = 0
for line in lines:
    count += 1
    if count == 1:
        #print(line.split('&')[9][13:])
        lis_appmsg_token.append(line.split('&')[9][13:])
    if count == 10:
        lis_cookie.append(line[8:])
    if count == 14:
        print(line.split('&')[0][:11])
        lis_fakeid.append(line.split('&'))

    if line == '\n':
        print("################")
        count = 0