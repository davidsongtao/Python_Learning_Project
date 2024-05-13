import re


def is_valid_email(email):
    # 电子邮件地址的正则表达式
    # 用户名只允许字母、数字、下划线、点
    # 域名由字母和数字组成
    # 顶级域名可以包含字母、数字、点和减号
    pattern = r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$'
    # 使用re.match来匹配邮箱地址
    if re.match(pattern, email):
        print("符合要求")
        return True
    else:
        print("错误！")
        return False


# 测试
email = "david.songtao@hotmail.com"
is_valid_email(email)  # 应该输出True
