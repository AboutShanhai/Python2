#!user/bin/python
# -*- coding: UTF-8 -*-

def print_import():
    print("fromImportDemo.py import me")


def print_fromImportAll():
    print("fromImportDemo.py from name import * ")


def print_fromImportName():
    print("fromImportDemo.py from name import Name ")


def modelName():
    return __name__     # 返回它自己的名称
