# copy_the_indicators_used_in_the_template.py
# version：0.5.14
#   1、加入备份MT5 Scripts文件夹内的mqh文件操作  2019.12.3
#   2. 对第1条备份MT5 Scripts文件夹程序段再次作修改，改为有含'a_'字符串文件均备份  2019.12.4
#   3. 对特殊要求备份的文件改为含'a_'字符串特殊文件的备份  2019.12.4
# version：0.5.13  2019.12.2
#   加入部分MQL5特殊头文件备份程序段
# version：0.5.12  2019.12.2
#   加入MT5 Scripts文件备份程序段；更改少量文件名
# version：0.5.11  2019.11.15
#   加入MT5 EA文件备份程序段
# version：0.5.10  2019.11.6
#   加入Visio流程图备份处理程序段
# version：0.5.9  2019.11.5-6
#   增加建立'E:\建立'Scripts_常用'文件夹; 加入特殊指标及特殊脚本备份处理程序段
# version：0.5.8  2019.10.13
#   建立'E:\备份常用代码'文件夹,将'forex_python_常用'、'templates_常用'、'Experts_常用'、'Indicators_常用'等备份在此文件夹内,便于查找
# version：0.5.7  2019.10.8
#   程序改成函数调用
# version：0.5.6  2019.10.8
#   加入备份模板内指标处理Python程序文件夹为'E:\forex_python_常用'及备份操作
# version：0.5.5  2019.10.7
#   1.格式作了整理
#   2.备份盘符改为'E:\'
#   3.加入备份EA文件夹为'E:\Experts_常用'
# version：0.5.4  2019.10.6
#   1.打印字符作修改
#   2.在模板文件名前加入模板序号，便于了解有多少模板
#   3.增加备份模板文件夹为'F:\templates_常用'
# version：0.5.3  2019.10.5
#   将指标备份文件夹改为'F:\Indicators_常用'
# version：0.5.2  2019.10.5
#   对一些繁体汉字操作会出现错误,原因是gb2312码不包含繁体汉字操作,改为gbk码,则能正确操作简繁体汉字
# version：0.5.1  2019.9.22
#   建立指标备份文件夹程序段作了修改
# version：0.5.0  2019.9.22
#   shutil.copy2()处作了修改
# version：0.4  2019.9.12
#   发现所复制的mq4及ex4文件的修改时间为新的复制时间的错误，变更命令，使复制的文件原修改时间
# version：0.3  2019.9.8
#   加入输出文件对齐方式，方便观看
# version：0.2  2019.9.8
#   加入指标是否有无信息、增加错误指示
# version：0.1  2019.9.8
#   初始版

import os
import shutil


def create_backup_folder(bak_path, description, mqex_files):
    '''建立备份文件夹及显示、记录信息'''
    if os.path.exists(bak_path):                                    # 模板备份文件夹存在
        message = 'The %s folder already exists.'
        print(message % bak_path)                           # 显示
    else:                                                           # 模板备份文件夹不存在
        os.mkdir(bak_path)                                          # 创建文件夹
        message = 'The %s folder was not created. Now create the %s folder.'
        print(message % (bak_path, bak_path))               # 显示
    print(description + bak_path + '\n')                    # 显示
    return mqex_files + '(' + description + bak_path + ')\n'        # 记录模板备份文件夹位置


def run_main():
    print('--------1--------2--------3--------4--------5--------6--------7--------8--------9--------10--------')  # 打印标记

    '''信息记录文件'''
    mqex_files = '常用tpl/常用mq4/常用ex4/mq5/ex5/py/vsdx files:\n'  # 常用文件记录

    '''预置基本路径，注意格式\\'''
    path = 'C:\\Users\\Administrator\\AppData\\Roaming\\MetaQuotes\\Terminal\\2010C2441A263399B34F537D91A53AC9'   # 预置基本路径
    path5 = 'C:\\Users\\Administrator\\AppData\\Roaming\\MetaQuotes\\Terminal\\FB9A56D617EDDDFE29EE54EBEFFE96C1'  # 预置MT5基本路径
    '''置当前工作文件夹'''
    print('当前工作文件夹:', os.getcwd())                     # 显示  # 查看当前工作文件夹
    os.chdir(path+'\\MQL4\\Indicators')                             # 重置当前工作文件夹
    print('重置当前工作文件夹:', os.getcwd() + '\n')           # 显示  # 再查看当前工作文件夹

    '''备份盘符'''
    drive = 'E:\\'

    '''备份常用代码文件夹及说明'''
    backup_folder = '备份常用代码'
    description = '备份常用代码文件夹: '
    general_path = drive + backup_folder                            # 备份常用代码文件夹路径
    mqex_files = create_backup_folder(general_path, description, mqex_files)  # 建立备份常用代码文件夹及显示、记录信息

    '''备份模板文件夹及说明'''
    backup_folder = 'templates_常用'
    description = '模板备份文件夹: '
    t_path = general_path + '\\' + backup_folder                    # 模板备份文件夹路径
    mqex_files = create_backup_folder(t_path, description, mqex_files)  # 建立模板备份文件夹及显示、记录信息

    '''备份指标文件夹及说明'''
    backup_folder = 'Indicators_常用'
    description = '指标备份文件夹: '
    i_path = general_path + '\\' + backup_folder                    # 指标备份文件夹路径
    mqex_files = create_backup_folder(i_path, description, mqex_files)  # 建立指标备份文件夹及显示、记录信息

    '''备份EA文件夹及说明'''
    backup_folder = 'Experts_常用'
    description = 'EA备份文件夹: '
    e__path = general_path + '\\' + backup_folder                   # EA备份文件夹路径
    mqex_files = create_backup_folder(e__path, description, mqex_files)  # 建立EA备份文件夹及显示、记录信息

    '''备份脚本文件夹及说明'''
    backup_folder = 'Scripts_常用'
    description = '脚本备份文件夹: '
    s__path = general_path + '\\' + backup_folder                   # 脚本备份文件夹路径
    mqex_files = create_backup_folder(s__path, description, mqex_files)  # 建立脚本备份文件夹及显示、记录信息

    '''备份MT5-EA文件夹及说明'''
    backup_folder = 'MT5_Experts_常用'
    description = 'MT5 EA备份文件夹: '
    mt5_e_path = general_path + '\\' + backup_folder                   # MT5 EA备份文件夹路径
    mqex_files = create_backup_folder(mt5_e_path, description, mqex_files)  # 建立MT5 EA备份文件夹及显示、记录信息

    '''备份MT5-Scripts文件夹及说明'''
    backup_folder = 'MT5_Scripts_常用'
    description = 'MT5 Scripts备份文件夹: '
    mt5_s_path = general_path + '\\' + backup_folder                   # MT5 Scripts备份文件夹路径
    mqex_files = create_backup_folder(mt5_s_path, description, mqex_files)  # 建立MT5 Scripts备份文件夹及显示、记录信息

    '''建立模板内指标备份处理Python程序文件备份文件夹及说明'''
    backup_folder = 'forex_python_常用'
    description = 'Python程序备份文件夹: '
    py_path = general_path + '\\' + backup_folder                   # Python程序备份文件夹路径
    mqex_files = create_backup_folder(py_path, description, mqex_files)  # 建立Python程序备份文件夹及显示、记录信息

    '''建立Visio流程图备份文件夹及说明'''
    backup_folder = 'Visio_file_常用'
    description = 'Visio流程图备份文件夹: '
    visio_path = general_path + '\\' + backup_folder                # Visio流程图备份文件夹路径
    mqex_files = create_backup_folder(visio_path, description, mqex_files) + '\n'  # 建立Visio流程图备份文件夹及显示、记录信息

    '''开始处理'''
    '''读模板文件夹目录'''
    result = os.listdir(path+'\\templates')                         # 读文件夹
    tpl_count = 0                                                   # 模板计数
    '''遍历 *.tpl 模板文件'''
    for line in result:
        sourcefile = line                                           # 作文件名
        line = line.lower()                                         # 把所有字符中的大写字母转换成小写字母
        if line.find('.tpl') >= 0:                                  # '.tpl'存在
            tpl_count += 1                                          # 模板计数
            print('\n' + str(tpl_count) + '：' + sourcefile)  # 显示
            mqex_files += str(tpl_count) + '：' + sourcefile + '\n'  # 加入序号及此模板文件名
            shutil.copy2(path+'\\templates\\'+sourcefile, t_path + '/')  # 复制模板文件
            with open(path+'\\templates\\'+sourcefile, 'rb') as sf:  # 按二进制方式打开源文件
                fileline = sf.readline()                            # 读1行
                fileline = fileline.decode('gbk', 'replace')        # bytes 类型转换为 str 类型, 用�取代非法字符 (*.tpl文件内
                                                                    # 的中文是gb2312码,gb2312是gbk的子集)
                while fileline:                                                         # 非无内容行；无内容行(最后行)则退出
                    fileline = fileline.lower()                                         # 大写字母转换成小写字母
                    if fileline.find('custom') >= 0:                                    # 'Custom'存在,则转换
                        fileline = sf.readline()                                        # 再读1行
                        fileline = fileline.decode('gbk', 'replace')                    # bytes 类型转换为 str 类型, 用�取代
                                                                                        # 非法字符 (*.tpl文件内的中文是gb2312
                                                                                        # 码,gb2312是gbk的子集)
                        if fileline.find('expert') >= 0:                                # 'expert'存在,则转换
                            fileline = sf.readline()                                    # 再读1行
                            fileline = fileline.decode('gbk', 'replace')
                            if fileline.find('name=') >= 0:                             # 'name='存在,则转换
                                files_to_copy = fileline.replace('name=', '')           # 去除'name='
                                files_to_copy = files_to_copy.replace('\n', '')         # 去除换行符
                                files_to_copy = files_to_copy.replace('\r', '')         # 去除回车符

                                if os.path.exists(files_to_copy + '.ex4'):                              # 文件存在
                                    a = '    ' + files_to_copy + '.ex4'
                                    print(a)                                                    # 显示
                                    mqex_files += a + '\n'                                              # 加入有ex4文件记录
                                    shutil.copy2(files_to_copy + '.ex4', i_path + '/')                  # 复制ex4文件，包含访
                                                                                                        # 问和修改时间
                                else:
                                    b = '    ' + files_to_copy + '.ex4'
                                    ln = len(b.encode('gbk'))                                           # 按汉字为2字节计算长
                                                                                                        # 度,gb2312是gbk的子集
                                    l1 = 46 - ln                                                        # 空字节数
                                    if l1 >= 5:                                                         # 计算对齐位置
                                        l2 = ln - len(b)                                                # 汉字个数：汉字为2字
                                                                                                        # 节长度-汉字为1字节长度
                                        b = b.ljust(46 - l2) + 'no ex4 !!!!!!'                          # 将'no ex4 !!!!!!'
                                                                                                        # 作对齐处理
                                    else:
                                        b += '     no ex4 !!!!!!'
                                    print(b)                                                    # 显示
                                    mqex_files += b + '\n'                                              # 加入无ex4文件记录

                                if os.path.exists(files_to_copy + '.mq4'):                              # 文件存在
                                    c = '    ' + files_to_copy + '.mq4'
                                    print(c)                                                    # 显示
                                    mqex_files += c + '\n'                                              # 加入有mq4文件记录
                                    shutil.copy2(files_to_copy + '.mq4', i_path + '/')                  # 复制mq4文件，包含访
                                                                                                        # 问和修改时间
                                else:
                                    d = '    ' + files_to_copy + '.mq4'
                                    ln = len(d.encode('gbk'))                                           # 按汉字为2字节计算长
                                                                                                        # 度,gb2312是gbk的子集
                                    l1 = 46 - ln                                                        # 空字节数
                                    if l1 >= 5:                                                         # 计算对齐位置
                                        l2 = ln - len(d)                                                # 汉字个数：汉字为2字
                                                                                                        # 节长度-汉字为1字节长度
                                        d = d.ljust(46 - l2) + 'no'                                     # 将'no'作对齐处理
                                    else:
                                        d += '     no'
                                    print(d)                                                    # 显示
                                    mqex_files += d + '\n'                                              # 加入无mq4文件记录

                            else:
                                e = '    ' + sourcefile + ' has error 1 !'  # 错误1
                                print(e)                                    # 显示有错误的模板文件
                                mqex_files += e + '\n'                      # 加入文件记录

                        else:
                            f = '    ' + sourcefile + ' has error 2 !'      # 错误2
                            print(f)                                        # 显示有错误的模板文件
                            mqex_files += f + '\n'                          # 加入文件记录

                    fileline = sf.readline()                                # 读下1行
                    fileline = fileline.decode('gbk', 'replace')            # bytes 类型转换为 str 类型, 用�取代非法字符
                                                                            # (*.tpl文件内的中文是gb码,gb2312是gbk的子集)
            mqex_files += '\n'                                              # 此模板文件处理完毕,加换行符

    '''遍历模板文件结束,加入模板文件总数'''
    print('\nTotal number of templates: ' + str(tpl_count) + '\n')   # 显示
    mqex_files += 'Total number of templates: ' + str(tpl_count) + '\n\n'   # 加入模板总数

    '''智能交易EA文件备份'''
    print('\nExpert Advisor files:')
    mqex_files += '\nExpert Advisor files:\n'
    '''读EA文件夹目录'''
    result = os.listdir(path+'\\MQL4\\Experts')                     # 读文件夹
    ea_count = 0                                                    # EA文件计数
    '''遍历 *.mq4/.ex4 EA文件'''
    for line in result:
        sourcefile = line                                           # 作文件名
        line = line.lower()                                         # 把所有字符中的大写字母转换成小写字母
        if line.find('.mq4') >= 0 or line.find('.ex4') >= 0:        # '.mq4'或'.ex4'存在
            ea_count += 1                                           # 计数
            print('    ' + sourcefile)                          # 显示
            mqex_files += '    ' + sourcefile + '\n'                # 加入此文件名
            shutil.copy2(path+'\\MQL4\\Experts\\'+sourcefile, e__path + '/')  # 复制EA文件
    '''遍历EA文件结束,加入EA文件总数'''
    print('\nTotal number of Expert Advisor files: ' + str(ea_count) + '\n')   # 显示
    mqex_files += '\nTotal number of Expert Advisor files: ' + str(ea_count) + '\n\n'  # 加入EA文件总数

    '''MT5智能交易EA文件备份'''
    print('\nMT5 Expert Advisor files:')
    mqex_files += '\nMT5 Expert Advisor files:\n'
    '''读EA文件夹目录'''
    result = os.listdir(path5+'\\MQL5\\Experts')                    # 读文件夹
    ea5_count = 0                                                   # MT5 EA文件计数
    '''遍历 *.mq5/.ex5 EA文件'''
    for line in result:
        sourcefile = line                                           # 作文件名
        line = line.lower()                                         # 把所有字符中的大写字母转换成小写字母
        if line.find('.mq5') >= 0 or line.find('.ex5') >= 0:        # '.mq5'或'.ex5'存在
            ea5_count += 1                                          # 计数
            print('    ' + sourcefile)                          # 显示
            mqex_files += '    ' + sourcefile + '\n'                # 加入此文件名
            shutil.copy2(path5+'\\MQL5\\Experts\\'+sourcefile, mt5_e_path + '/')  # 复制MT5 EA文件
    '''遍历MT5 EA文件结束,加入MT5 EA文件总数'''
    print('\nTotal number of MT5 Expert Advisor files: ' + str(ea5_count) + '\n')   # 显示
    mqex_files += '\nTotal number of MT5 Expert Advisor files: ' + str(ea5_count) + '\n\n'  # 加入MT5 EA文件总数

    '''MT5脚本Scripts自定义(custom)文件备份'''
    print('\nMT5 scripts custom files:')
    mqex_files += '\nMT5 scripts custom files:\n'
    '''读Scripts文件夹目录'''
    result = os.listdir(path5+'\\MQL5\\Scripts')                    # 读文件夹
    s5_count = 0                                                    # MT5 scripts custom 文件计数
    '''遍历 *.mq5/.ex5/.mqh scripts custom 文件'''
    for line in result:
        sourcefile = line                                           # 作文件名
        line = line.lower()                                         # 把所有字符中的大写字母转换成小写字母
        #if line.find('.mq5') >= 0 or line.find('.ex5') >= 0 or line.find('.mqh') >= 0:  # '.mq5'或'.ex5'或'.mqh'存在
        if line.find('a_') >= 0:                                    # 'a_'存在
            s5_count += 1                                           # 计数
            print('    ' + sourcefile)                          # 显示
            mqex_files += '    ' + sourcefile + '\n'                # 加入此文件名
            shutil.copy2(path5+'\\MQL5\\Scripts\\'+sourcefile, mt5_s_path + '/')  # 复制MT5 scripts custom 文件
    '''遍历MT5 scripts custom 文件结束,加入MT5 scripts custom 文件总数'''
    print('\nTotal number of MT5 scripts custom files: ' + str(s5_count) + '\n')   # 显示
    mqex_files += '\nTotal number of MT5 scripts custom files: ' + str(s5_count) + '\n\n'  # 加入MT5 scripts custom 文件总数

    '''部分特殊指标文件备份'''
    indicators_file = 'a_指标例程.mq4'
    shutil.copy2(path+'\\MQL4\\Indicators\\' + indicators_file, i_path + '/')  # 复制特殊指标文件
    print('\n备份的特殊指标文件:')
    print('    ' + indicators_file)                             # 显示
    mqex_files += '\n备份的特殊指标文件:\n'
    mqex_files += '    ' + indicators_file                          # 加入特殊指标文件名
    '''部分特殊脚本文件备份'''
    scripts_file = 'a_脚本例程.mq4'
    shutil.copy2(path+'\\MQL4\\Scripts\\' + scripts_file, s__path + '/')  # 复制特殊脚本文件
    print('备份的特殊脚本文件:')
    print('    ' + scripts_file)                                # 显示
    mqex_files += '\n备份的特殊脚本文件:\n'
    mqex_files += '    ' + scripts_file                             # 加入特殊脚本文件名
    '''部分MQL5特殊头文件备份'''
    scripts_file = 'a_Expert.mqh'
    shutil.copy2(path5+'\\MQL5\\Include\\Expert\\' + scripts_file, mt5_e_path + '/')  # 复制MQL5特殊头文件
    print('备份的MQL5特殊头文件:')
    print('    ' + scripts_file + '\n')                         # 显示
    mqex_files += '\n备份的MQL5特殊头文件:\n'
    mqex_files += '    ' + scripts_file + '\n\n'                    # 加入MQL5特殊头文件名

    '''模板内指标备份处理的Python程序文件备份'''
    print('\n备份处理模板中指标的Python程序文件:')
    mqex_files += '\n备份处理模板中指标的Python程序文件:\n'
    '''读Python程序文件目录'''
    py_sourcefile_path = 'E:\\Documents\\workspace\\workspace_Python\\ForeignExchange_Stock_Calculation'
    result = os.listdir(py_sourcefile_path)                         # 读文件夹
    py_count = 0                                                    # Python程序文件计数
    '''遍历 *.py 文件'''
    for line in result:
        sourcefile = line                                           # 作文件名
        line = line.lower()                                         # 把所有字符中的大写字母转换成小写字母
        if line.find('.py') >= 0:                                   # '.py'存在
            py_count += 1                                           # 计数
            print('    ' + sourcefile)                          # 显示
            mqex_files += '    ' + sourcefile + '\n'                # 加入此文件名
            shutil.copy2(py_sourcefile_path+'\\'+sourcefile, py_path + '/')  # 复制Python程序文件
    '''遍历Python程序文件结束,加入Python程序文件总数'''
    print('\n处理外汇的python程序总数: ' + str(py_count) + '\n')  # 显示
    mqex_files += '\n处理外汇的python程序总数: ' + str(py_count) + '\n\n'   # 加入Python程序文件总数

    '''Visio流程图备份处理'''
    print('\nVisio流程图文件:')
    mqex_files += '\nVisio流程图文件:\n'
    '''读Visio流程图文件目录'''
    visio_sourcefile_path = 'E:\\Documents\\Visio_file'
    result = os.listdir(visio_sourcefile_path)                      # 读文件夹
    visio_count = 0                                                 # 文件计数
    '''遍历文件'''
    for line in result:
        sourcefile = line                                           # 作文件名
        line = line.lower()                                         # 把所有字符中的大写字母转换成小写字母
        if line.find('.vsdx') >= 0:                                 # 文件存在
            visio_count += 1                                        # 计数
            print('    ' + sourcefile)                          # 显示
            mqex_files += '    ' + sourcefile + '\n'                # 加入此文件名
            shutil.copy2(visio_sourcefile_path+'\\'+sourcefile, visio_path + '/')  # 复制文件
    '''遍历Visio流程图文件结束,加入Visio流程图文件总数'''
    print('\nVisio流程图文件总数: ' + str(visio_count) + '\n')    # 显示
    mqex_files += '\nVisio流程图文件总数: ' + str(visio_count) + '\n\n'   # 加入文件总数

    with open(general_path+'\\mqex_files.txt', 'w', encoding='utf8') as tf:  # 按utf8码打开目标文件
        '''写入目标文件'''
        tf.write(mqex_files)                                        # 保存文件


run_main()



