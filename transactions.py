import mysql.connector as MDS 
import room
import customer as cust

import arrow
from datetime import date


def check_in(myconn, id, no):
    fobj = open("dates.txt","w")
    sql="SELECT * FROM ROOMS WHERE Roomno = '{}'".format(no)
    mycur = myconn.cursor()
    mycur.execute(sql)
    rooms = mycur.fetchall()
    mycur.close()


    sql="SELECT * FROM CUSTOMERS WHERE CustomerID = '{}'".format(id)
    mycur = myconn.cursor()
    mycur.execute(sql)
    custs = mycur.fetchall()
    mycur.close

    if custs  and rooms:
        time = arrow.now().format('YYYY,MM,DD')
        global date_split
        date_split = time.split(",")
        text = id+"/"+time
        fobj.writelines([text])

        sql="UPDATE CUSTOMERS SET Room = '{}' WHERE CustomerID = '{}'".format(no,id)
        mycur = myconn.cursor()
        mycur.execute(sql)
        mycur.close

        occ='yes'
        sql="INSERT INTO TRANSACTION(CustomerID,Roomno,isOccupied) VALUES('{}','{}','{}')".format(id,no,occ)
        mycur = myconn.cursor()
        mycur.execute(sql)
        mycur.close
        myconn.commit()

    fobj.close()


def check_out(myconn, id, no):
    fobj = open("dates.txt","r")
    
    
    def numOfDays(date1, date2):
    #check which date is greater to avoid days output in -ve number
        if date2 > date1: 
            return (date2-date1).days
        else:
            return (date1-date2).days


    # Driver program
    dat = fobj.readlines()
    for i in range(len(dat)):
        a = dat[i].partition("/")
        if id in a[0]:
            global fdate1
            fdate1 = a[2]

    sql="SELECT * FROM ROOMS WHERE Roomno = '{}'".format(no)
    mycur = myconn.cursor()
    mycur.execute(sql)
    pri = mycur.fetchall()
    mycur.close
    fobj.close()

    final_date = fdate1.split(',')
    today = arrow.now().format('YYYY,MM,DD')
    today_date = today.split(",")
    date1 = date(int(final_date[0]),int(final_date[1]),int(final_date[2]))
    date2 = date(int(today_date[0]),int(today_date[1]),int(today_date[2]))
    days = numOfDays(date1,date2)

    tpri = days*float(pri[-1][-1])
    sql="UPDATE TRANSACTION SET isOccupied = '{}', price = {} WHERE CustomerID = '{}'".format("no",int(tpri),id)
    mycur = myconn.cursor()
    mycur.execute(sql)
    mycur.close

    sql="UPDATE CUSTOMERS SET Room = {} WHERE CustomerID = '{}'".format(000,id)
    mycur = myconn.cursor()
    mycur.execute(sql)
    mycur.close
    myconn.commit()

    

def report_tran(myconn):
    sql="SELECT * FROM TRANSACTION"
    mycur = myconn.cursor()
    mycur.execute(sql)
    records = mycur.fetchall()
    mycur.close()
    return records


