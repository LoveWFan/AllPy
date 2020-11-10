#!/usr/bin/python3
import re

if __name__ == "__main__":
    str = '''click_music_album
music_play_album
click_album_tongback
click_album_ringtone'''
    split = str.split("\n")
    for subStr in split:
        print(" public static final String " + subStr.upper() + "= \"" + subStr + "\";\n")
