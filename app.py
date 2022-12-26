from flask import Flask, render_template, request, redirect, session, jsonify
from flask_session import Session

import sys
import json


def function_list(script):
    
    file = open(session['path']+'\\'+ script+'.py','r')
    functions = []
    
    for line in file:
       line= line.replace(' ', '')
       
       if(line[0:3] == 'def'):
         line = line.replace('\n','')
         line = line.replace(':','')
         i = line.find('(')
         j = line.find(')')
         line = line.replace( line[i:j+1], '')
         functions.append(line[3:])
    
    return functions


def file_options(path):
    'Read script name from README.txt'
    
    file= open(path + '\README.txt', 'r')
    scripts=[]
    for line in file:
       scripts.append(line)
    return scripts


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/getScriptList', methods=["post"])

def getScriptList():
    'Gets the scripts name in the drop-down list '

    folder_path = request.form.get("path")
    folder_path = folder_path.replace('\\', "\\\\")
    session["path"] = folder_path
    
    py_scripts = file_options(folder_path)
    session['py_scripts'] = py_scripts
    
    return render_template('index.html') 


@app.route('/getFunctionList', methods=["post"])
def getFunctionList():
    'Gets name of function(s) present within the python script selected from the drop-down list'

    script= str(request.form.get("readme"))
    script = script.replace('\r','')
    script = script.replace('\n','')
    session['script'] = script
    #py_scripts = session['py_scripts'] 
    functions = function_list(script)
    session['functions'] = functions
    
    return render_template('index.html', functions = functions)

@app.route('/execute', methods = ['post'])
def execute():
    'runs the selected function from the selected python script'
    
    #uncomment to access scripts from other directories than home directory
    sys.path.insert(1, session['path'])    

    functions = session['functions']
    fun_list = request.form.getlist("function_checkbox")      #list of functions selected by the user
    script= session['script']
    run = __import__(script)
    
    # list to store graph data
    jsonData = []
    
    #list to store xl data (data to be displayd in table form)
    table = []
    
    #list to store text data 
    text = []

    i=0

    for fun in fun_list:
        #data = getattr(run, fun)()
        
        if fun[-6:]== '_graph': 
            data = getattr(run, fun)()
            # data['id'] = "char"
            data.update({'id': 'chart'+str(i)})
            i = i+1
            data = json.dumps(data)
            jsonData.append(data)

        elif fun[-3:]== '_xl':
            data = getattr(run, fun)()
            table.append(data)
        else:
            data = getattr(run, fun)()
            text.append(data)
    
    sys.path.remove(session['path'])

    return render_template('index.html',jsonData = jsonData, text=text ,table= table, functions= functions )

if __name__ == '__main__':
    app.debug = False
    app.run()

