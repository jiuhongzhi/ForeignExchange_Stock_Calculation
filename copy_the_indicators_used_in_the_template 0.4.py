# copy_the_indicators_used_in_the_template.py
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
# import chardet      # 查看当前字符串的编码格式


"""
def length(value, code):
    '''计算字符串长度'''
    '''code = 'utf-8' '''
    '''code = 'gb2312' '''
    a_length = len(value)
    utf8_length = len(value.encode(code))
    a_length = (utf8_length - a_length) / 2 + a_length
    return a_length
"""

# bb = chardet.detect(b'abcd')                   # test         # 查看当前字符串的编码格式

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
mq4ex4_files = 'mq4/ex4 file:\n\n'                              # mq4/ex4文件记录
# error = ''
'''读模板文件夹目录'''
result = os.listdir(path+'\\templates')                         # 读文件夹
'''遍历 *.tpl 模板文件'''
for line in result:
    # line = '维加斯通道海龟交易模板.tpl'          # test
    print('\n' + line)                          # test
    sourcefile = line                                           # 作文件名
    line = line.lower()                                         # 把所有字符中的大写字母转换成小写字母
    if line.find('.tpl') >= 0:                                  # '.tpl'存在
        # sourcefile = line                                     # 作文件名
        # with open(path+'\\'+sourcefile, 'r', encoding='utf8') as sf:     # 按utf8码打开源文件
        # with open(path+'\\'+sourcefile, 'r') as sf:           # 打开源文件
        mq4ex4_files += sourcefile + '\n'                       # 加入此模板文件名
        with open(path+'\\templates\\'+sourcefile, 'rb') as sf: # 按二进制方式打开源文件
            # all_file = sf.read()                    # test    # 读取文件所有内容
            fileline = sf.readline()                            # 读1行
            # string = fileline.decode('utf-8', 'ignore')       # bytes 类型转换为 str 类型, 忽略非法字符，用strict会抛出异常
            # fileline = fileline.decode('utf-8', 'replace')    # bytes 类型转换为 str 类型, 用�取代非法字符
            fileline = fileline.decode('gb2312', 'replace')     # bytes 类型转换为 str 类型, 用�取代非法字符 (*.tpl文件内的中文是gb2312码)
            # fileline = sf.readline()                              # test
            # fileline = fileline.decode('utf-8', 'replace')        # test
            # fileline = sf.readline()                              # test
            # fileline = fileline.decode('utf-8', 'replace')        # test
            # fileline = sf.readline()                              # test
            # fileline = fileline.decode('utf-8', 'replace')        # test
            # print(fileline)                                       # test
            while fileline:                                                         # 非无内容行；无内容行(最后行)则退出
                fileline = fileline.lower()                                         # 大写字母转换成小写字母
                if fileline.find('custom') >= 0:                                    # 'Custom'存在,则转换
                    fileline = sf.readline()                                        # 再读1行
                    fileline = fileline.decode('gb2312', 'replace')                 # bytes 类型转换为 str 类型, 用�取代非法字符 (*.tpl文件内的中文是gb2312码)
                    if fileline.find('expert') >= 0:                                # 'expert'存在,则转换
                        fileline = sf.readline()                                    # 再读1行
                        fileline = fileline.decode('gb2312', 'replace')
                        if fileline.find('name=') >= 0:                             # 'name='存在,则转换
                            files_to_copy = fileline.replace('name=', '')           # 去除'name='
                            files_to_copy = files_to_copy.replace('\n', '')         # 去除换行符
                            files_to_copy = files_to_copy.replace('\r', '')         # 去除回车符
                            if os.path.exists(files_to_copy + '.ex4'):                                          # 文件存在
                                a = '    ' + files_to_copy + '.ex4'
                                print(a)                                                    # test
                                mq4ex4_files += a + '\n'                                                        # 加入有ex4文件记录
                                # shutil.copyfile(files_to_copy + '.ex4', a_path + '/' + files_to_copy + '.ex4')  # 复制ex4文件，但不包含访问和修改时间
                                shutil.copy2(files_to_copy + '.ex4', a_path + '/')                              # 复制ex4文件
                            else:
                                b = '    ' + files_to_copy + '.ex4'
                                l = len(b.encode('gb2312'))                                                     # 按汉字为2字节计算长度
                                l1 = 40 - l                                                                     # 空字节数
                                if l1 >= 5:                                                                     # 计算对齐位置
                                    l2 = l - len(b)                                                             # 汉字个数：汉字为2字节长度-汉字为1字节长度
                                    b = b.ljust(40 - l2) + 'no ex4 !!!!!!'                                      # 将'no ex4 !!!!!!'作对齐处理
                                else:
                                    b += '     no ex4 !!!!!!'
                                print(b)                                                    # test
                                mq4ex4_files += b + '\n'                                                        # 加入无ex4文件记录
                            if os.path.exists(files_to_copy + '.mq4'):                                          # 文件存在
                                c = '    ' + files_to_copy + '.mq4'
                                print(c)                                                    # test
                                mq4ex4_files += c + '\n'                                                        # 加入有mq4文件记录
                                # shutil.copyfile(files_to_copy + '.mq4', a_path + '/' + files_to_copy + '.mq4')  # 复制mq4文件，但不包含访问和修改时间
                                shutil.copy2(files_to_copy + '.mq4', a_path + '/')                              # 复制mq4文件
                            else:
                                d = '    ' + files_to_copy + '.mq4'
                                l = len(d.encode('gb2312'))                                                     # 按汉字为2字节计算长度
                                l1 = 40 - l                                                                     # 空字节数
                                if l1 >= 5:                                                                     # 计算对齐位置
                                    l2 = l - len(d)                                                             # 汉字个数：汉字为2字节长度-汉字为1字节长度
                                    d = d.ljust(40 - l2) + 'no'                                                 # 将'no'作对齐处理
                                else:
                                    d += '     no'
                                print(d)                                                    # test
                                mq4ex4_files += d + '\n'                                                        # 加入无mq4文件记录
                            pass

                        else:
                            e = '    ' + sourcefile + ' has error 1 !'  # 错误1
                            print(e)                        # test      # 显示有错误的模板文件
                            mq4ex4_files += e + '\n'                    # 加入文件记录

                    else:
                        f = '    ' + sourcefile + ' has error 2 !'      # 错误2
                        print(f)                            # test      # 显示有错误的模板文件
                        mq4ex4_files += f + '\n'                        # 加入文件记录

                fileline = sf.readline()                                # 读下1行
                fileline = fileline.decode('gb2312', 'replace')         # bytes 类型转换为 str 类型, 用�取代非法字符 (*.tpl文件内的中文是gb2312码)

            pass

        mq4ex4_files += '\n'                                            # 此模板文件处理完毕,加换行符

    pass

os.chdir(path+'\\MQL4\\Indicators\\Indicators_bak')             # 重置当前工作文件夹
with open('mq4ex4_files.txt', 'w', encoding='utf8') as tf:      # 按utf8码打开目标文件
    '''写入目标文件'''
    tf.write(mq4ex4_files)                                      # 保存文件






