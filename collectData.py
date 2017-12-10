# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 22:50:36 2017

@author: ekrav
"""

# -*- coding: utf-8 -*-

import tweepy, sys, xlrd,json
from rtstock.stock import Stock
from json import JSONDecoder

def rest_query_ex1():
    book = xlrd.open_workbook("E:/Spring 17/DM/Assignments/HW3/ravi_ekambaram_hw3/HW3/Company Names.xlsx")
    first_sheet = book.sheet_by_index(0)
    cells = first_sheet.col_slice(colx=0, start_rowx=0, end_rowx=None)
    d = 0
    m = 0
    n = 0
    a = 0
    b = 0
    c = 0
    f1 = open('unbiased.txt', 'a+')
    f = open('biased.txt', 'a+')
    for cell in cells:
        stock = Stock('ABBV')
        for stock in stock.get_historical('2016-06-27', '2016-10-26'):
            mboolean = False
            nboolean = False
            dboolean = False
            aboolean = False
            bboolean = False
            cboolean = False
            rse = float(stock['High']) - float(stock['Low'])
            if float(stock['Close']) > float(stock['Open']):
                mboolean = True
                if float(stock['Close'])>100:
                    aboolean = True
                    json.dump(stock, f)

                    f.write('\n')
            else:

                if float(stock['Close']) > 100:
                    nboolean = True
                    if rse >1:

                        bboolean = True
                else:
                    dboolean = True
                    if rse> 1:
                        cboolean = True
            json.dump(stock, f1)
            f1.write('\n')
            if all([mboolean,aboolean]):
                a+=1
            elif all([mboolean,not aboolean]):
                m+=1
            elif all([nboolean,bboolean]):
                b+=1
            elif all([nboolean,not bboolean]):
                n+=1
            elif all([dboolean,cboolean]):
                c+=1
            elif all([dboolean,not cboolean]):
                d+=1
    f1.close()
    f.close()
    print a,b,c,d,m,n
    apirecall = float(m+a)/float(m+a+n+b)
    qprecision = float(a)/float(a+m)
    qrecall = float(a)/float(a+b+c)
    print 'API RECALL : ',apirecall
    print 'QUALITY PRECISION : ',qprecision
    print 'QUALITY RECALL : ',qrecall
rest_query_ex1()
