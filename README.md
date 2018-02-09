# Python-OOP-Test
### Python 面向对象尝试

#### 10:00 PM, Feb 9th, 2018 @ dormitory

- 发现 __self 不是固定名称__，可以取符合变量规则的任意名称

  ```python
  	  def __init__(selfhappy, name):
          selfhappy.name = name
          print('(Initializing {0})'.format(selfhappy.name))
          Robot.population += 1

      def sayHi(selfhappy):
          print('Greeting, my master call me {0}.'.format(selfhappy.name))
  ```

  比如把 self 改为 selfhappy , 程序正常运行

- __声明类方法__，有2种方法

  1. 用 @classmethod 语句

     ```python
         @classmethod
         def howMany(itdoesntmater):
             print('We have {0:d} robots.'.format(Robot.population))
     ```

  2. 用内置的 classmethod() 函数

     ```python
         def howMany(itdoesntmater):
             print('We have {0:d} robots.'.format(Robot.population))
         howMany = classmethod(howMany)  
     ```
