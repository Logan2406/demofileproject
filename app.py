from flask import Flask, render_template,request,flash, send_file
import os
from demoFunctions import *
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

app.config['UPLOAD_FOLDER']=os.path.join(os.getcwd(),"static","files")

@app.route('/upload', methods=['GET','POST'])
def upload():
    if(request.method=='POST'):
        ff = request.files['file1']
        ff.save(app.config['UPLOAD_FOLDER']+"\\"+ff.filename)
        [pdf_files,img_file]=print_hi(ff.filename)
        print(pdf_files)
        print(img_files)

        return render_template('file.html',Files=pdf_files,Images=img_files,file_len=len(pdf_files),img_len=len(img_files))

@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    outfile = filename
    return send_file(outfile,as_attachment=True)

if(__name__=="__main__"):
    app.run(debug=True,port=8000)
