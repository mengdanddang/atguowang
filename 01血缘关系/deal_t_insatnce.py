# -*- coding: utf-8 -*-
# @Time    : 2022/9/6 10:48
# @Author  : 孟砀砀
# @File    : deal_t_insatnce.py
# @Software: PyCharm

import xlrd
import json


def read_excel():
    data_excel = xlrd.open_workbook('t_insatnce.xls')

    # 获取sheet得名称
    names = data_excel.sheet_names()

    table = data_excel.sheets()[0]
    # print(table)

    rows = table.nrows
    # 返回所有单元格由行组成得列表
    row_data = table.row_values(2)
    # 返回所有列组成得元组
    col_data = table.col_values(4, start_rowx=1)

    # for i in (1,rows):
    row_res = []

    for index in col_data:
        row_str = ''
        obj = json.loads(index)
        # 解析来源
        # 来源得数据类型
        src_stepType = obj['steps'][0]['stepType']
        # 数据得方式

        # 来源表  --样式多样需要逐步解析
        src_base = obj['steps'][0]['parameter']
        # print(type(src_base))
        dest_base = obj['steps'][1]['parameter']
        sjfs = obj['steps'][0]['name']
        if "connection" in src_base.keys():
            # 来源表名称

            src_table = src_base['connection'][0]['table']
            # print(src_table)
            # 来源表数据库
            src_guid = src_base['connection'][0]['datasource']

            # print(dest_base)
            dest_table = dest_base['table']
            # print(src_table)
            # 来源表数据库
            dest_guid = dest_base['datasource']
            srfs = obj['steps'][1]['name']

        else:
            src_table = src_base['table']
            src_guid = src_base['datasource']

            dest_table = dest_base['table']
            # print(src_table)
            # 来源表数据库
            dest_guid = dest_base['datasource']
            srfs = obj['steps'][1]['name']

        # 解析目的
        row_str = str(src_stepType) + ',' + str(sjfs) + ',' + str(src_guid) + ',' + str(
            src_table) + ',' + str(srfs) + ',' + str(dest_guid) + ',' + str(dest_table)
        # print(row_str)
        row_res.append(row_str)
    return row_res

        # print(src_stepType, sjfs, src_guid, src_table, srfs, dest_guid, dest_table)


# 数据写入
def write_excel(row_res):
    with open('resoult.csv','a', encoding='utf-8') as fp:
        for row in row_res:
            print(row)
            fp.write(str(row))
            fp.write('\n')
    fp.close()
if __name__ == '__main__':
    row_res = read_excel()
    write_excel(row_res)
