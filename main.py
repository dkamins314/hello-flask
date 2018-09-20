from flask import Flask,request

app = Flask(__name__)
app.config['DEBUG'] = True

form="""

<!DOCTYPE html>

<html>
     
    <body>
        <form action= "hello",  method="Post">
            <labelfor "first name"> First name</label> 
            <input id="first name" type = "text" name = 'first name' /></label>
            <input type = "submit" />
        </form>
        
    </body>   
         
</html>
"""
@app.route("/")
def index():
    return form

@app.route("/Hello")
def hello():
    first_name= request.args.get("first_name")
    return '<h1> Hello '+ first_name +'</'
app.run()