# copy_the_indicators_used_in_the_template.py
# version：0.1  2019.9.8
#   初始版

import os
import shutil

# 打开文件夹templates，注意格式\\
# path = 'C:\\Users\\Administrator\\AppData\\Roaming\\MetaQuotes\\Terminal\\2010C2441A263399B34F537D91A53AC9\\templates\\templates_bak'
'''预置基本路径'''
path = 'C:\\Users\\Administrator\\AppData\\Roaming\\MetaQuotes\\Terminal\\2010C2441A263399B34F537D91A53AC9'  # 预置基本路径
# C:\Users\Administrator\AppData\Roaming\MetaQuotes\Terminal\2010C2441A263399B34F537D91A53AC9\MQL4\Indicators

'''置当前工作文件夹'''
print(os.getcwd())                                              # 查看当前工作文件夹
os.chdir(path+'\\MQL4\\Indicators')                             # 重置当前工作文件夹
print(os.getcwd())                                              # 再查看当前工作文件夹

'''建立指标备份文件夹'''
a_path = 'Indicators_bak'                                       # 指标备份文件夹名
if os.path.exists(a_path):                                      # 指标备份文件夹存在
    print(a_path, 'folder already exists.')
else:                                                           # 指标备份文件夹不存在
    print(a_path, 'folder does not exist.')
    os.mkdir(a_path)                                            # 创建文件夹
    print('The', a_path, 'folder has been created.')

'''开始处理'''
'''信息记录文件'''
no_mq4_files = 'Nonexistent mq4 file:\n\n'                      # 不存在的mq4文件记录
no_ex4_files = 'Nonexistent ex4 file:\n\n'                      # 不存在的ex4文件记录
'''读模板文件夹目录'''
result = os.listdir(path+'\\templates')                         # 读文件夹
'''遍历 *.tpl 模板文件'''
for line in result:
    # line = '维加斯通道海龟交易模板.tpl'     # test
    print('\n' + line)                      # test
    line = line.lower()                                         # 把所有字符中的大写字母转换成小写字母
    if line.find('.tpl') >= 0:                                  # ' .tpl '存在
        sourcefile = line                                       # 作文件名
        # with open(path+'\\'+sourcefile, 'r', encoding='utf8') as sf:     # 按utf8码打开源文件
        # with open(path+'\\'+sourcefile, 'r') as sf:           # 打开源文件
        with open(path+'\\templates\\'+sourcefile, 'rb') as sf:            # 按二进制方式打开源文件
            # all_file = sf.read()                              # 读取文件所有内容           # test
            fileline = sf.readline()                            # 读1行
            # string = fileline.decode('utf-8', 'ignore')       # bytes 类型转换为 str 类型, 忽略非法字符，用strict会抛出异常  # test
            # fileline = fileline.decode('utf-8', 'replace')    # bytes 类型转换为 str 类型, 用�取代非法字符
            fileline = fileline.decode('gb2312', 'replace')     # bytes 类型转换为 str 类型, 用�取代非法字符 (*.tpl文件内的中文是gb2312码)
            # fileline = sf.readline()                              # test
            # fileline = fileline.decode('utf-8', 'replace')        # test
            # fileline = sf.readline()                              # test
            # fileline = fileline.decode('utf-8', 'replace')        # test
            # fileline = sf.readline()                              # test
            # fileline = fileline.decode('utf-8', 'replace')        # test
            # print(fileline)                                     # test

            no_mq4_files += sourcefile + '\n'                       # 加入此模板文件名
            no_ex4_files += sourcefile + '\n'                       # 加入此模板文件名
            while fileline:                                         # 非无内容行；无内容行(最后行)则退出
                if fileline.find('name=Custom Indicator') >= 0:     # 'name=Custom Indicator'存在,则转换
                    fileline = sf.readline()                        # 再读1行
                    fileline = fileline.decode('gb2312', 'replace') # bytes 类型转换为 str 类型, 用�取代非法字符 (*.tpl文件内的中文是gb2312码)
                    if fileline.find('<expert>') >= 0:              # '<expert>'存在,则转换
                        fileline = sf.readline()                    # 再读1行
                        fileline = fileline.decode('gb2312', 'replace')
                        if fileline.find('name=') >= 0:             # 'name='存在,则转换
                            files_to_copy = fileline.replace('name=', '')  # 去除'name='
                            print('  ' + files_to_copy, end='')        # test
                            files_to_copy = files_to_copy.replace('\n', '')  # 去除换行符
                            files_to_copy = files_to_copy.replace('\r', '')  # 去除回车符
                            if os.path.exists(files_to_copy + '.ex4'):          # 文件存在
                                shutil.copyfile(files_to_copy + '.ex4', a_path + '/' + files_to_copy + '.ex4')    # 复制ex4文件
                            else:
                                no_ex4_files += '    ' + files_to_copy + '.ex4' + '\n'    # 不存在的ex4文件记录
                            if os.path.exists(files_to_copy + '.mq4'):                  # 文件存在
                                shutil.copyfile(files_to_copy + '.mq4', a_path + '/' + files_to_copy + '.mq4')    # 复制mq4文件
                            else:
                                no_mq4_files += '    ' + files_to_copy + '.mq4' + '\n'    # 不存在的mq4文件记录
                            a = 1            # test
                            pass

                fileline = sf.readline()                            # 读下1行
                fileline = fileline.decode('gb2312', 'replace')     # bytes 类型转换为 str 类型, 用�取代非法字符 (*.tpl文件内的中文是gb2312码)

            pass
    pass

os.chdir(path+'\\MQL4\\Indicators\\Indicators_bak')             # 重置当前工作文件夹
no_mq4_files += '\n\n' + no_ex4_files                           # 并入单个文件
with open('no_mq4ex4_files.txt', 'w', encoding='utf8') as tf:   # 按utf8码打开目标文件
    '''写入目标文件'''
    tf.write(no_mq4_files)                                      # 保存文件






