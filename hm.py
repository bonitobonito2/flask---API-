from logging import info
from flask import Flask,render_template,url_for,redirect,request

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Zaalizaali2'
app.config['MYSQL_DB'] = 'facebook'

mysql = MySQL(app)

activatedAcc=0
@app.route("/", methods = ["POST","GET"])
def hello():
    if request.method == "POST":
      userDetails= request.form
      name  = userDetails['name']
      username = userDetails['username']
      age = userDetails['age']
      password = userDetails['password']
      
    #   cur.execute("INSERT INTO users(name,username,age,passwd) VALUES (%s,%s,%s,%s)",(name,username,age,password))
    #   mysql.connection.commit()
      cur = mysql.connection.cursor()
      cur.execute("SELECT name FROM USERS")
      counter1=""
      arr=[]
      for i in cur:
        for j in i:
            if j =="(" or j =="'" or j ==")":
                continue
            else:
                counter1+=j
                arr.append(counter1)
                counter1=""

      counter3 = 0
      counter2 = len(arr)
      for i in arr:
        counter2 = len(arr)
        if i == name:
            return render_template("index.html",already = "given product already exists, try another")
            break
            
        else:
           counter3+=1
      if counter2==counter3 and len(password)>8 :
                print("succses1")
                cur.execute("INSERT INTO users(name,username,age,passwd) VALUES (%s,%s,%s,%s)",(name,username,age,password))
                mysql.connection.commit()
                return render_template("index.html",already = "პროდუქტი დამატებულია")
      else: 
                
                 print(counter2,counter2,)
                 return render_template("index.html",already = "something went wrong")

      if arr == [] and len(password) >8 :
            print("succses2")
            cur.execute("INSERT INTO users(name,username,age,passwd) VALUES (%s,%s,%s,%s)",(name,username,age,password))
            mysql.connection.commit()
            return render_template("index.html",already = 'პროდუქტი დამატებულია')
         
    return render_template("index.html") 
global username
@app.route("/login",methods = ["POST","GET"])
def login():
    if request.method=="POST" :
         userDetails= request.form
         username = userDetails["username"]
         password = userDetails["password"]
         cur = mysql.connection.cursor()
         cur.execute("SELECT username FROM USERS WHERE passwd = '%s'"%(password))
         information = cur.fetchall()
         counter1 = ""
         for i in information:
            for j in i:
                if j == "(" or j == "'" or j == ")":
                    continue
                else:
                    counter1 += j
         if username == counter1 and counter1!="":
            cur.execute("SELECT *FROM USERS WHERE username = '%s'"%(username))
            informacia = cur.fetchall()
            informacia=list(informacia)
            return render_template("profile.html",name = informacia[0][0], username = informacia[0][1], age = informacia[0][2],password=informacia[0][3])
         elif username.__le__==0 or password.__le__==0:
              return render_template("login.html",user = username)
         else:
              
              return render_template("login.html",username=username,password=password)          
            
       
    return render_template("login.html")  



@app.route('/people',methods=["POST","GET"])
def people():
    if request.method=="POST":
        userdetails = request.form
        text = userdetails['delete']
        print(text)
        import mysql.connector
        db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "Zaalizaali2",
            database = "facebook"
        )

        runner = db.cursor()
        runner.execute("DELETE FROM USERS WHERE name='%s'"%(text))
        db.commit()

    while True:
        import mysql.connector
        db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "Zaalizaali2",
            database = "facebook"
        )

        runner = db.cursor()
        runner.execute("SELECT * FROM USERS")
        hm = runner.fetchall()
        objs = ['name','username','age','password']
        dicts = {}
        counter=0
        realobj = []
        counter2= 0
        for i in hm:
            for j in i:
                
                if counter<4:
                    
                
                 
                  dicts.update({objs[counter]:j})
                  counter+=1
                
                elif counter==4:
                    
                    realobj.append(dicts)
                    counter=0
                    dicts={}
                    dicts.update({objs[counter]:j})
                    counter+=1
        realobj.append(dicts)            
        return render_template('people.html',items = realobj)       



@app.route('/search',methods=["POST","GET"])
def search():
    dictInlist=[]
    if request.method == "POST":
        information = request.form
        productName = information['search']
        print(productName)
        import mysql.connector
        db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "Zaalizaali2",
            database = "facebook"
        )

        runner = db.cursor()
        runner.execute("SELECT * FROM USERS WHERE name LIKE '%s'"%(productName))
        print(runner)
        row = runner.fetchall()
        objs = ['name','username','age','password']
        row = list(row) 
        if row ==[]:
            return render_template('search.html',erorr= productName)
        else:    
             dictInlist += [
            {objs[0]:row[0][0],objs[1]:row[0][1],objs[2]:row[0][2],objs[3]:row[0][3]
            }
        ]
        return render_template('search.html',items = dictInlist)
       
        print(dictInlist)

    return render_template('search.html')    

        
       
   
    

          


          
     


    
if __name__=="__main__":
    app.run(debug=True)

