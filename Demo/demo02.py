import os

s = 'Hello World\n文本文件的中文信息读取\n文本文件中文信息的写入\n'
f = open('file/test1.txt', 'a+', encoding="utf-8")  # test1是已经存在于当前目录下的文档
f.write(s)
f.close
