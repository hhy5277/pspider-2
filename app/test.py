#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Created on    : 2019-03-11 22:41
# @Author  : zpy
# @Software: PyCharm


from app.task import Task

class App(object):

    @staticmethod
    def task(bind=True, **kwargs):
        def skr(func, **kwargs):
            print('start',kwargs)
            func(**kwargs)
            print('end')
            return
        return skr

class TestTask(Task):

    def start(self):
        print('skr skr')


if __name__ == '__main__':
    TestTask.app = App()
    TestTask().ptask(skr='skr')