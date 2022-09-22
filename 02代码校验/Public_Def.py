# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 21:24
# @Author  : 孟砀砀
# @File    : Public_Def.py
# @Software: PyCharm
class Public_def:
    def __init__(self):
        self.words = Public_def().read_file()

    def read_file(self):
        """
        测试的代码  获取代码
        :return:
        """
        words_list = []
        with open('test.txt', 'r', encoding='utf-8') as fp:
            for line in fp:
                words_list.append(line)
        return words_list


    def Deal_Line_Word(self, line_word):
        """
        方法是剔除 每一行代码中 "--" 之后的数据
        :param line_word: 每一行的代码码
        :return: 返回剔除 "--"  之后的内容
        """
        str = ""
        for letter in line_word:
            if letter != '-':
                str = str + letter
            else:
                break
        return str

    def get_word_list(self,words):
        """
        :param words:  传入的是代码的内容
        :return:
        """
        # 获取读取test文件下的内容   测试用例
        res_list = []
        words = self.words
        for word_line in words:
            # 提出代码中注释的内容
            word_line = Public_def().Deal_Line_Word(word_line)
            # 同一行的数据用空格分隔 找到每一个关键字
            word_line_list = word_line.split(' ')
            # 切分后的数据添加到数组中
            res_list.append(word_line_list)
        return res_list
