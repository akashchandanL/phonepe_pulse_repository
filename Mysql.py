# Creating connection with MySQL
# Connecting with SQL
mydb = sql.connect(host="localhost",
                   user="root",
                   password="9945484183mM@",
                   auth_plugin="mysql_native_password",
                   database= "Phonepe_pulse"
                  )
mycursor = mydb.cursor(buffered=True)

# Creating new database and tables
mycursor.execute("CREATE DATABASE Phonepe_pulse")

mycursor.execute("USE Phonepe_pulse")

# Creating agg_trans table
mycursor.execute("create table agg_trans (State varchar(100), Year int, Quarter int, Transaction_type varchar(100), Transaction_count int, Transaction_amount double)")

for i,row in df_agg_trans.iterrows():
    #here %S means string values 
    sql = "INSERT INTO agg_trans VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()
	
	
# Creating agg_user table
mycursor.execute("create table agg_user (State varchar(100), Year int, Quarter int, Brands varchar(100), Count int, Percentage double)")

for i,row in df_agg_user.iterrows():
    sql = "INSERT INTO agg_user VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    mydb.commit()
	
	
# Creating map_trans table
mycursor.execute("create table map_trans (State varchar(100), Year int, Quarter int, District varchar(100), Count int, Amount double)")

for i,row in df_map_trans.iterrows():
    sql = "INSERT INTO map_trans VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    mydb.commit()
	

# Creating map_user table
mycursor.execute("create table map_user (State varchar(100), Year int, Quarter int, District varchar(100), Registered_user int, App_opens int)")

for i,row in df_map_user.iterrows():
    sql = "INSERT INTO map_user VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    mydb.commit()

# Creating top_trans table
mycursor.execute("create table top_trans (State varchar(100), Year int, Quarter int, Pincode int, Transaction_count int, Transaction_amount double)")

for i,row in df_top_trans.iterrows():
    sql = "INSERT INTO top_trans VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    mydb.commit()
	
# Creating top_user table
mycursor.execute("create table top_user (State varchar(100), Year int, Quarter int, Pincode int, Registered_users int)")

for i,row in df_top_user.iterrows():
    sql = "INSERT INTO top_user VALUES (%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    mydb.commit()