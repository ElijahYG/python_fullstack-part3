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
    How To：
    操作流程如下：
    1、程序运行后会显示出目前的配置文件信息，用户选择功能编号进入相对应功能模块
    2、添加backend信息：用户将要添加的backend所有信息用字典形式输入
       示例：{"backend": "test.oldboy.org","record":{"server name": "100.1.1.9","server ip": "100.1.1.9","weight": 20,"maxconn": 30}}
       同时也满足添加server信息时，如果backend域名地址已经存在则修改;如果backend不存在则创建；
    3、修改backend信息：用户同样将要修改的backend所有信息用字典形式输入，程序会校验是否有对应的backend名称，有则正常修改，没有则提示用户有误
    4、删除backend信息：程序会显示出目前配置文件中存在的backend信息，用户输入想要删除的backend信息即可，如果域名输入有误，则提示用户重新输入
    5、查询backend信息：用户输入要查询的backend信息，会显示出该backend信息下的具体server配置参数，如果用户输入错误会有相对应提示
    个人发挥：用模块化的编程思想
- 个人博客地址：http://blog.csdn.net/dragonyangang/article/details/74067566

# 第三模块：作业2：员工信息表程序
    Readme
    Author: Elijah
    Time: 2017-06-20
    Function:员工信息表程序——要求
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
    How To：操作流程如下：
    1、程序运行后用户根据语句语法说明进行SQL输入，支持增、删、改、查操作，程序通过判断用户输入的字符串关键字分别进入不懂的操作模块
    2、添加SQL：以insert开头的字符串会定位置添加功能，程序会判断用户输入的表文件是否在当前目录下，若不在则提示错误
    3、删除SQL：用户输入delete关键字后系统会列出当前默认staff_table表中的行项目，用户输入相对应的编号进行删除行项目操作
    4、修改SQL：以update开头进行对应功能，判断用户set字段名和值与查询条件字段和对应值
    5、查询SQL：支持要求中的三种语法
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
    How To：
    操作流程如下：
    1、程序运行后用户选择以不同身份登录，用户身份or管理员身份，
    2、用户操作：进入时用户输入用户名密码进行登录，校验用户文件中是否存在，若失败3次则加入冻结名单，需要管理员才能解冻，若成功则会显示5项功能：
        ①存款：用户输入存款金额进行对应账号的存款操作，相应对将操作明细记录到账单中
        ②取款：用户输入取款金额进行取款，若取款金额大于当前余额+用户额度则会提示用户不能取款，并显示该用户当前余额，等待重新输入取款金额
        ③转账：会列举出该用户可以转账的用户清单以供选择，选择完成后输入转账金额，若转账金额超过用户当前余额则会提出金额超出，重新等待用户选择转账用户
        ④显示账单：用户输入欲查询的年月，如果输入正确则会显示出对应年月用户的所有存、取款、转账等对应操作的金额和余额明细
        ⑤修改密码：提示用户输入当前密码，正确后等待用户设置新密码
    3、管理员操作：默认只有一个管理员账号admin和密码admin123，输入正确后进入管理员功能区，包括3项功能：
        ①添加用户：等待管理员输入新用户的用户名和密码进行添加，同时设置用户额度默认为10000
        ②冻结用户：显示当前系统存在的用户，并等待管理员输入欲冻结的用户，完成后写入冻结用户清单文件中以备用户登录时进行校验
        ③设定用户额度：显示当前系统存在的用户，等待管理员选择并设置该用户新额度        
    个人发挥：用模块化的编程思想
- 个人博客地址：http://blog.csdn.net/dragonyangang/article/details/74071248

[回到顶部](#readme)
