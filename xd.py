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
            
          
          print(j)
          dicts.update({objs[counter]:j})
          counter+=1
          
        elif counter==4:
            
            realobj.append(dicts)
            counter=0
            dicts={}
            dicts.update({objs[counter]:j})
            counter+=1
            

            
          
           
              
        

