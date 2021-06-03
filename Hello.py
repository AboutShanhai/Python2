#!user/bin/python
# -*- coding: UTF-8 -*-

print('Hello World!')

import re

pattern = re.compile(ur'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
str = u'当前 IP：35.241.80.59  来自于：中国 香港   cloud.google.com'
m = pattern.search(str)
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.group(4))
