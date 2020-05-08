from flask import Flask,render_template,request,redirect,url_for
from flask import request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/name',methods=['GET','POST'])
def get_name():
    if request.method=='POST':
        return 'zxh POST'
    else:
        return 'zxh GET'


@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method=='POST':
        f=request.files['file']
        basepath = os.path.dirname(__file__)
        upload_path=os.path.join('/tmp/flask/upload',secure_filename(f.filename))
        f.save(upload_path)
        sudoPassword = '991103'
        command = 'mv /tmp/flask/upload/'+secure_filename(f.filename)+'  /var/www/html'
        str = os.system('echo %s|sudo -S %s' % (sudoPassword, command)) 
        return redirect(url_for('upload'))
    return render_template('upload.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
