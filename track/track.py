#!/usr/bin/python3
import re
if __name__ == "__main__":
    str = '''点击“我的钱包”入口	me_wallet_click
钻石充值页面展示	me_diamond_recharge_show
充值档位点击	me_diamond_recharge_click
点击“确认充值”	me_diamond_recharge_confirm_click
充值成功	me_diamond_recharge_success
充值失败	me_diamond_recharge_fail
金币兑换页面展示	me_coin_exchange_click
兑换档位点击	me_coin_exchange_click
点击“确认充值”	me_coin_exchange_confirm_click
兑换成功	me_coin_exchange_success
兑换失败	me_coin_exchange_fail
从钱包页面返回上一级	me_wallet_out
点击官方QQ群的“复制”按钮	me_qq_copy_click'''
    split = str.split("\n")
    for subStr in split:

        re_split = re.split('\s+', subStr)

        print("//" + re_split[0])
        print(" public static final String " + re_split[1].upper() + "= \"" + re_split[1] + "\";\n")
