# -*- coding: utf-8 -*-
# @Time    : 2022/9/20 21:42
# @Author  : 孟砀砀
# @File    : Deal_Words.py
# @Software: PyCharm

class Deal_Words:
    def __init__(self):
        pass

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

    def Deal_DML_Words(self, words):
        """
        :param words: 传进来的是代码的片段
        :return:  返回代码是否合规
        """
        res = '代码没问题，可以发布'
        world_list = Deal_Words().read_file()
        for word_line in world_list:
            # 提出代码中注释的内容
            word_line = Deal_Words().Deal_Line_Word(word_line)
            # 同一行的数据用空格分隔 找到每一个关键字
            word_line_list = word_line.split(' ')
            # 判断代码中是否有create
            for word in word_line_list:
                print(word.upper())
                if word.strip('').upper() == "CREATE":
                    res = "DML代码中不能有建表语句，请检查"
                    break
                elif word == "*":
                    res = "DML代码中不能有SELECT * 的操作，请检查"
                    break
        return res
