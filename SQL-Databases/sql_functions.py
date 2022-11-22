import mysql.connector
from mysql.connector import Error # import Error function separately to have easy access to it

# ------------------------- Connecting to MySQL Server to get Access to all DBs
def create_server_connection(host_name, port_name, user_name, user_password): # establish a connection to that server.
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            port = port_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
        return connection
    except Error as err:
        print(f"Error: '{err}'")
        return None

# ------------------------- Show Available Databases based on the connection you established
def show_databases(connection):
    mycursor = connection.cursor(buffered=True)
    list_of_dbs = []
    try:
        mycursor.execute("SHOW DATABASES")
        for database_tuple in mycursor:
            list_of_dbs.append(database_tuple[0])
    except Error as err:
        print(f"Error: '{err}'")
    return list_of_dbs

# ------------------------- Check is there is a particular Database based on the connection you established
def check_database(connection,db_name_check):
    mycursor = connection.cursor(buffered=True)
    try:
        mycursor.execute("SHOW DATABASES")
        for database_tuple in mycursor:
            database_name = database_tuple[0]
            if(database_name == db_name_check):
                print("We have this Database")
                break
        else:
            print("No such a Database")
    except Error as err:
        print(f"Error: '{err}'")
    return None

# ------------------------- Create a Database and Check if already exists based on the connection you established
def create_database(connection,new_db_name):
    mycursor = connection.cursor(buffered=True)
    try:
        mycursor.execute("SHOW DATABASES")
        for database_tuple in mycursor:
            database_name = database_tuple[0]
            if(database_name == new_db_name):
                print("We have this Database")
                break
        else:
            try:
                mycursor.execute("CREATE DATABASE "+new_db_name)
                print("Database created successfully")
            except Error as err:
                print(f"Error: '{err}'")
    except Error as err:
        print(f"Error: '{err}'")
    return None

# ------------------------- Delete a Database and Check if exists based on the connection you established
def delete_database(connection,db_name):
    mycursor = connection.cursor(buffered=True)
    try:
        mycursor.execute("SHOW DATABASES")
        for database_tuple in mycursor:
            database_name = database_tuple[0]
            if(database_name == db_name):
                try:
                    mycursor.execute("DROP DATABASE "+db_name)
                    print("Database deleted successfully")
                except Error as err:
                    print(f"Error: '{err}'")
        else:
            print("No such a Database")
    except Error as err:
        print(f"Error: '{err}'")
    return None

# ------------------------- Connecting to MySQL Server in a particular Database
def db_connection(host_name, port_name, user_name, user_password, db_name): # establish a connection to that server.
    create_server_connection(host_name, port_name, user_name, user_password)
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            port = port_name,
            user=user_name,
            passwd=user_password,
            database=db_name # <---- the only difference is here to the create_server_connection function
        )
        print("Connection successful to "+db_name)
        return connection
    except Error as err:
        print(f"Error: '{err}'")
        return None
    
# ------------------------- Query Execution Function for Feching
# You must fetch all rows for the current query before executing new statements using the same connection.
def execute_query_fetch(connection, query):
    mycursor = connection.cursor()
    try:
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        return(myresult)
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
        return None

# ------------------------- Query Execution Function for Commiting
# The commit() method is one among the various methods in Python which is used to make the database transactions.
def execute_query_commit(connection, query):
    mycursor = connection.cursor()
    try:
        mycursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
        return None