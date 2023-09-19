# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: api_doc_qa.py
# @time: 2023/7/22 15:20
import time
import traceback

from flask import request
from flask.json import jsonify
from flask import Blueprint

from qa.doc_qa import DocQA
from utils.logger import logger

api_doc_qa = Blueprint('api_doc_qa', __name__)


@api_doc_qa.route("/api/doc_qa", methods=["POST"])
def chatgpt_group_chat():
    question = request.json["question"]
    model_name = request.json.get("model_name", "Baichuan-13B-Chat")
    return_data = {'question': question, 'answer': '', "status": 'success', 'error': '', 'elapse_ms': 0,
                   "contexts": "", "sources": ""}
    t1 = time.time()
    try:
        reply, contexts, sources = DocQA(question).answer(model_name)
        return_data['answer'] = reply
        return_data['contexts'] = contexts
        return_data['sources'] = sources
    except Exception:
        logger.error(traceback.format_exc())
        return_data['status'] = 'fail'
        return_data['error'] = traceback.format_exc()

    t2 = time.time()
    return_data['elapse_ms'] = (t2 - t1) * 1000

    return jsonify(return_data)
