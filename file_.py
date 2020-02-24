# !/usr/bin/env python
# encoding: utf-8
import os
import datetime,time


# size_dict = {}
# type_dict = {}

def get_size_type(path):
    files = os.listdir(path)  # 返回path指定的文件夹包含的文件或文件夹的名字的列表
    # print(files)
    for filename in files:
        file_name=filename
        # print(file_name)
        file_path = os.path.join(path, filename)  # os.path.join(path1[, path2[, ...]])	把目录和文件名合成一个路径
        if os.path.isdir(file_path):  # 判断路径是否为目录
            get_size_type(file_path)  # 递归
        elif os.path.isfile(file_path):  # 判断路径是否为文件
            file_type = os.path.splitext(file_path)[1]  # 分割路径，返回路径名和文件扩展名的元组
            if not file_type:
                file_type=None
            file_size = os.path.getsize(file_path)
            file_timetamp=os.path.getmtime(path)  # 时间戳
            timeArray = time.localtime(file_timetamp)
            file_createdate= time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
            file_authority=oct(os.stat(file_path).st_mode)
            print(f'文件名：{file_name},文件大小：{file_size},文件类型：{file_type}, 文件路径: {file_path},文件权限:{file_authority},文件创建日期:{file_createdate}')

if __name__ == '__main__':
    _file = r'E:\temp\test'
    get_size_type(_file)

    # for each_type in type_dict.keys():
    # print("该文件夹下共有【 %s 】的文件【 %d 】个 ,占用内存【 %.2f 】MB" %
    # print(f'文件名：{filename},文件大小：{file_size},文件类型：{file_type}',文件路径:{file_path})
