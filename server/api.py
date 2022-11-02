from multiprocessing import connection
from flask import Flask
from flask_mysqldb import MySQL
from dotenv import load_dotenv
load_dotenv()
import os
from flask_cors import CORS

#-------------------------------------------------------------------------------------------
# MYSQL queries
#-------------------------------------------------------------------------------------------

app = Flask(__name__)
cors = CORS(app)
app.config['MYSQL_HOST'] = '159.223.91.38'
app.config['MYSQL_USER'] = 'yujing'
app.config['MYSQL_PASSWORD'] = 'AVNS_tsp5nuC_MhlRP0_cIVV'
app.config['MYSQL_DB'] = 'ICT3x03'
app.config['MYSQL_PORT'] = 25060
mysql = MySQL(app)

#insert,update,delete queries (no data retrival)
def db_query(sql):
    cursor = mysql.connection.cursor()
    cursor.execute(sql)
    mysql.connection.commit()
    cursor.close()

#fetch all
def db_query_fetchall(sql):
    cursor = mysql.connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    return data

#fetch one
def db_query_fetchone(sql):
    cursor = mysql.connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    mysql.connection.commit()
    cursor.close()
    return data

#-------------------------------------------------------------------------------------------
# MYSQL query statements
#-------------------------------------------------------------------------------------------

def get_all_laptop():
    return "SELECT * FROM LaptopInfo"

def get_cartItemsInfo(userId):
    return f"SELECT l.laptopName, l.imageUrl, l.price, c.cartItemId, c.quantity, c.cartId FROM LaptopInfo as l join CartItems as c on c.laptopId = l.laptopId where c.cartId = '{userId}'"

def get_account(email=None, pk=None):
    get_account_parameter = pk if pk else email
    return f"SELECT * FROM UserInfo WHERE {'userId' if pk else 'email'} = '{get_account_parameter}'"

def insert_new_user(input_name,input_email,hashed_password):
    return f"INSERT INTO UserInfo (username, email, password) VALUES('{input_name}', '{input_email}', '{hashed_password}')"

def insert_cartItem(userId, laptopId, quantity):
    return f"INSERT INTO CartItems (cartId, laptopId, quantity) VALUES('{userId}', '{laptopId}', '{quantity}')"

def update_verification_status(email):
    return f"UPDATE UserInfo SET verification_status = 1 WHERE email = '{email}'"

def update_password(newPwd,email):
    print(email)
    return f"UPDATE UserInfo SET password = '{newPwd}' WHERE email = '{email}'"

def update_username(newUsername, email):
    return f"UPDATE UserInfo SET username = '{newUsername}' WHERE email = '{email}'"

def update_email(newEmail, email):
    return f"UPDATE UserInfo SET email = '{newEmail}' WHERE email = '{email}'"
def update_cartItem_quantity(newQuantity,cartItemId):
    return f"UPDATE CartItems SET quantity = '{newQuantity}' WHERE cartItemId = '{cartItemId}'"

def delete_cartItem(cartItemId):
    return f"DELETE from CartItems where cartItemId = '{cartItemId}'"

def get_account_id(email):
    return f"SELECT userId FROM ICT3x03.UserInfo WHERE email = '{email}'"

def insert_cartid_userid (userId):
    return f"INSERT INTO Cart (cartId, userId) VALUES('{userId}','{userId}')"

#-------------------------------------------------------------------------------------------
# MYSQL logging section 
#-------------------------------------------------------------------------------------------

def register_logging (user_id, user_username, user_email, verification_status, registered_date, last_login, ip_address, country, failed_login_attempts, successful_password_reset, attempt_password_reset): 
	return f"INSERT INTO logging (user_id, user_username, user_email, verification_status, registered_date, last_login, ip_address, country, failed_login_attempts, successful_password_reset, attempt_password_reset) VALUES ('{user_id}', '{user_username}', '{user_email}', '{verification_status}', '{registered_date}', '{last_login}', '{ip_address}', '{country}', '{failed_login_attempts}', '{successful_password_reset}', '{attempt_password_reset}')"

def register_updatestatus_logging (user_email): 
	return f"UPDATE logging SET verification_status = 1 WHERE user_email = '{user_email}'"

def login_updatestatus_logging (user_email,timestamp): 
	return f"UPDATE logging SET last_login = '{timestamp}' WHERE user_email = '{user_email}'"

def failed_logging (user_email): 
	return f"UPDATE logging SET failed_login_attempts = failed_login_attempts + 1 WHERE user_email = '{user_email}'"

def successful_passwordreset_logging (user_email): 
	return f"UPDATE logging SET successful_password_reset = successful_password_reset + 1 WHERE user_email = '{user_email}'"

def attempt_passwordreset_logging (user_email): 
	return f"UPDATE logging SET attempt_password_reset = attempt_password_reset + 1 WHERE user_email = '{user_email}'"