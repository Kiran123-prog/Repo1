from flask import Flask,render_template,request, redirect
import re
from ip import features
app = Flask(__name__)


@app.route('/')
def front_page():
    return render_template("frontpage.html")
@app.route('/login')
def hello_world():
    return render_template("welcome.html")
db = {'admin':'admin','allan':'123'}
@app.route('/form_login',methods=['POST','GET'])
def login():
    name = request.form['username']
    pwd = request.form['password'] 
    if name not in db:
        return render_template('welcome.html',info='Invalid User')
    else:
        if db[name]!=pwd:
            return render_template('welcome.html',info='Invalid Password')
        else:
            return render_template('home.html',name=name)


@app.route('/scan',methods=['POST','GET'])
def scanning():
    
    if request.method == 'GET':
        ip = request.args.get('ip')
        print(ip)
        regex_pattern =r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
        result = bool( re.match( regex_pattern, str(ip)))
        print(result)
        if (result):
            print("Valid")
            a = [('Virtual Machine', '20.115.105.28', 'Linux'),('Virtual Machine', '20.115.105.27', 'Windows')]
            return render_template('scan.html',result=a)
        else:
            print("Invalid")  
            return render_template('home.html')  
@app.route('/details/<ip_address>',methods=['POST','GET'])

def ip(ip_address):
    ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",str(ip_address))
    print(ips)
    f=features()
    head = ('ip','HostName','ServerType','OS Version','Device Type')
    
    # if ("20.115.105.28" in ips) or ("20.115.105.27" in ips):
    f=features()
    print(f)
        
    return render_template('ip.html',result=ips,name=f)

    # return render_template('ip.html',result=ips,headings=head,f=f)


if __name__== '__main__':
    app.run(debug=True)
