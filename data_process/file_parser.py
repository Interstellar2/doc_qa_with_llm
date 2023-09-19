# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: file_parser.py
# @time: 2023/9/8 18:01
from langchain.document_loaders import TextLoader, PyPDFLoader, Docx2txtLoader, SeleniumURLLoader

from utils.logger import logger


class FileParser(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def txt_loader(self):
        documents = TextLoader(self.file_path, encoding='utf-8').load()
        return documents

    def pdf_loader(self):
        loader = PyPDFLoader(self.file_path)
        documents = loader.load_and_split()
        return documents

    def docx_loader(self):
        loader = Docx2txtLoader(self.file_path)
        documents = loader.load()
        return documents

    def url_loader(self):
        loader = SeleniumURLLoader(urls=[self.file_path])
        documents = loader.load()
        return documents

    def parse(self):
        logger.info(f'parse file: {self.file_path}')
        if self.file_path.endswith(".txt"):
            return self.txt_loader()
        elif self.file_path.endswith(".pdf"):
            return self.pdf_loader()
        elif self.file_path.endswith(".docx"):
            return self.docx_loader()
        elif "http" in self.file_path:
            return self.url_loader()
        else:
            logger.error("unsupported document type!")
            return []


