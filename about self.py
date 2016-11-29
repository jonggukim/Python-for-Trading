class test:
    def func1():
        print("funtion 1111")
    def func2(self):
        print(id(self))
        print("funtion 222")


f = test()
f.func2()


print(id(f))

test.func1()
id(test.func1())