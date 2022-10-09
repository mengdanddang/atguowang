# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 21:19
# @Author  : 孟砀砀
# @File    : Deal_Dml_words.py
# @Software: PyCharm

from Public_Def import Public_def
# 这个方法为了验证DML 建表语句中的语法
class Deal_Ddl_Words:
    def __init__(self):
        pass

    def Deal_Dml_Words(self,words):
        line_word_list = Public_def().get_word_list(words)
        num_line = 1
        res = "DDL节点没问题，可以正常发布"
        for line_word in line_word_list:
            # 循环每一行中的关键字
            for word in line_word:
                # 判断是否包含插入语句
                if word.strip().upper() == "INSERT":
                    res = "DDL代码中不能DML的语言，请检查 %d 行代码" %(num_line)
                    break
            num_line +=1
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
        if node_name[0:7] != "CREATE_":
            res = "节点名称应该以CREATE开头，请检查"
        return res




