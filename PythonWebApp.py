from flask import Flask, url_for, render_template, request

app = Flask(__name__) 

@app.route("/")
def render_main():
    return render_template('index.html')



@app.route("/response")
def render_response():
    Name = request.args['Name']
    Age = request.args['Age']
    Gender = request.args['Gender']
    Education = request.args['Education']
    Homeschooled = request.args['Homeschooled']
    HomeschoolEducation = request.args['HomeschoolEducation']
    Major = request.args['Major']
    Establishment = request.args['Establishment']
    Preferance = request.args['Preferance']
    
    
    
    reply1 = "My Name is " + Name + ", I am " + Age + " years old. " + "I am a " + Gender + " person." + " My Highest education is " + Education + "." + " I was " + Homeschooled + " Homeschooled."
    if HomeschoolEducation != "":
        reply1 = reply1 + " The Highest education I recieved while homeschooled was " + HomeschoolEducation + "."
    if Major != "":
        reply1 = reply1 + " I Majored in " + Major + "." 
    if Establishment != "":
        reply1 = reply1 + " I recived my highest education at " + Establishment 
        
    reply1 = reply1 + "." " My prefered job is a " + Preferance + ". " + "What job would be the best for me? " + "PLEASE PASTE THE SENTENCE RECEIVED TO CHATGPT OR ANY CHAT AI BOT."
        
    return render_template('response.html', response = reply1)
    
if __name__=="__main__":
    app.run(debug=True)
