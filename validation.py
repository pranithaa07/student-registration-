import streamlit as st
import sqlite3

conn=sqlite3.connect("users.db",check_same_thread=False)
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    name TEXT PRIMARY KEY,
    password TEXT
)
""")

choice=st.sidebar.selectbox("menu",["Login","Register"])

if choice == "Register":
    name=st.text_input("Username")
    password=st.text_input("password",type="password")
    if st.button("Register"):
        cursor.execute("INSERT INTO users(name,password)VALUES(?,?)",(name,password))
        conn.commit()
        st.balloons()
if choice == "Login":
    name=st.text_input("Username")
    password=st.text_input("password",type="password")
    if st.button("Login"):
        cursor.execute("""SELECT *FROM users WHERE name=? AND password=?""",(name,password))
        result=cursor.fetchone()
        if result:
            st.success("Valid User")
        else:
            st.error("Invalid User")



        
