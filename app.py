from flask import Flask,request,redirect,render_template,url_for,flash,session,send_file
from flask_mysqldb import MySQL
from flask_session import Session
from otp import genotp
from cmail import sendmail
from cotp import cgenotp
import random
import os
from io import BytesIO
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from tokenreset import token
from tokenreset1 import token
import stripe
app=Flask(__name__)
app.secret_key='*cd@htl'
app.config['SESSION_TYPE']='filesystem'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Shannu786.'
app.config['MYSQL_DB']='CFA'
Session(app)
stripe.api_key='sk_test_51Mvx2WSDd4hbuBLCwovKUy0ALgUxeMqA4rMyj04Zp3k1P254ux83Xubb45hUtmJIfGnbUgRoFOeTeYqPY5Vvb6cx00VvcxDuZh'
mysql=MySQL(app)
@app.route('/')
def index():
    cursor=mysql.connection.cursor()
    cursor.execute('select cid,name,username,fund_required,funds_collected from campaign where status="Approved"')
    data=cursor.fetchall()
    return render_template('userdashboard.html',data=data)

@app.route('/signupregister',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        name=request.form['name']
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        mobile=request.form['mobile']      
        cursor=mysql.connection.cursor()
        cursor.execute('select username from register')
        data=cursor.fetchall()
        cursor.execute('SELECT email from register')
        edata=cursor.fetchall()
        if (username,) in data:
            flash('User already exists')
            flash('Create another Username')
            return render_template('signup.html')
        if (email,) in edata:
            flash('Email id already exists')
            return render_template('signup.html')
        cursor.close()
        otp=genotp()
        subject='Thanks for signingup to the application'
        body=f'Use this otp to register {otp}  '
        sendmail(email,subject,body)
        return render_template('otp.html',otp=otp,name=name,username=username,email=email,password=password,mobile=mobile)
    else:
        return render_template('signup.html')
    

@app.route('/login',methods=['GET','POST'])
def login():
    if session.get('user'):
        return redirect(url_for('userdashboard'))
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        cursor=mysql.connection.cursor()
        cursor.execute('select count(*) from register where username=%s and password=%s',[username,password])
        count=cursor.fetchone()[0]
        if count==0:
            flash('Invalid  password')
            return render_template('login.html')
        else:
            session['user']=username
            return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/admin',methods=['GET','POST'])
def admin():
    if request.method=='POST':
        name=request.form['name']
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        mobile=request.form['mobile']      
        cursor=mysql.connection.cursor()
        cursor.execute('select username from admin')
        data=cursor.fetchall()
        cursor.execute('SELECT email from admin')
        edata=cursor.fetchall()
        if (username,) in data:
            flash('User already exists')
            flash('Create another Username')
            return render_template('admin.html')
        if (email,) in edata:
            flash('Email id already exists')
            return render_template('admin.html')
        cursor.close()
        otp1=genotp()
        subject='Thanks for signingup to the application'
        body=f'Use this otp to register {otp1}'
        sendmail(email,subject,body)
        return render_template('otp1.html',otp1=otp1,name=name,username=username,email=email,password=password,mobile=mobile)
    else:
        return render_template('admin.html')

@app.route('/adminlogin',methods=['GET','POST'])
def adminlogin():
    if session.get('admin'):
        return render_template('admindashboard.html')
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        cursor=mysql.connection.cursor()
        cursor.execute('select count(*) from admin where username=%s and password=%s',[username,password])
        count=cursor.fetchone()[0]
        if count==0:
            flash('Invalid username or password')
            return render_template('adminlogin.html')
        else:
            session['admin']=username
            return redirect(url_for('admindashboard'))
    return render_template('adminlogin.html')

@app.route('/otp1/<otp1>/<name>/<username>/<email>/<password>/<mobile>',methods=['GET','POST'])
def otp1(otp1,name,username,email,password,mobile):
    if request.method=='POST':
        uotp=request.form['otp']
        if otp1==uotp:
            cursor=mysql.connection.cursor()
            lst=[name,username,email,password,mobile]
            query='insert into admin values(%s,%s,%s,%s,%s)'
            cursor.execute(query,lst)
            mysql.connection.commit()
            cursor.close()
            flash('Details registered')
            return redirect(url_for('adminlogin'))
        else:
            flash('Wrong otp')
            return render_template('otp1.html',otp1=otp1,name=name,username=username,email=email,password=password,mobile=mobile)


@app.route('/admindashboard')
def admindashboard():
    if session.get('admin'):
        return render_template('admindashboard.html')
    else:
        return redirect(url_for('adminlogin'))


@app.route('/create')
def home():
    if session.get('user'):
        return render_template('home.html')
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    if session.get('user'):
        session.pop('user')
        return redirect(url_for('index'))
    else:
        flash('already logged out!')
        return redirect(url_for('login'))
@app.route('/adminlogout')
def alogout():
    if session.get('admin'):
        session.pop('admin')
        return redirect(url_for('index'))
    else:
        flash('already logged out!')
        return redirect(url_for('adminlogin'))


@app.route('/allcampaigns')
def allcampaigns():
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT * from campaign')
    cids=cursor.fetchall()
    return render_template('allcampaigns.html',cids=cids)
@app.route('/otp/<otp>/<name>/<username>/<email>/<password>/<mobile>',methods=['GET','POST'])
def otp(otp,name,username,email,password,mobile):
    if request.method=='POST':
        uotp=request.form['otp']
        if otp==uotp:
            cursor=mysql.connection.cursor()
            lst=[name,username,email,password,mobile]
            query='insert into register values(%s,%s,%s,%s,%s)'
            cursor.execute(query,lst)
            mysql.connection.commit()
            cursor.close()
            flash('Details registered successfully')
            return redirect(url_for('login'))
        else:
            flash('Wrong otp')
            return render_template('otp.html',otp=otp,name=name,username=username,email=email,password=password,mobile=mobile)



@app.route('/forgotpassword',methods=['GET','POST'])
def forgot():
    if request.method=='POST':
        username=request.form['username']
        cursor=mysql.connection.cursor()
        cursor.execute('select username from register')
        data=cursor.fetchall()
        if (username,) in data:
            cursor.execute('select email from register where username=%s',[username])
            data=cursor.fetchone()[0]
            cursor.close()
            subject=f'Reset Password for {data}'
            body=f'Reset the password using-{request.host+url_for("createpassword",token=token(username,120))}'
            sendmail(data,subject,body)
            flash('Reset link sent to your mail')
            return redirect(url_for('login'))
        else:
            return 'Invalid username'
    return render_template('forgot.html')



@app.route('/campaign', methods=['GET', 'POST'])
def campaigns():
    if session.get('user'):
        if request.method == 'POST':
            name = request.form['name']
            description = request.form['description']
            fund = request.form['fund']
            dfile = request.files['file1']
            img_name=dfile.filename.split('.')
            if img_name[-1]!='jpg':
                return 'Incorrect Value for jpg'
            cid=cgenotp()
            img_filename=cid+'.jpg'
            dfile1 = request.files['file2']
            filename=dfile1.filename
            base_dir=os.path.dirname(os.path.abspath(__file__))
            img_path=os.path.join(base_dir, 'static/campaigns/')
            file_final=os.path.join(img_path,img_filename)
            dfile.save(file_final)
            try:
                cursor = mysql.connection.cursor()
                cursor.execute('INSERT INTO campaign (cid,name, username, description,fund_required,dfile,dname) VALUES (%s,%s,%s,%s,%s,%s,%s)', [cid,name,session.get('user'), description,fund,dfile1.read(),filename])
                mysql.connection.commit()
                cursor.close()
                flash('Submitted successfully')
                return redirect(url_for('index'))
            except Exception as e:
                flash(f'Error occurred: {e}')
                return redirect(url_for('index'))
        return render_template('userdashboard.html')
    else:
        return redirect(url_for('login'))





@app.route('/createpassword/<token>',methods=['GET','POST'])
def createpassword(token):
    try:
        s=Serializer(app.config['SECRET_KEY'])
        username=s.loads(token)['user']
        if request.method=='POST':
            npass=request.form['npassword']
            cpass=request.form['cpassword']
            if npass==cpass:
                cursor=mysql.connection.cursor()
                cursor.execute('update register set password=%s where username=%s',[npass,username])
                mysql.connection.commit()
                return 'Password reset Successfull'
            else:
                return 'Password mismatch'
        return render_template('newpassword.html')
    except:
        return 'Link expired try again'

@app.route('/viewfile/<cid>')
def viewfile(cid):
    if session.get('admin') or session.get('user'):
        cursor=mysql.connection.cursor()
        cursor.execute('select dname,dfile from campaign where cid=%s',[cid])
        data=cursor.fetchone()
        cursor.close()
        filename=data[0]
        bin_file=data[1]
        byte_data=BytesIO(bin_file)
        return send_file(byte_data,download_name=filename,as_attachment=False)
    else:
        return redirect(url_for('login'))            
@app.route('/approve/<cid>')
def approve(cid):
    if session.get('admin'):
        cursor=mysql.connection.cursor()
        cursor.execute("update campaign set status='Approved' where cid=%s",[cid])
        mysql.connection.commit()
        return redirect(url_for('allcampaigns'))
    else:
        return redirect(url_for('adminlogin'))
@app.route('/campaigndetails/<cid>')
def campaigndetails(cid):
    cursor=mysql.connection.cursor()
    cursor.execute('select cid,name,description from campaign where cid=%s',[cid])
    data=cursor.fetchone()
    return render_template('pageinfo.html',data=data)
@app.route('/donatenow/<cid>')
def donatenow(cid):
    cursor=mysql.connection.cursor()
    cursor.execute('select name from campaign where cid=%s',[cid])
    name=cursor.fetchone()[0]
    cursor.close()
    return render_template('Donate.html',cid=cid,name=name)
@app.route('/pay',methods=['POST'])
def pay():
    if session.get('user'):
        cid=request.form['cid']
        name=request.form['name']
        amount=request.form['amount']
        checkout_session=stripe.checkout.Session.create(
            success_url=request.host_url+url_for('success_pay',cid=cid,amount=amount),
            line_items=[
                {
                    'price_data': {
                        'product_data': {
                            'name': f'{name}',
                        },
                        'unit_amount': int(amount)*100,
                        'currency': 'inr',
                    },
                    'quantity': 1,
                },
                ],
            mode="payment",)
        return redirect(checkout_session.url)
    return redirect(url_for('index'))
@app.route('/success_pay/<cid>/<amount>')
def success_pay(cid,amount):
    cursor=mysql.connection.cursor()
    cursor.execute('select funds_collected from campaign where cid=%s',[cid])
    funds_collected=int(amount)+cursor.fetchone()[0]
    cursor.execute('update campaign set funds_collected=%s where cid=%s',[funds_collected,cid])
    mysql.connection.commit()
    flash('Donation received Successfully')
    return redirect(url_for('index'))



app.run(use_reloader=True,debug=True)   
