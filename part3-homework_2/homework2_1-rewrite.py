#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "Elijah"
__date__ = "2017/7/5 16:14"

import os

GLOBAL_STAFFDICT = {}


def operation():
    '''
    功能选择界面
    :param :
    :return: input_sql
    '''
    welcome_str = '''
                                      欢迎来到员工信息查询程序
------------------------------------------------------------------------------------------------------
操作语法说明：

添加：INSERT INTO 表名称 VALUES 值1, 值2,....
删除：DELETE —> 输入欲删除的条目编号
修改：UPDATE 表名称 SET 列名称 = 新值 WHERE 列名称 = 某值
查询：SELECT * FROM 表名称 WHERE 列名称 = 某值
      SELECT * FROM 表名称 WHERE 列名称 LIKE 某值
      SELECT 列名称1,列名称2... FROM 表名称 WHERE 列名称 = 某值
------------------------------------------------------------------------------------------------------
    '''
    print(welcome_str)
    input_sql = input('请输入SQL语句(或者输入q退出)：\n>>>').strip()
    if input_sql.lower() == 'q':
        print('感谢使用模拟SQL程序，欢迎再次使用！再见！')
        exit()
    else:
        return input_sql


def read_table(sql_file):
    '''
    将SQL表文件读取至内存
    :param :
    :return:memory_dict
    '''
    memory_dict = {}
    staff_list = []
    with open(sql_file, mode='r', encoding='utf-8') as f:
        for line in f:
            staff_list.clear()
            for i in range(len(line.split(',')) - 1):
                staff_list.append(line.split(',')[(i + 1)].strip())
            memory_dict[line.split(',')[0]] = staff_list.copy()
    return memory_dict


def write_table(sql_file, memory_dict):
    '''
    将内存数据写至SQL表文件
    :param staff_dict:
    :return:
    '''
    with open(sql_file, mode='w', encoding='utf-8') as f:
        for k, v in memory_dict.items():
            num = len(memory_dict[k])
            f.write(str(k) + ',')
            for i in range(num):
                if i == (num - 1):
                    f.write(str(v[i]).strip())
                else:
                    f.write(str(v[i]).strip() + ',')
            f.write('\n')


def creat(memory_dict, input_sql):
    '''
    添加语句
    :param :staff_dict
    :return:None
    '''
    while True:
        tab_name = input_sql.split()[2] + '.txt'
        file_list = os.listdir(os.getcwd())
        if tab_name in file_list:
            fields = input_sql.lower().split('values')[1]
            memory_dict[len(memory_dict.keys()) + 1] = fields.split(',')
            print('新条目已经添加至表' + tab_name + '!')
            break
        else:
            print('对不起，当前目录不存在命令中的表！请检查命令！')
            break


def retrieve(memory_dict, input_sql):
    '''
    查询员工信息
    :param memory_dict:
    :param input_sql:
    :return:
    '''
    while True:
        count = 0
        field_dict = {'name': 0, 'age': 1, 'phone': 2, 'dept': 3, 'enroll_date': 4}
        tab_name = input_sql.split()[3] + '.txt'
        file_list = os.listdir(os.getcwd())
        if tab_name in file_list:
            select_str = input_sql.lower().split('from')[0]
            select_field = select_str[select_str.lower().index(' '):]
            condition_str = input_sql.lower().split('where')[1]
            if ('*' in select_field) and ('=' in condition_str):
                condition_field = condition_str.lower().split('=')[0].strip()
                condition_value = condition_str.lower().split('=')[1].strip()
                try:
                    for k, v in memory_dict.items():
                        if condition_value.replace('\'', '') == v[field_dict[condition_field]]:
                            count += 1
                            print(str(k) + '、' + str(v))
                except:
                    print('对不起，字段输入有误！请重新输入命令！')
                    break
                print('共查询出 ' + str(count) + ' 个条目')
                break
            elif ('*' in select_field) and ('like' in condition_str.lower()):
                condition_field = condition_str.lower().split('like')[0].strip()
                condition_value = condition_str.lower().split('like')[1].strip()
                for k, v in memory_dict.items():
                    try:
                        if condition_value.replace('\'', '') in v[field_dict[condition_field]]:
                            count += 1
                            print(str(k) + '、' + str(v))
                    except:
                        print('对不起，字段输入有误！请重新输入命令！')
                        break
                print('共查询出 ' + str(count) + ' 个条目')
                break
            elif (',' in select_field):
                flag = False
                select_fieldlist = select_field.strip().split(',')
                condition_field = condition_str.lower().split('=')[0].strip()
                condition_value = condition_str.lower().split('=')[1].strip()
                for k, v in memory_dict.items():
                    if flag:
                        break
                    try:
                        if condition_value.replace('\'', '') == v[field_dict[condition_field]]:
                            count += 1
                            print('\n' + str(k) + '、', end='')
                            for i in range(len(select_fieldlist)):
                                try:
                                    print(v[field_dict[select_fieldlist[i]]] + ',', end='')
                                except:
                                    print('对不起，您查询的列名称有误，请重新输入！')
                                    flag = True
                                    count = 0
                                    break
                    except:
                        print('对不起，字段输入有误！请重新输入命令！')
                        break
                print('\n共查询出 ' + str(count) + ' 个条目')
                break
            else:
                print('对不起，您输入的查询命令有误，请重新输入！')
                break
        else:
            print('对不起，当前目录不存在命令中的表！请检查命令！')
            break


def update(memory_dict, input_sql):
    '''
    修改员工信息
    :param :staff_dict
    :return:
    '''
    count = 0
    flag = False
    field_dict = {'name': 0, 'age': 1, 'phone': 2, 'dept': 3, 'enroll_date': 4}
    while not flag:
        tab_name = input_sql.split()[1] + '.txt'
        file_list = os.listdir(os.getcwd())
        if tab_name in file_list:
            update_str = input_sql[
                         input_sql.lower().index(' ', input_sql.lower().index('set')):input_sql.lower().index('where')]
            update_field = update_str.split('=')[0].strip()
            update_value = update_str.split('=')[1].replace('\'', '').strip()
            condition_str = input_sql.lower().split('where')[1]
            condition_field = condition_str.split('=')[0].strip()
            condition_value = condition_str.split('=')[1].replace('\'', '').strip()
            for k, v in memory_dict.items():
                try:
                    if v[field_dict[condition_field]].lower() == condition_value.lower():
                        v[field_dict[update_field]] = update_value
                        count += 1
                        print('条目 ' + str(k) + '、' + str(v) + ' 修改完成！')
                except:
                    print('对不起，字段输入有误！请重新输入命令！')
                    flag = True
                    break
            if count == 0:
                print('对不起，没有符合条件的条目，表未作任何修改！')
                break
            elif count > 0:
                print('共有' + str(count) + '个条目修改完成！')
                break
        else:
            print('对不起，当前目录不存在命令中的表！请检查命令！')
            break


def delete(memory_dict, input_sql):
    '''
    删除员工信息
    :param :staff_dict
    :return:
    '''
    while True:
        for k, v in memory_dict.items():
            print(k + '、' + str(v))
        del_num = input('\n请输入您要删除的条目编号(或者输入q退出):\n>>>').strip()
        if del_num.isdigit() and 0 < int(del_num) <= len(memory_dict):
            is_sure = input('请确认是否删除条目(y/n)：\n' + str(memory_dict[del_num]) + '\n>>>').strip()
            if is_sure.lower() == 'y':
                del memory_dict[del_num]
                print('条目删除成功！')
                break
            elif is_sure.lower() == 'n':
                break
            else:
                print('输入有误，请重新选择！\n')
                continue
        elif del_num.lower() == 'q':
            break
        else:
            print('请输入正确的条目编号！\n')
            continue


if __name__ == '__main__':
    while True:
        GLOBAL_STAFFDICT = read_table('staff_table.txt')
        input_sql = operation()
        if input_sql.lower().split()[0] == 'insert':
            creat(GLOBAL_STAFFDICT, input_sql)
            write_table('staff_table.txt', GLOBAL_STAFFDICT)
            continue
        elif input_sql.lower().split()[0] == 'delete':
            delete(GLOBAL_STAFFDICT, input_sql)
            write_table('staff_table.txt', GLOBAL_STAFFDICT)
            continue
        elif input_sql.lower().split()[0] == 'update':
            update(GLOBAL_STAFFDICT, input_sql)
            write_table('staff_table.txt', GLOBAL_STAFFDICT)
            continue
        elif input_sql.lower().split()[0] == 'select':
            retrieve(GLOBAL_STAFFDICT, input_sql)
            write_table('staff_table.txt', GLOBAL_STAFFDICT)
            continue
        else:
            while True:
                is_exit = input('是否确认退出（y/n）？\n>>>')
                if is_exit.lower() == 'y':
                    write_table('staff_table.txt', GLOBAL_STAFFDICT)
                    exit()
                elif is_exit.lower() == 'n':
                    break
                else:
                    print('您输入的操作有误，请重新输入！')
                    continue
