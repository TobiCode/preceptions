# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 23:29:41 2019

@author: Tobi
"""

import sqlite3

from flask import Flask, jsonify, request, Blueprint

precepts_routes = Blueprint('precepts_routes', __name__)

@precepts_routes.route("/daily_precept", methods=['GET'])
def get_random_precept():
    conn = sqlite3.connect('percept_webs.db')
    c = conn.cursor()    
    sql = "SELECT * FROM Precepts ORDER BY RANDOM() LIMIT 1;"
    result = next(c.execute(sql))
    print (type((result)))
    print(result)
    result_json = jsonify(result)
    print(result_json)
    print(type(result_json))
    
    # Save (commit) the changes
    conn.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    
    return result_json
    
@precepts_routes.route("/add_daily_precept", methods=['POST'])
def add_precept():
    if request.method== 'POST':
        data = request.form
        if "Precept_Text" in data:
            precept_text = data["Precept_Text"]
        else:
            precept_text = None
        if "Author" in data:
            author = data["Author"]
        else:
            author = None
        if "Interpretation" in data:
            interpretation = data["Interpretation"]
        else:
            interpretation = None
            
        conn = sqlite3.connect('percept_webs.db')
        c = conn.cursor()
        c.execute('INSERT INTO Precepts VALUES (?,?,?,?)',(None, precept_text,author, interpretation))
        # Save (commit) the changes
        conn.commit()
        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        conn.close()
        
        return (jsonify({"Status": "DONE"}))
    
'''TODO
@precepts_routes.route("/delete_daily_precept", methods=['POST'])
def delete_precept():
    ##USe Post here, because we don't know the id of the precept
    if request.method== 'POST':
        data = request.form
        if "Precept_Text" in data:
            precept_text = data["Precept_Text"] 
        else:
            precept_text = None
        if "Author" in data:
            author = data["Author"]
        else:
            author = None
        if "Interpretation" in data:
            interpretation = data["Interpretation"]
        else:
            interpretation = None
            
        conn = sqlite3.connect('percept_webs.db')
        c = conn.cursor()
        c.execute('INSERT INTO Precepts VALUES (?,?,?,?)',(None, precept_text,author, interpretation))
        # Save (commit) the changes
        conn.commit()
        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        conn.close()
        
        return (jsonify({"Status": "DONE"}))
    
