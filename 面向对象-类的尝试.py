# 10:00 PM, Feb 9th, 2018 @ dormitory
# 面向对象， 类的尝试
# 发现 self 不是固定名称

class Robot:
    population = 0
    def __init__(selfuck, name):
        selfuck.name = name
        print('(Initializing {0})'.format(selfuck.name))
        Robot.population += 1

    def sayHi(selfuck):
        print('Greeting, my master call me {0}.'.format(selfuck.name))

    @classmethod
    def howMany(itdoesntmater):
        print('We have {0:d} robots.'.format(Robot.population))
    # 声明 howMany() 为类方法
    # 可以用 @classmethod， 也可以用以下语句
    # howMany = classmethod(howMany)

pass
# Alpha1 = Robot('Alpha1')
# Alpha2 = Robot('Alpha2')
# Alpha1.sayHi()
# Robot.howMany()
