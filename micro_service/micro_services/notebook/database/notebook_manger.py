# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/6 
@desc:
"""

import logging
from micro_services.notebook.models import NotebookModel
# from .note_manger import NoteManager
from database import MySQLManger
from utilities.util import models_to_list, model_to_dict

logger = logging.getLogger('log')


class NoteBookManager(MySQLManger):
    _users = {}

    def __init__(self):
        super(NoteBookManager, self).__init__()
        self.model = NotebookModel

    def add_notebook(self, data):
        """
        新建到数据库
        data = {
            name = "hello"
        }
        :return:
        """
        if not isinstance(data, dict):
            raise Exception('data not dict')

        self.add_data(data)
        return True

    def add_notebook_list(self, data_list):
        """
        新建多个到数据库
        :param data:
        :return:
        """
        self.add_notebook_list(data_list)
        return True

    def notebook_from(self, query):
        """
        返回 notebook list
        query: {
            id = 12,
            name = 'boy'
        }
        :return: list
        """
        if not isinstance(query, dict):
            raise Exception('query not dict')

        d = self.load_data_one(query)
        return d

    def notebook_one_from(self, query):
        """
        返回单个 notebook
        :param query:
        :return: dict
        """
        l = self.load_data_list(query)
        return l

    def is_exit_books(self, query):
        """
        查询是否存在该笔记
        :param title:
        :param user_id:
        :return:
        """
        if not isinstance(query, dict):
            raise Exception('query not dict')

        ext = self.notebook_one_from(query)

        return True if ext else False

    def delete_one_notebook(self, query):
        """
        删除笔记本，如果存在笔记也一起删除
        :param _id:
        :return:
        """
        if self.is_exit_books(query):
            self.delete_one_notebook(query)
            return True
        else:
            return False