# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

import os
import datetime
import numpy as np

import detect_anju_freeze

# netlify-flask  을 위해 추가
#pip install Frozen-Flask
from flask_frozen import Freezer
from app import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()



#----------------------------------
#upload file
#----------------------------------
#파일 업로드 처리
@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
   program_id = 'server.py'


   if request.method == 'POST':

      #----------------------------
      # Save the file to ./uploads
      f = request.files['file']
      file_name =secure_filename(f.filename)
      basepath = os.path.dirname(__file__)
      file_path = os.path.join(
      basepath, 'uploads', file_name)
      f.save(file_path)
      retrun_msg = '파일저장 완료!'
      print('[5]retrun_msg :',retrun_msg)

      #--------------------------c--
      # Make prediction
      #similar_glass_details=glass_detection.getUrl(file_path)
      #labels=detect_anju.detect(f)

      labels=detect_anju.detect(file_name)


      retrun_msg = '분석완료 !'
      print('[6]retrun_msg :',retrun_msg)

      return render_template('index.html', retrun_msg = retrun_msg,  labels=labels ,result_img= file_name)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
   #app.run(debug = True)
   app.run(host="0.0.0.0", port=5000)  # debug=True causes Restarting with stat