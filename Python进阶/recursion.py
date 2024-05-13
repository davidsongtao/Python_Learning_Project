"""
演示Python递归操作
需求： 通过递归，找出一个指定文件夹内的全部文件

思路：写一个函数，列出文件夹内的全部内容，如果是文件就收集到list,
如果是文件夹，就递归调用自己，再次判断
"""
import os


def test_os():
    """演示os模块的三个基础用法"""
    print(os.listdir("/home/songtao/Documents/test"))  # 列出目标目录里的全部内容
    print(os.path.isdir("/home/songtao/Documents/test/a"))  # 判断目标路径是否是一个文件夹
    print(os.path.exists("/home/songtao/Documents/test/a"))  # 判断目标路径是否存在


def get_files_list(path):
    """
    从指定的文件夹中使用递归的方式，获取全部的文件列表
    :param path: 被判断的文件夹
    :return: list,包含全部的文件，如果目录不存在或者无文件就返回一个空list
    """
    files_list = []
    if os.path.exists(path):  # 判断传入的路径是否存在
        # 路径存在，列出所有文件,判断列出的文件里是文件还是文件夹，如果是文件，放入list，如果是文件夹，递归调用自己
        for content in os.listdir(path):
            new_path = path + "/" + content  # 重新组装新的文件夹路径
            if os.path.isdir(new_path):
                # 是文件夹，递归调用自己，传入新path
                files_list += get_files_list(new_path)
            else:
                files_list.append(new_path)  # 如果是文件，直接加入list
    else:
        print(f"指定的目录{path}不存在。")  # 路径不存在，打印错误提示

    return files_list


if __name__ == '__main__':
    print(get_files_list("/home/songtao/Documents/test"))
