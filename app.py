from empdetails import Employee, SalaryCalculaor
from flask import Flask, render_template,jsonify,request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/employee_signup', methods=['GET','POST'])
def emp_signup():
    if request.method=="POST":
        eid= request.form.get('eid')
        ename= request.form.get('ename')
        dptid= request.form.get('dptid')
        designation=request.form.get('designation')
        emailid=request.form.get('emailid')
        contact_no=request.form.get('contact_no')
        address=request.form.get('address')
        print(eid,ename,dptid)
        emp=Employee()
        emp.empinsert(eid=eid,ename=ename,dptid=dptid,designation=designation,email=emailid,contact=contact_no,address=address)
        return jsonify({'Message': "Sucessfully Fetched the data"})
    else:
        return render_template('signup.html')
    
@app.route('/employees',methods=['GET','POST'])
def show_employees():
    emp=Employee()
    data=emp.show_employees()
    return render_template('showemployees.html',employees=data) 

@app.route('/attendance',methods=['GET','POST'])
def attendance():
    if request.method=="POST":
        dptid=request.form.get("dptid")
        dptname=request.form.get("dptname")
        eid=request.form.get("eid")
        ename=request.form.get("ename")
        date=request.form.get("date")
        timein=request.form.get("timein")
        timeout=request.form.get("timeout")
        
        emp=Employee()
        emp.attendence(dptid=dptid,dptname=dptname,eid=eid,ename=ename,date=date,timein=timein,timeout=timeout)
        return jsonify({'Attendence':"Sucessfully inserted"})
    return render_template('attendence.html')
@app.route('/salary_details',methods=['GET','POST'])
def salarydetails():
     if request.method=='POST':
        eid=request.form.get("edi")
        dptid=request.form.get("dptid")
        acc_no=request.form.get("account_number")
        pan=request.form.get("pan")
        bs=request.form.get("base_sallary")
        emp=Employee()
        emp.salaryinsert(eid=eid,dptid=dptid,account_number=acc_no,pan=pan,base_sallary=bs)
        return jsonify({'Salarydetails':"Sucessfully inserted"})
     return render_template('salary.html')
        

@app.route('/payroll_release',methods=['GET','POST'])
def payrollrelease():
    if request.method=='POST':
        eid=request.form.get("empid")
        sc=SalaryCalculaor()
        total_sallary=sc.salarycalculation(eid=int(eid))
        context={'EmployeeID':eid,'TotalSalary':int(total_sallary)}
        return render_template('showsalary.html',data=context)
    else:
        return render_template('empid.html')



if __name__=='__main__':
    app.run(host='0.0.0.0',port=5050)


#emp= Employee()
#emp.empinsert(eid=5,ename='Jennie',dptid=1,designation='Manager', email='jen@gmail.com',contact=99829384,address='hyderabad')