# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: llm_chat_api.py
# @time: 2023/7/22 15:12
import json
import requests

from config.config_parser import EMBEDDING_API, CHAT_COMPLETION_API, SYSTEM_ROLE
from utils.logger import logger


def get_text_embedding(req_text, model_name):
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps({"model": model_name, "input": req_text})
    new_req = requests.request("POST", EMBEDDING_API, headers=headers, data=payload)
    return new_req.json()['data'][0]['embedding']


def chat_completion(message, model_name):
    payload = json.dumps({
        "model": model_name,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_ROLE
            },
            {
                "role": "user",
                "content": message
            }
        ],
        "temperature": 0,
        "max_tokens": 300
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", CHAT_COMPLETION_API, headers=headers, data=payload)
    logger.info(f"model_name: {model_name}, response: {response.text}")
    return response.json()['choices'][0]['message']['content']
