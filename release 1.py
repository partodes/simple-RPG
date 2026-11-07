import time
import random
player_time=2
class character:
    def __init__(self,name,damage,hp):
        self.name= name
        self.damage=damage
        self.hp=hp
    def attack(self,target):
        target.hp -= self.damage
        if target.hp <0:
            target.hp = 0
        print(f'{self.name}发动攻击，{target.name}还剩{target.hp}滴血')
class player(character):
    def special_attack(self,target):
        global player_time
        player_time-= 1
        target.hp -= 30
        if target.hp < 0:
            target.hp = 0
        print(f'{self.name}对{target.name}发动特殊攻击')
    def run(self):
        self.poss = random.randint(1,2)
        if self.poss == 1:
            print('逃跑成功')
        else:
            print('逃跑失败')    
class monster(character):
    def realive(self):
        self.hp +=10
        if self.hp > 150:
            self.hp = 150
        print(f'{self.name}发动回血,还剩{self.hp}滴血')                                    
    def strike(self,target):
        target.hp -= self.damage*1.5
        if target.hp < 0:
            target.hp = 0
        print(f'{self.name}发动重击,{target.name}还剩{target.hp}滴血')
p = player(input('输入名字>>>'),15,100) 
m1 = monster('slime',20,150)
m2 = monster('goblin',20,150)
print('游戏开始！')
while True:
    print(f'''
    {m1.name}剩余血量{m1.hp}
    {m2.name}剩余血量{m2.hp}
    {p.name}剩余血量{p.hp}
    ---------------------------------''') 
    cho = input(f'''对决选择
    1:普通攻击造成两只怪物15滴血
    2:特殊攻击造成两只怪物30滴血，{player_time}次机会
    3:逃跑，50%成功率
    ---------------------------------
    >>>''')
    if not cho.isdigit():
        print('请输入正确指令')
        continue
    else:
        cho = int(cho)
    if cho == 1:
        if m1.hp <=0 and m2.hp > 0:
            p.attack(m2)
        elif m2.hp <= 0 and m1.hp>0:
            p.attack(m1)
        else:
            attack_choose = random.randint(1,2)
            if attack_choose == 1:
                print(f'选择了{m1.name}')
                p.attack(m1)
            if attack_choose == 2:
                print(f'选择了{m2.name}')
                p.attack(m2)    
    elif cho == 2:
        if player_time == 0:
            print('次数用完，请重新选择')
            continue
        if m1.hp <=0 and m2.hp > 0:
            p.special_attack(m2)
        elif m2.hp <= 0 and m1.hp>0:
            p.special_attack(m1)
        else:
            attack_choose = random.randint(1,2)
            if attack_choose == 1:
                print(f'选择了{m1.name}')
                p.special_attack(m1)
            if attack_choose == 2:
                print(f'选择了{m2.name}')
                p.special_attack(m2)
    elif cho == 3:
        p.run()
        if p.poss == 1:
            break
    else:
        print('指令错误，回合重置，请输入1-3数字')
        continue    
    print('''玩家回合结束，接下来怪物出手
    --------------------------''')
    if m1.hp<=0 and m2.hp>0:
        print(f'检测{m1.name}被击败，{m2.name}进入战斗')                    
        m2_cho =random.randint(1,2)
        if m2_cho == 1:
            m2.attack(p)
        else:
            m2.strike(p)
    if m2.hp<= 0 and m1.hp > 0:
        print(f'检测{m2.name}被击败，{m1.name}进入战斗')
        m1_cho = random.randint(1,2)
        if m1_cho == 1:
            m1.attack(p)
        else:
            m1.realive()
    if m2.hp > 0 and m1.hp > 0:
        print('怪兽随机加入游戏')
        time.sleep(2)
        mos_cho = random.randint(1,2)
        if mos_cho == 1:
            print(f'{m1.name}参与进攻')
            m1_cho = random.randint(1,2)
            if m1_cho == 1:
                m1.attack(p)
            if m1_cho == 2:
                m1.realive()
        else:
            print(f'{m2.name}参与进攻')
            m2_cho = random.randint(1,2)
            if m2_cho==1:
                m2.attack(p)
            if m2_cho == 2:
                m2.strike(p)


    if p.hp <=0:
        print(f'''游戏结束，怪物获胜
        {m1.name}:{m1.hp}滴血
        {m2.name}:{m2.hp}滴血''')
        break
    if m1.hp <=0 and m2.hp <= 0:
        print(f'''游戏结束，玩家获胜
        {p.name}:{p.hp}滴血''')    
        break    
                
                    
    
    
              
           
    