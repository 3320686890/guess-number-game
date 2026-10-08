import random
print("欢迎来玩猜数字小游戏")
print("现在，电脑已经生成了一个随机数")
number = random.randint(1,100)
count = 0
while    True: 
          figure = input("请您输入一个数字")
          if not figure.isdigit():
                  print("你打的啥啊喂")
                  continue
          word = int (figure)
          if word > 100 or word < 1:
                  print("范围没设那么广，只有1到100")
                  continue
          count += 1
          if word > number:
                  print("猜大了")
          elif word < number:
                  print("猜小了")
          else :
                  print(f"猜对啦，就是{number}")
                  print(f"你一共猜了{count}次")
                  if count <= 3:
                          print("哇塞，厉害啊")
                  elif 3 < count <10:
                          print("不错不错")
                  else :
                          print("可惜可惜")
                  break
                        