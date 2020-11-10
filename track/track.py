#!/usr/bin/python3
import re
if __name__ == "__main__":
    str = '''点击游戏战绩入口	me_game_record_click
最近战绩页面展示	me_recent_record_page_show
总战绩页面展示	me_total_record_page_show
最近战绩页面的头像点击	me_recent_record_avatar_click'''
    split = str.split("\n")
    for subStr in split:

        re_split = re.split('\s+', subStr)

        print("//" + re_split[0])
        print(" public static final String " + re_split[1].upper() + "= \"" + re_split[1] + "\";\n")
