# from model import get_db_connection , create_db
from ml import modelcnn
from model import insert_data, get_data
from flask import Flask, redirect , render_template , request, jsonify
from uuid import uuid4
import os
import json

app = Flask(__name__,static_url_path='', static_folder='static')
app.config['UPLOAD_FOLDER'] = 'testing/'
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

def generate_unique_filename(file):
    ext = file.filename.rsplit('.', 1)[1].lower()
    unique_filename = f"{uuid4()}.{ext}"
    return unique_filename

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/test', methods=['POST'])
def test():
    if request.method == 'POST':
        data = {}
        file = request.files['file']
        unique_filename = generate_unique_filename(file)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)
        hasil1,result1 = modelcnn.efficient_net(filepath)
        hasil2,result2 = modelcnn.vgg19(filepath)
        result1_percentage = result1 * 100
        result2_percentage = result2 * 100

        # Format nilai dengan dua digit desimal
        result1 = "{:.2f}".format(result1_percentage)
        result2 = "{:.2f}".format(result2_percentage)

        data["image"] = filepath
        data['result1'] = result1
        data['result2'] = result2
        data['hasil1'] = hasil1
        data['hasil2'] = hasil2
        id = insert_data(data)
        return json.dumps(data, indent=4)
        # return redirect(f"/result/{id}")

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/result/<id>', methods=['GET']) 
def result(id) :
    print(id)
    data = get_data(id)
    print(data)
    data.todict()
    return json.dumps(data, indent=4)
    # return render_template('result_detail.html', percobaan=data)

if __name__ == '__main__' :
    app.run(debug=True)