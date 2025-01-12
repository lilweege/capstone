#coding:utf-8

if __name__ == '__main__':

    for i in range(1,10):
        for j in range(1,10):
            message = str(i)
            message += "x"
            message += str(j)
            message += "="
            message += str(i*j)
            print(message)