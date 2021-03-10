from pymysql import *
def getdata():
    con=connect(host='localhost',database='world',user='root',password='root')
    curs=con.cursor()
    query="""select * from world.city
            where Name='kalyan';"""
    curs.execute(query)
    res=curs.fetchone()
    curs.close()
    con.close()
    return res
result=getdata()
print(result)