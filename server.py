from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key= 'secret tunnells'





@app.route('/')                           
def counter():
    if "count" in session:
        session["count"] += 1
    else:
        session["count"] = 0

    return render_template('index.html', count= session["count"])



@app.route('/bumper')                           
def bumper():
    if "count" in session:
        session["count"] += 2
    else:
        session["count"] = 0

    return render_template('index.html', count= session["count"])











#============================================
#Reset Session to Empty
#============================================

@app.route("/destroy_session")
def destroy_session():
    session.clear()
    return redirect("/")












if __name__=="__main__":
    app.run(debug=True)