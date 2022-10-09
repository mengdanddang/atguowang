# -*- coding: utf-8 -*-
# @Time    : 2022/9/27 18:00
# @Author  : 孟砀砀
# @File    : Deal_DI_Words.py
# @Software: PyCharm

"""
这是数据集成任务的判断
"""
import json
from Public_Def import Public_def

class Deal_DI_Words:
    def __init__(self):
        pass

    def read_file(self,file_name):
        """
        测试的代码  获取代码
        :return:
        """
        str = ''
        with open(file_name, 'r', encoding='utf-8') as fp:
            for line in fp:
                str = str + line
        return str


    def Deal_DI_Words(self,words):
        res = "数据集成任务没问题，可以发布"
        # 测试环境 的输入 是读取本地的是数据    这里需要删除
        words = Deal_DI_Words().read_file('di_test.txt')
        obj = json.loads(words)
        # 获取并发数
        concurrent = obj['setting']['speed']['concurrent']
        if concurrent > 4:
            res = "单任务的并发数过大，请确认任务的并发数"
        return res

    def Analysis_Node_Name(self,node_name):
        """
        :param node_name: 节点的名称
        :return: 返回节点的校验结果
        """
        res = '节点名称没问题，可以正常发布'
        # 节点名称转大写
        node_name = node_name.upper()
        # 节点名称以空格切分
        node_name_list = node_name.split(' ')
        # 判断数组的长度
        if len(node_name_list) > 1:
            res = "节点名称中存在空格，请检查"
        # 检查是否以SQL开头
        if node_name[0:3] != "DI_":
            res = "节点名称应该以DI开头，请检查"
        return res

