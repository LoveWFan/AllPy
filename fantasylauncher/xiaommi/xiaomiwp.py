#!/user/local/bin/python
# -*- coding:utf-8 -*-
import os
import sys
import zipfile
import time
import platform
import uuid

DEBUGMODE = True

currentProjectFilePath = ''
quality = "75"


def unzip():
    for root, dirs, files in os.walk(currentProjectFilePath):
        for name in files:
            if name.endswith(".mtz"):
                command = "7z x -tZip -y %s -o%s" % (
                    os.path.join(root, name), os.path.join(root, uuid.uuid3(uuid.NAMESPACE_DNS, name).__str__()))
                log(command)
                os.system(command)
                command = "del %s\\%s " % (root, name)
                log(command)
                os.system(command)


def extactWallPaper():
    for root, dirs, files in os.walk(currentProjectFilePath):
        for name in files:
            if "wallpaper.jpg" in name:
                fullname = os.path.join(root, name);
                str = fullname[0:fullname[0:fullname.rindex("\\")].rindex("\\")]
                command = "copy %s %s" % (os.path.join(root, name), currentProjectFilePath + "\\wallPaper\\" + str[
                                                                                                               str.rindex(
                                                                                                                   "\\") + 1:len(
                                                                                                                   str)] + "_" + name)
                log(command)
                os.system(command)

def extactWallPaper():
    for root, dirs, files in os.walk(currentProjectFilePath):
        for name in files:
            if "wallpaper.jpg" in name:
                fullname = os.path.join(root, name);
                str = fullname[0:fullname[0:fullname.rindex("\\")].rindex("\\")]
                command = "copy %s %s" % (os.path.join(root, name), currentProjectFilePath + "\\wallPaper\\" + str[
                                                                                                               str.rindex(
                                                                                                                   "\\") + 1:len(
                                                                                                                   str)] + "_" + name)
                log(command)
                os.system(command)

def compress(filePath):
    if os.path.isfile(filePath):
        split_name = os.path.splitext(filePath)
        if split_name[1] == ".webp" or (split_name[1] != ".jpg" and split_name[1] != ".png"):
            return
        command = "cwebp -q " + quality + " " + filePath + " -o " + \
                  split_name[0] + ".webp"

        log(command)
        os.system(command)
        command = "del %s" % (filePath)
        log(command)
        os.system(command)


def compressFolder():
    for root, dirs, files in os.walk(currentProjectFilePath):
        for name in files:
            compress(os.path.join(root, name))


def getJson():
    jsonStr = "{\"data\":["
    for name in os.listdir(currentProjectFilePath):
        new_path = os.path.join(currentProjectFilePath, name)
        if os.path.isfile(new_path):
            jsonStr = jsonStr \
                      + ("{\"id\":\"" + name[0:name.rindex(".")] + "\",") \
                      + ("\"wallPaperId\":\"" + name[0:name.rindex(".")] + "\",") \
                      + (
                              "\"previewUrl\":\"https://firebasestorage.googleapis.com/v0/b/fantasylauncher-7dec8.appspot.com/o/wallpaper%2Fpreview%2F" + name + "?alt=media" + "\",") \
                      + ("\"type\":0,") \
                      + ("\"tag\":\"\",") \
                      + ("\"free\":true,") \
                      + ("\"ver\":0") \
                      + "},"

    print jsonStr[0:len(jsonStr) - 1] + "]}"


def log(logString):
    if DEBUGMODE:
        print logString
    else:
        return


if __name__ == '__main__':
    # print '输入参数列表:'
    if len(sys.argv) > 1:
        for index in range(len(sys.argv)):
            if index == 1:
                currentProjectFilePath = sys.argv[index]
    else:
        currentProjectFilePath = os.getcwd()

    # unzip()
    # extactWallPaper()
    # compressFolder()
    # getJson()
