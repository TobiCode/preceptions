import sqlite3

from flask import Flask, jsonify, request

conn = sqlite3.connect('percept_webs.db')

app = Flask(__name__)

@app.route("/")
def hello_world():
    welcome_string = "Hello. Welcome to the webservice for the Preception App."
    return welcome_string

@app.route("/daily_precept", methods=['GET'])
def get_random_preception():
    with app.app_context():
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
    
@app.route("/add_daily_precept", methods=['GET', 'POST'])
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
        

        

#get_random_preception(conn)

if __name__ == '__main__':
    app.run(debug=True, port=5050)