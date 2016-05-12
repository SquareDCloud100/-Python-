#-*- coding: UTF-8 -*-#

class calculate:
    def sum(self, *args):      # *args 가 n개의 변수를 받아들일 때 사용
        total = 0
        for item in args:
            total += item
        return total;

    def sub(self,a,b):
        return a-b

    def multi(self, *args):
        total = 1 
        for item in args:
            total *= args 
        return total
