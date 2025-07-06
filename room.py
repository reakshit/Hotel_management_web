import mysql.connector as MDS 



def add_room(myconn, roomno, roontype, roompri):
    sql="INSERT INTO ROOMS VALUES('{}','{}',{})".format(roomno,roontype,roompri)
    mycur = myconn.cursor()
    mycur.execute(sql)
    mycur.close()
    myconn.commit()


def update_rooom(myconn, uroom, roomno, roontype, roompri):
    sql = "UPDATE ROOMS             SET Roomno = '{}',                 RoomType = '{}',                 RoomPrice = {}                 WHERE Roomno = '{}'".format(roomno, roontype, roompri, uroom)
    mycur = myconn.cursor()
    mycur.execute(sql)
    mycur.close()
    myconn.commit()


def delete_room(myconn, roomno):
    sql="DELETE FROM ROOMS WHERE Roomno = '{}';".format(roomno)
    mycur = myconn.cursor()
    mycur.execute(sql)
    mycur.close()
    myconn.commit()

def report_room(myconn):
    sql="SELECT * FROM ROOMS"
    mycur = myconn.cursor()
    mycur.execute(sql)
    records = mycur.fetchall()
    mycur.close()
    return records


