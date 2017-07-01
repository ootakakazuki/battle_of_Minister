import character as c

def print_self_select():
    print("誰を選びますか")
    print("福田首相 : 1")
    print("野田総理 : 2")
    print("森元首相 : 3")
    inp_self = int(input())
    if inp_self == 1:
        y = c.hukuda()
    elif inp_self == 2:
        y = c.Noda()
    elif inp_self == 3:
        y = c.mori()
    return y


def print_target_select():
    print("対戦相手を選ぼう")
    print("福田首相 : 1")
    print("野田総理 : 2")
    print("森元首相 : 3")
    inp_ene = int(input())
    if inp_ene == 1:
        t = c.hukuda()
    elif inp_ene == 2:
        t = c.mori()
    elif inp_ene == 3:
        t = c.Noda()
    return t


def print_command_select(y, t):
    print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
    print("　　　　　　     HP    MP      AT     DE")
    print(y.name + "　"*(6-(len(y.name))), "  ", + y.HP,  "  ",  y.MP, "  " ,y.AT, "  ", y.DE)
    y.status()
    print(t.name + "　"*(6-(len(t.name))), "  " , t.HP, "  " , t.MP, "  " , t.AT, "  ", t.DE)
    t.status()
    print("1 : 攻撃\n2 : チャージ\n3 : 回復\n4 : 特殊攻撃\n", end='')
    if y.name == "野田総理":
        print("5 : 毒技")
    if y.name == "福田首相":
        print("5 : ガチビンタ\n6 : リフレクション")
    inp = int(input("好きなコマンドを入力しよう: "))
    print("---------------------------------------------")
    return inp


def ozisan_kakusei(you, tar):
    if you.name == "森元首相" and you.HP <= 250 and you.kakusei_flg == 0:
        you.AT *= 1.5
        you.kakusei_flg = 1
        print("馬鹿野郎！！！！")
        print("森元首相は覚醒した！")

    if tar.name == "森元首相" and tar.HP <= 250 and tar.kakusei_flg == 0:
        tar.AT *= 1.5
        tar.kakusei_flg = 1
        print("馬鹿野郎！！！！")
        print("森元首相は覚醒した！")


def print_win(tar):
    print(tar.name + "は倒れた！")
    print(tar.ziseinoku)
    print("You WIN!!")


def print_lose(you):
    print(you.name + "は倒れた！")    
    print(you.ziseinoku)
    print("You LOSE...")