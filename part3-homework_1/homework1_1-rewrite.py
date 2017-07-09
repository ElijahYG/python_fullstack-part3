#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "Elijah"
__date__ = "2017/7/5 10:32"

import os

GLOBAL_VAR = {'IS_RETRIEVE': False,
              'IS_CONTINUE': False}
FILE_DICT = {}


def operation(file_dict):
    '''
    操作功能列表
    :param file_dict:
    :return:
    '''
    backend_str = ''
    for i in file_dict.keys():
        backend_str += i + '\n'

    welcome_str = '''
        欢迎来到HAproxy配置程序
-------------------------------------
backend信息如下：
%s
-------------------------------------
请选择您的操作：
1、添加backend 和sever信息
2、删除backend 和sever信息
3、修改backend 和sever信息
4、查询backend 和sever信息
5、退出配置程序
    ''' % backend_str

    print(welcome_str)
    opera_num = input('>>>').strip()
    return opera_num


def read_config(seclect_file):
    '''
    读取配置文件内容至内存
    :param seclect_file:
    :return:
    '''
    backend = ""
    server_info = []
    f_dict = {}
    with open(seclect_file, mode='r', encoding='utf-8') as f:
        for line in f:
            if line.strip().startswith('backend'):
                backend = line.split()[1]
                continue
            if line.strip().startswith('server'):
                server_info.clear()
                server_info.append(line.split()[1])
                server_info.append(line.split()[2])
                server_info.append(line.split()[4])
                server_info.append(line.split()[6])
                f_dict[backend] = server_info.copy()
    return f_dict


def backup(backup_file):
    '''
    对haproxy配置文件备份
    :param backup_file:
    :return:
    '''
    import time
    with open(backup_file, mode='r', encoding='utf-8') as f:
        s = f.read()
    with open('haproxy_backup.conf', mode='a', encoding='utf-8') as f_backup:
        f_backup.write('\n>>>' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '--backup\n')
        f_backup.write(s)


def create(file_dict):
    '''
    添加backend 和sever信息
    :param file_dict:
    :return:
    '''
    while True:
        server_info = []
        new_backend = input(
            '请输入要添加的backend信息(或者输入q退出)：\n'
            '示例：{"backend": "test.oldboy.org","record":{"server name": "100.1.1.9","server ip": "100.1.1.9","weight": 20,"maxconn": 30}}\n>>>').strip()
        if new_backend.lower() == 'q':
            break
        else:
            try:
                eval(new_backend)
            except:
                print('对不起，您输入的信息有误！请重新输入\n')
                continue
        new_backend = eval(new_backend)
        try:
            server_info.append(new_backend["record"]["server name"])
            server_info.append(new_backend["record"]["server ip"])
            server_info.append(new_backend["record"]["weight"])
            server_info.append(new_backend["record"]["maxconn"])
        except:
            print('对不起，您输入的backend信息有误，请重新输入！')
            continue
        file_dict[new_backend["backend"]] = server_info.copy()
        print('添加成功！')


def retrieve(file_dict):
    '''
    查询backend 和sever信息
    :return:None
    '''
    while not GLOBAL_VAR['IS_RETRIEVE']:
        retri_backend = input('请输入要查询的backend名称(或者输入q退出)：\n>>>').strip()
        if retri_backend in file_dict.keys():
            show_info = '''
            您查询的backend信息如下：
            backend: %s
            server name: %s
            server ip: %s
            weight: %s
            maxconn: %s
            ''' % (retri_backend, file_dict[retri_backend][0], file_dict[retri_backend][1],
                   file_dict[retri_backend][2], file_dict[retri_backend][3])
            print(show_info)
            choice = input('是否继续查询(y/n)?').strip()
            GLOBAL_VAR['IS_CONTINUE'] = False
            while not GLOBAL_VAR['IS_CONTINUE']:
                if choice.lower() == 'y':
                    GLOBAL_VAR['IS_CONTINUE'] = True
                    continue
                elif choice.lower() == 'n':
                    GLOBAL_VAR['IS_RETRIEVE'] = True
                    break
                else:
                    print('您的输入有误，请重新输入！')
                    continue
        elif retri_backend.lower() == 'q':
            break
        else:
            print('您输入的backend信息有误，请重新输入！')


def update(file_dict):
    '''
    修改backend 和sever信息
    :param file_dict:
    :return:
    '''
    while True:
        update_backend = input(
            '请输入要修改的backend信息(或者输入q退出)：\n'
            '示例：{"backend": "test.oldboy.org","record":{"server name": "100.1.1.9","server ip": "100.1.1.9","weight": 20,"maxconn": 30}}\n>>>').strip()
        if update_backend.lower() == 'q':
            break
        else:
            try:
                eval(update_backend)
            except:
                print('对不起，您输入的信息有误！请重新输入\n')
                continue
            update_backend = eval(update_backend)
            if file_dict[update_backend["backend"]]:
                file_dict[update_backend["backend"]][0] = update_backend["record"]["server name"]
                file_dict[update_backend["backend"]][1] = update_backend["record"]["server ip"]
                file_dict[update_backend["backend"]][2] = update_backend["record"]["weight"]
                file_dict[update_backend["backend"]][3] = update_backend["record"]["maxconn"]
                print('修改成功！')
            else:
                print('对不起，您输入的backend不存在！')



def delete(file_dict):
    '''
    删除backend 和sever信息
    :return:None
    '''
    delete_backend = input('请输入要删除的backend信息：\n>>>').strip()
    if input('请确认是否要删除一下信息：\n' + str(file_dict[delete_backend]) + '\n(y/n)>>>').lower() == 'y':
        del file_dict[delete_backend]
        print('删除backend信息成功！')
    else:
        print('请重新输入！')


def write_config(seclect_file, file_dict):
    '''
    将内存写入配置文件
    :param seclect_file:
    :param file_dict:
    :return: None
    '''
    with open(seclect_file, mode='r', encoding='utf-8') as f:
        info_old = f.read()
        info_new = info_old[:info_old.index('\nbackend ')]
    with open(seclect_file, mode='w', encoding='utf-8') as f:
        f.write(info_new)
        for i in file_dict.keys():
            content = '''
backend %s
        server %s %s weight %s maxconn %s
            ''' % (i, file_dict[i][0], file_dict[i][1], file_dict[i][2], file_dict[i][3])
            f.write(content)


if __name__ == '__main__':
    while True:
        select_file = input('请输入您要查看的配置文件名(直接回车选择默认文件haproxy.conf):\n>>>').strip()
        if select_file == '':
            select_file = 'haproxy.conf'
        else:
            select_file = select_file
        file_list = os.listdir(os.getcwd())
        if select_file in file_list:
            while True:
                FILE_DICT = read_config(select_file)
                opera_num = operation(FILE_DICT)
                if opera_num == '1':
                    backup(select_file)
                    create(FILE_DICT)
                    write_config(select_file, FILE_DICT)
                    continue
                elif opera_num == '2':
                    backup(select_file)
                    delete(FILE_DICT)
                    write_config(select_file, FILE_DICT)
                    continue
                elif opera_num == '3':
                    backup(select_file)
                    update(FILE_DICT)
                    write_config(select_file, FILE_DICT)
                    continue
                elif opera_num == '4':
                    backup(select_file)
                    GLOBAL_VAR['IS_RETRIEVE'] = False
                    retrieve(FILE_DICT)
                    write_config(select_file, FILE_DICT)
                    continue
                elif opera_num == '5':
                    while True:
                        is_exit = input('是否确认退出（y/n）？\n>>>')
                        if is_exit.lower() == 'y':
                            exit()
                        elif is_exit.lower() == 'n':
                            break
                        else:
                            print('您输入的操作有误，请重新输入！')
                            continue
        else:
            print('您选择的配置文件错误或不存在，请重新选择！')
            continue
