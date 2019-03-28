from numpy.random import *
import character as c
import view as v
import status_action as st

def main():
    you = v.print_self_select()  # 自分が操作するキャラクターを選ぶ
    tar = v.print_target_select()  # 対戦相手を選ぶ
    print(tar.name + "が現れた！")
    ref_count = 0  # リフレクターのためにターンを数えるカウンター
    while 1:  # 以下ループ
        inp = v.print_command_select(you, tar)
        inp = st.you_status(you, inp)
        st.you_action(you, tar, inp, ref_count)

        # 敵の行動を乱数で出す
        if tar.name == "野田総理":
            a = randint(1, 6)
        elif tar.name == "福田首相":
            a = randint(1, 7)
        else:
            a = randint(1, 5)
        a = st.ene_status(a, tar)
        if tar.HP <= 0:
            v.print_win(tar)
            break
        st.ene_action(a, you, tar, ref_count)
        # 敵の行動後に体力が0になる場合もあるため(反動ダメージなど)
        if tar.HP <= 0:
            v.print_win(tar)
            break
        if you.HP <= 0:
            v.print_lose(you)
            break
        v.mori_kakusei(you, tar)  # 森元首相覚醒する表示
        ref_count += 1
        print(str(ref_count) + "ターン目")
        if you.reflect_flg == 1 and ref_count - you.ref_count ==6:  # リフレクト処理
            you.reflect_flg = 0
            you.DE /= 2
            print(you.name + "のリフレクトが消えた！")


if __name__ == "__main__":
    main()
