#!/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Elijah"
__date__ = "2017/6/18 20:07"

# Readme
# Author: Elijah
# Time: 2017-06-18
# Function:HAproxy配置文件操作
#     1. 根据用户输入输出对应的backend下的server信息
#     2. 可添加backend 和sever信息
#     3. 可修改backend 和sever信息
#     4. 可删除backend 和sever信息
#     5. 操作配置文件前进行备份
#     6. 添加server信息时，如果ip已经存在则修改;如果backend不存在则创建；若信息与已有信息重复则不操作
# Need Environment：Python 3.5 、PyCharm
# Move：
# Feature：
# Important py file：os
# How To：Execute directly
# 个人发挥：用模块化的编程思想
# 个人博客地址：http://blog.csdn.net/dragonyangang/article/details/74067566

#导入
import os

#全局变量
global_var = {'is_retrieve':False,
              'is_continue':False}
file_dict = {}

#函数定义
def operation(file_dict):
    '''
    操作功能列表
    :return: opera_num
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
    ''' %backend_str

    print(welcome_str)
    opera_num = input('>>>').strip()
    return opera_num

def read_config(seclect_file):
    '''
    读取配置文件内容至内存
    :return:f_dict
    '''
    backend = ""
    server_info = []
    f_dict = {}
    # seclect_file = input('请选择想要操作的HAproxy配置文件：\n>>>').strip()
    with open(seclect_file,mode='r',encoding='utf-8') as f:
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
    :param seclect_file:
    :return:None
    '''
    import time
    with open(backup_file, mode='r',encoding='utf-8') as f:
        s = f.read()
    with open('haproxy_backup.conf',mode='a',encoding='utf-8') as f_backup:
        f_backup.write('\n>>>' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '--backup\n')
        f_backup.write(s)

def create(file_dict):
    '''
    添加backend 和sever信息
    :return:None
    '''
    server_info = []
    new_backend = input('请输入要添加的backend信息：\n>>>').strip()
    new_name = input('请输入要添加的server name信息：\n>>>').strip()
    new_ip = input('请输入要添加的server ip信息：\n>>>').strip()
    new_weight = input('请输入要添加的weight信息：\n>>>').strip()
    new_maxconn = input('请输入要添加的maxconn信息：\n>>>').strip()
    server_info.append(new_name)
    server_info.append(new_ip)
    server_info.append(new_weight)
    server_info.append(new_maxconn)
    file_dict[new_backend] = server_info.copy()
    print('添加成功！')

def retrieve(file_dict):
    '''
    查询backend 和sever信息
    :return:None
    '''
    while not global_var['is_retrieve']:
        retri_backend = input('请输入要查询的backend名称(或者输入Q退出)：\n>>>').strip()
        if retri_backend in file_dict.keys():
            show_info = '''
            您查询的backend信息如下：
            backend: %s
            server name: %s
            server ip: %s
            weight: %s
            maxconn: %s
            ''' %(retri_backend, file_dict[retri_backend][0], file_dict[retri_backend][1],
                  file_dict[retri_backend][2],file_dict[retri_backend][3])
            print(show_info)
            choice = input('是否继续查询(y/n)?').strip()
            global_var['is_continue'] =False
            while not global_var['is_continue']:
                if choice.lower() == 'y':
                    global_var['is_continue'] = True
                    continue
                elif choice.lower() == 'n':
                    global_var['is_retrieve'] = True
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
    :return:None
    '''
    update_backend = input('请输入要修改的backend信息：\n>>>').strip()
    update_name = input('请输入要修改的server name信息：\n>>>').strip()
    update_ip = input('请输入要修改的server ip信息：\n>>>').strip()
    update_weight = input('请输入要修改的weight信息：\n>>>').strip()
    update_maxconn = input('请输入要修改的maxconn信息：\n>>>').strip()
    if file_dict[update_backend] :
        file_dict[update_backend][0] = update_name
        file_dict[update_backend][1] = update_ip
        file_dict[update_backend][2] = update_weight
        file_dict[update_backend][3] = update_maxconn
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
    with open(seclect_file,mode='r',encoding='utf-8') as f:
        info_old = f.read()
        info_new = info_old[:info_old.index('\nbackend ')]
    with open(seclect_file,mode='w',encoding='utf-8') as f:
        f.write(info_new)
        for i in file_dict.keys():
            content = '''
backend %s
        server %s %s weight %s maxconn %s
            ''' %(i, file_dict[i][0], file_dict[i][1], file_dict[i][2] ,file_dict[i][3])
            f.write(content)

#主函数
if __name__ == '__main__':
    while True:
        select_file = input('请输入您要查看的配置文件名(直接回车选择默认文件haproxy.conf):\n>>>').strip()
        if select_file == '':
            select_file = 'haproxy.conf'
        else:
            select_file = select_file
        #获取当前路径下的文件名称
        file_list=os.listdir(os.getcwd())
        if select_file in file_list:
            while True:
                file_dict = read_config(select_file)
                opera_num = operation(file_dict)
                #添加功能
                if opera_num == '1':
                    #添加前备份
                    backup(select_file)
                    create(file_dict)
                    #添加后写入文件
                    write_config(select_file,file_dict)
                    continue
                #删除功能
                elif opera_num == '2':
                    #添加前备份
                    backup(select_file)
                    delete(file_dict)
                    #添加后写入文件
                    write_config(select_file,file_dict)
                    continue
                #修改功能
                elif opera_num == '3':
                    #添加前备份
                    backup(select_file)
                    update(file_dict)
                    #添加后写入文件
                    write_config(select_file,file_dict)
                    continue
                #查询功能
                elif opera_num == '4':
                    #添加前备份
                    backup(select_file)
                    global_var['is_retrieve'] = False
                    retrieve(file_dict)
                    #添加后写入文件
                    write_config(select_file,file_dict)
                    continue
                #退出
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
        else :
            print('您选择的配置文件错误或不存在，请重新选择！')
            continue
