#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/18 10:26
# @Author  : Ktry
# @Site    : 
# @File    : test.py
# @Software: PyCharm Community Edition

import web

urls = ('/hello', 'hello',)


def test():
    print 'success'


class hello(object):
    def GET(self):
        return 'hello world'


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
