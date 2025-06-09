import sqlite3

SQL12 = sqlite3.connect("sql_table1.db") #sql12 can be renamed
con12 = SQL12.cursor() #con12 can be renamed, its a variable not a constant
con12.execute(""" 
             CREATE TABLE IF NOT EXISTS BUYERS1(
                 Buyers_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 Buyers_name TEXT,
                 Buyers_age INTEGER,
                 Product TEXT,
                 Product_price INTEGER                
)
""")

#.execute must be added to every major action
#if not exists to prevent code duplication
con12.execute("""
INSERT INTO BUYERS1("Buyers_name", "Buyers_age", "Product", "Product_price")
VALUES
("Andrew sanders",23,"Bike",20000),
("Qwen stacy",19,"Tablet",2000),
("Kate williams",20,"Laptop",5000),
("Eddie frank",40,"Tyres",1500),
("Jones mattes",38,"Car",40000),
("Carl patt",50,"Case",10000)
""")
SQL12.commit()

#.commit to run it, else it would not register(there must only be one .commit)