# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: api_file_upload.py
# @time: 2023/7/22 16:41
import os
import traceback

from flask import request, jsonify, Blueprint

from data_process.data_processor import DataProcessor


api_file_upload = Blueprint('api_file_upload', __name__)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx'}
UPLOAD_FILE_PATH = './files'

html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>文件上传</h1>
    <form method=post enctype=multipart/form-data>
         FILE: <input type=file name=file>
         URL PARSE: <input name="url" type="url" class="form-control" id="url">
         <input type=submit value=上传>
    </form>
    '''


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@api_file_upload.route('/api/uploads', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        url = request.form['url']
        if url:
            return_data = {"url": url, "parse": "ok!", "error": ""}
            try:
                DataProcessor(url).data_insert()
            except Exception:
                return_data["parse"] = "fail!"
                return_data["error"] = traceback.format_exc()
            return jsonify(return_data)
        else:
            file = request.files['file']
            file_name = file.filename
            if file and allowed_file(file_name):
                file_path = os.path.join(UPLOAD_FILE_PATH, file_name)
                if os.path.exists(file_path):
                    return f"The file <mark>{file_name}</mark> already existed!"
                file.save(file_path)
                # 解析文本
                DataProcessor(file_path).data_insert()
                return jsonify({"upload file": file_name,
                                "ES": "ok!",
                                "Milvus": "ok!"})
    return html
