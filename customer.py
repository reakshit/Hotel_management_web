import mysql.connector as MDS 




def new_cust(myconn, cID, name):
    sql="INSERT INTO CUSTOMERS(CustomerID,Name) VALUES('{}','{}')".format(cID,name)
    mycur = myconn.cursor()
    mycur.execute(sql)
    mycur.close()
    myconn.commit()

def update_cust(myconn, tID, cID, name):
    sql = "UPDATE CUSTOMERS             SET CustomerID = '{}',Name = '{}'                WHERE CustomerID = '{}'".format(cID, name, tID)

    mycur = myconn.cursor()
    mycur.execute(sql)
    mycur.close()
    myconn.commit()


def delete_cust(myconn, cID):
    sql="DELETE FROM CUSTOMERS WHERE CustomerID = '{}';".format(cID)
    mycur = myconn.cursor()
    mycur.execute(sql)
    mycur.close()
    myconn.commit()


def report_cust(myconn):
    sql="SELECT * FROM CUSTOMERS"
    mycur = myconn.cursor()
    mycur.execute(sql)
    records = mycur.fetchall()
    mycur.close()
    return records



