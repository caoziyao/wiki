# coding: utf-8

import os
import json
import datetime
from app.utils.const import WikiRoot, ignore_file
from app.handler.base_handler import BaseHandler
from micro_services.mznv.model import NodeModel, TreeModel,  BookModel, ArticleModel

from app.manager import BookManger
from app.database import DBSession

class BookHandler(BaseHandler):
    def get(self):
        manger = BookManger()
        data = manger.get_book_list()
        self.write(data)