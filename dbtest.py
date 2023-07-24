# import sqlite3
# conn=sqlite3.connect('pms.db')
# cur=conn.cursor()

# #def show_employees(self):
# conn=sqlite3.connect('pms.db')
# cur=conn.cursor()
# cur.execute("SELECT*FROM employee_details")
# data=[]
# for i in cur.fetchall():
#         context={}
#         context['eid']=i[0]
#         context['ename']=i[1]
#         context['dptid']=i[2]
#         context['designation']=i[3]
#         context['email']=i[4]
#         context['contact']=i[5]
#         context['address']=i[6]
#         data.append(context)
# print(data)    
# conn.commit()
# conn.close()




#cur.execute("create table employee_details(eid int ,ename varchar(30),dptid int,designation varchar(30),email varchar(30),contact int,address varchar(30))")
#cur.execute("create table attedance(dptid int ,dptname varchar(30),eid int,ename varchar(30),date datetime,timein datetime,timeout datetime)")
#cur.execute("create table sallary_details(eid int,dptid int,account_number varchar(30),pan varchar(30),base_sallary int )")


#from empdetails import Employee

#emp= Employee()
#emp.attendence(dptid=5,dptname='CS',eid=10,ename='udft',date='09-02-2023',timein='09:55',timeout='05:00')

# from empdetails import Employee

# emp=Employee()
# emp.salaryinsert(eid=15,dptid=5,account_number=123454,pan='23423534',base_sallary=234222)


# import sqlite3
# conn=sqlite3.connect('pms.db')
# cur=conn.cursor()
# #cur.execute("DELETE FROM ATTEDANCE")
# cur.execute("DELETE FROM SALLARY_DETAILS")
# conn.commit()

from empdetails import SalaryCalculaor
sc= SalaryCalculaor()