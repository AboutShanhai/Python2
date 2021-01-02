#!user/bin/python
# -*- coding: utf-8 -*-

# 相同目录
print "\n\n\n------------------------------List------------------------------"

import fromImportModel
fromImportModel.print_import()              # Yes
fromImportModel.print_fromImportAll()       # Yes
fromImportModel.print_fromImportName()      # Yes
# print_import()                            # No
# print_fromImportAll()                     # No
# print_fromImportName()                    # No
print fromImportModel.modelName()


'''
from fromImportModel import *
fromImportModel.print_import()              # Yes
fromImportModel.print_fromImportAll()       # Yes
fromImportModel.print_fromImportName()      # Yes
print_import()                              # Yes
print_fromImportAll()                       # Yes
print_fromImportName()                      # Yes
'''

'''
from fromImportModel import print_fromImportName
# fromImportModel.print_import()             # No
# fromImportModel.print_fromImportAll()      # No
# fromImportModel.print_fromImportName()     # No
# print_import()                             # No
# print_fromImportAll()                      # No
# print_fromImportName()                     # Yes
'''
print'----------------------------------------------------------------------'

# 不同目录
print '\n\n\n------------------------------UnList------------------------------'

from importFunc import FuntionMode
FuntionMode.print_import()                  # Yes
FuntionMode.print_fromImportAll()           # Yes
FuntionMode.print_fromImportName()          # Yes
# print_import()                            # No
# print_fromImportAll()                     # No
# print_fromImportName()                    # No
print FuntionMode.modelName()


'''
from importFunc.FuntionMode import *
print_import()                              # Yes
print_fromImportAll()                       # Yes
print_fromImportName()                      # Yes
print modelName()
'''
print '----------------------------------------------------------------------'
