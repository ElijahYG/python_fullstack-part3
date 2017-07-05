# python_fullstack
## [我的博客](http://blog.csdn.net/dragonyangang "我的博客")

# 第三模块：作业1：HAproxy配置文件操作
    Readme
    Author: Elijah
    Time: 2017-06-18
    Function:HAproxy配置文件操作
        1. 根据用户输入输出对应的backend下的server信息
         2. 可添加backend 和sever信息
        3. 可修改backend 和sever信息
        4. 可删除backend 和sever信息
        5. 操作配置文件前进行备份
        6. 添加server信息时，如果ip已经存在则修改;如果backend不存在则创建；若信息与已有信息重复则不操作
    Need Environment：Python 3.5 、PyCharm
    Move：
    Feature：
    Important py file：os
    How To：Execute directly
    个人发挥：用模块化的编程思想
- 个人博客地址：http://blog.csdn.net/dragonyangang/article/details/74067566

# 第三模块：作业2：员工信息表程序
    Readme
    Author: Elijah
    Time: 2017-06-20
    Function:员工信息表程序
        可进行模糊查询，语法至少支持下面3种:
            select name,age from staff_table where age > 22
            select  * from staff_table where dept = "IT"
            select  * from staff_table where enroll_date like "2013"
        查到的信息，打印后，最后面还要显示查到的条数
        可创建新员工纪录，以phone做唯一键，staff_id需自增
        可删除指定员工信息纪录，输入员工id，即可删除
        可修改员工信息，语法如下:
         UPDATE staff_table SET dept="Market" WHERE where dept = "IT"
        1. 支持至少三种方法的select查询，并在最后显示查询到的条数。
        2. 创建新员工记录，以phone为唯一键，staff_id自增
        3. 输入员工id可删除指定员工信息记录
        4. 可以使用UPDATE命令修改指定员工信息。
    Need Environment：Python 3.5 、PyCharm
    Move：
    Feature：
    Important py file：re、time
    How To：Execute directly
    个人发挥：用模块化的编程思想
- 个人博客地址：http://blog.csdn.net/dragonyangang/article/details/74069329

# 第三模块：作业3：ATM

    Readme
    Author: Elijah
    Time: 2017-06-24
    Function:ATM
        1. 指定最大透支额度
        2. 可取款
        3. 定期还款（每月指定日期还款，如15号）
        4. 可存款
        5. 定期出账单
        6. 支持多用户登陆，用户间转帐
        7. 支持多用户
        8. 管理员可添加账户、指定用户额度、冻结用户等
    Need Environment：Python 3.5 、PyCharm
    Move：
    Feature：
    Important py file：re、datetime
    How To：Execute directly
    个人发挥：用模块化的编程思想
- 个人博客地址：http://blog.csdn.net/dragonyangang/article/details/74071248

[回到顶部](#readme)
