#! /usr/bin/python3
# coding=utf-8


import re
import sys

# 年份
years = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
# 关键字，比如域名www.baidu.com，关键字就可以是bd，BD，Bd
keywords = ['dftb', 'Dftb', 'dfc', 'DFC', 'Dfc', 'dongfangcheng']


def main():
    # 获取域名
    domain = sys.argv[1]
    if re.match(r'https?://www', domain):
        key1 = domain.split('.')[1]
    else:
        print('输入格式:python3 generatePass.py http://www.xxx.com 子域名单词(可以没有)')
        print('example1 : python3 generatePass.py http://www.baidu.com')
        print('example2 : python3 generatePass.py http://www.baidu.com qq')
        sys.exit()

    # 获取子域名单词
    try:
        sys.argv[2]
    except:
        subdomain = ''
    else:
        subdomain = sys.argv[2]

    # 域名后加上键盘规律的字典
    keyboards = get_keyboards()
    generate_pass(key1, keyboards)

    # 年份字典
    generate_pass(key1, years)
    generate_pass1(key1, years)

    # 自定义字符串字典
    custom_words = open_customwords()
    generate_pass(key1, custom_words)

    # 关键字字典
    if keywords != '':
        for i in keywords:
            generate_pass(i, keyboards)
            generate_pass(i, years)
            generate_pass1(i, years)
            generate_pass(i, custom_words)

    # 子域名字典
    if subdomain != '':
        generate_pass(subdomain, keyboards)
        generate_pass(subdomain, years)
        generate_pass1(subdomain, years)
        generate_pass(subdomain, custom_words)
        generate_subpass(key1, subdomain, keywords, years)


#  获取键盘规律的字典
def get_keyboards():
    with open('keyboards.txt') as f:
        strs = [i.strip() for i in f.readlines()]
    return strs


# 普通字典生成(domain + list)
def generate_pass(str, lists):
    with open('passwords.txt','a') as f:
        for i in lists:
            f.write(str + i + '\n')


# 追加字符字典(domain + year + char)
def generate_pass1(str, lists):
    with open('passwords.txt', 'a') as f:
        for i in lists:
            f.write(str + i + '@' + '\n')
            f.write(str + i + '!' + '\n')
            f.write(str + i + '#' + '\n')
            f.write(str + i + '$' + '\n')
            f.write(str + i + '%' + '\n')
            f.write(str + i + '^' + '\n')
            f.write(str + i + '&' + '\n')
            f.write(str + i + '*' + '\n')
            f.write(str + i + '(' + '\n')
            f.write(str + i + ')' + '\n')
            f.write(str + i + '-' + '\n')
            f.write(str + i + '_' + '\n')
            f.write(str + i + '=' + '\n')
            f.write(str + i + '!@' + '\n')
            f.write(str + i + '@!' + '\n')
            f.write(str + i + '!@!' + '\n')
            f.write(str + i + '@!@' + '\n')
            f.write(str + i + '!@#' + '\n')
            f.write(str + i + '#@!' + '\n')
            f.write(str + i + '#!@' + '\n')
            f.write(str + i + '@!#' + '\n')
            f.write(str + i + '@#!' + '\n')
            f.write(str + i + '!@#$' + '\n')
            f.write(str + i + '$#@!' + '\n')
            f.write(str + '!' + i + '\n')
            f.write(str + '@' + i + '\n')
            f.write(str + '#' + i + '\n')
            f.write(str + '$' + i + '\n')
            f.write(str + '%' + i + '\n')
            f.write(str + '^' + i + '\n')
            f.write(str + '&' + i + '\n')
            f.write(str + '*' + i + '\n')
            f.write(str + '(' + i + '\n')
            f.write(str + ')' + i + '\n')
            f.write(str + '-' + i + '\n')
            f.write(str + '_' + i + '\n')
            f.write(str + '=' + i + '\n')
            f.write(str + '!@' + i + '\n')
            f.write(str + '@!' + i + '\n')
            f.write(str + '!@!' + i + '\n')
            f.write(str + '@!@' + i + '\n')
            f.write(str + '!@#' + i + '\n')
            f.write(str + '!#@' + i + '\n')
            f.write(str + '@!#' + i + '\n')
            f.write(str + '@#!' + i + '\n')
            f.write(str + '#@!' + i + '\n')
            f.write(str + '#!@' + i + '\n')
            f.write(str + '!@#$' + i + '\n')
            f.write(str + '$#@!' + i + '\n')


# 打开自定义字符串文件
def open_customwords():
    with open('custom_words.txt', 'r') as f:
        strs = [i.strip() for i in f.readlines()]
    return strs


def generate_subpass(domain, subdomain, lists, years):
    with open('passwords.txt', 'a') as f:
        f.write(subdomain + '.' + domain + '\n')
        f.write(subdomain + '.' + domain + '.com' + '\n')
        for i in lists:
            f.write(i + subdomain + '\n')
            f.write(i + subdomain + '!' + '\n')
            f.write(i + subdomain + '@' + '\n')
            f.write(i + subdomain + '#' + '\n')
            f.write(i + subdomain + '$' + '\n')
            f.write(i + subdomain + '%' + '\n')
            f.write(i + subdomain + '^' + '\n')
            f.write(i + subdomain + '&' + '\n')
            f.write(i + subdomain + '*' + '\n')
            f.write(i + subdomain + '(' + '\n')
            f.write(i + subdomain + ')' + '\n')
            f.write(i + subdomain + '-' + '\n')
            f.write(i + subdomain + '_' + '\n')
            f.write(i + subdomain + '=' + '\n')
            f.write(i + subdomain + '!@' + '\n')
            f.write(i + subdomain + '@!' + '\n')
            f.write(i + subdomain + '!@!' + '\n')
            f.write(i + subdomain + '@!@' + '\n')
            f.write(i + subdomain + '!@#' + '\n')
            f.write(i + subdomain + '!#@' + '\n')
            f.write(i + subdomain + '@!#' + '\n')
            f.write(i + subdomain + '@#!' + '\n')
            f.write(i + subdomain + '#@!' + '\n')
            f.write(i + subdomain + '#!@' + '\n')
            f.write(i + subdomain + '!@#$' + '\n')
            f.write(i + subdomain + '$#@!' + '\n')
            f.write(i + '!' + subdomain + '\n')
            f.write(i + '@' + subdomain + '\n')
            f.write(i + '#' + subdomain + '\n')
            f.write(i + '$' + subdomain + '\n')
            f.write(i + '%' + subdomain + '\n')
            f.write(i + '^' + subdomain + '\n')
            f.write(i + '&' + subdomain + '\n')
            f.write(i + '*' + subdomain + '\n')
            f.write(i + '(' + subdomain + '\n')
            f.write(i + ')' + subdomain + '\n')
            f.write(i + '-' + subdomain + '\n')
            f.write(i + '_' + subdomain + '\n')
            f.write(i + '=' + subdomain + '\n')
            f.write(i + '!@' + subdomain + '\n')
            f.write(i + '@!' + subdomain + '\n')
            f.write(i + '!@!' + subdomain + '\n')
            f.write(i + '@!@' + subdomain + '\n')
            f.write(i + '!@#' + subdomain + '\n')
            f.write(i + '!#@' + subdomain + '\n')
            f.write(i + '@!#' + subdomain + '\n')
            f.write(i + '@#!' + subdomain + '\n')
            f.write(i + '#@!' + subdomain + '\n')
            f.write(i + '#!@' + subdomain + '\n')
            f.write(i + '!@#$' + subdomain + '\n')
            f.write(i + '$#@!' + subdomain + '\n')
        for i in lists:
            for j in years:
                f.write(i + subdomain + j + '\n')
                f.write(i + subdomain + j + '!' + '\n')
                f.write(i + subdomain + j + '@' + '\n')
                f.write(i + subdomain + j + '#' + '\n')
                f.write(i + subdomain + j + '$' + '\n')
                f.write(i + subdomain + j + '%' + '\n')
                f.write(i + subdomain + j + '^' + '\n')
                f.write(i + subdomain + j + '&' + '\n')
                f.write(i + subdomain + j + '*' + '\n')
                f.write(i + subdomain + j + '(' + '\n')
                f.write(i + subdomain + j + ')' + '\n')
                f.write(i + subdomain + j + '-' + '\n')
                f.write(i + subdomain + j + '_' + '\n')
                f.write(i + subdomain + j + '=' + '\n')
                f.write(i + subdomain + j + '!@' + '\n')
                f.write(i + subdomain + j + '@!' + '\n')
                f.write(i + subdomain + j + '!@!' + '\n')
                f.write(i + subdomain + j + '@!@' + '\n')
                f.write(i + subdomain + j + '!@#' + '\n')
                f.write(i + subdomain + j + '!#@' + '\n')
                f.write(i + subdomain + j + '@!#' + '\n')
                f.write(i + subdomain + j + '@#!' + '\n')
                f.write(i + subdomain + j + '#@!' + '\n')
                f.write(i + subdomain + j + '#!@' + '\n')
                f.write(i + subdomain + j + '!@#$' + '\n')
                f.write(i + subdomain + j + '$#@!' + '\n')
                f.write(i + '!' + subdomain + j + '\n')
                f.write(i + '@' + subdomain + j + '\n')
                f.write(i + '#' + subdomain + j + '\n')
                f.write(i + '$' + subdomain + j + '\n')
                f.write(i + '%' + subdomain + j + '\n')
                f.write(i + '^' + subdomain + j + '\n')
                f.write(i + '&' + subdomain + j + '\n')
                f.write(i + '*' + subdomain + j + '\n')
                f.write(i + '(' + subdomain + j + '\n')
                f.write(i + ')' + subdomain + j + '\n')
                f.write(i + '-' + subdomain + j + '\n')
                f.write(i + '_' + subdomain + j + '\n')
                f.write(i + '=' + subdomain + j + '\n')
                f.write(i + '!@' + subdomain + j + '\n')
                f.write(i + '@!' + subdomain + j + '\n')
                f.write(i + '!@!' + subdomain + j + '\n')
                f.write(i + '@!@' + subdomain + j + '\n')
                f.write(i + '!@#' + subdomain + j + '\n')
                f.write(i + '!#@' + subdomain + j + '\n')
                f.write(i + '@!#' + subdomain + j + '\n')
                f.write(i + '@#!' + subdomain + j + '\n')
                f.write(i + '#@!' + subdomain + j + '\n')
                f.write(i + '#!@' + subdomain + j + '\n')
                f.write(i + '!@#$' + subdomain + j + '\n')
                f.write(i + '$#@!' + subdomain + j + '\n')


if __name__ == '__main__':
    main()