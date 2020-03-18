#!/user/local/bin/python
# -*- coding:utf-8 -*-
import os
import sys
import uuid

DEBUGMODE = True

currentProjectFilePath = ''


def log(logString):
    if DEBUGMODE:
        print logString
    else:
        return


def deleteUnuseResoure():
    for root, dirs, files in os.walk(currentProjectFilePath):
        for name in dirs:
            if name.startswith("preview"):  # 判断文件夹是否为空
                command = "rmdir /s /q %s" % (os.path.join(root, name))
                log(command)
                os.system(command)


def generateConfigJson():
    for root in os.listdir(currentProjectFilePath):
        rootDir = os.path.join(currentProjectFilePath, root)
        if os.path.isdir(rootDir):
            f = open(rootDir + "\\" + root + ".json", "w+")
            f.write("{")
            for child in os.listdir(rootDir):
                childDir = os.path.join(rootDir, child)
                if os.path.isdir(childDir):
                    if child.startswith("wallpaper"):
                        wallPaperStr = "\"wallpaper\":["
                        unlockWallPaperStr = "\"unlockwallpaper\":["
                        for file in os.listdir(childDir):
                            if file.startswith("home_wallpaper"):
                                wallPaperStr = wallPaperStr + "\"" + file + "\","
                            else:
                                unlockWallPaperStr = unlockWallPaperStr + "\"" + file + "\","
                        f.write(wallPaperStr[0:len(wallPaperStr) - 1])
                        f.write("],")
                        f.write(unlockWallPaperStr[0:len(unlockWallPaperStr) - 1])
                    # elif child.startswith("icon"):
                    #     iconStr = "\"icons\":["
                    #     for file in os.listdir(childDir):
                    #         iconStr = iconStr + "\"" + file + "\","
                    #     f.write(iconStr[0:len(iconStr) - 1])
                    #     f.write("],")
            f.write("]}")
            f.close()


def zipFile():
    for root in os.listdir(currentProjectFilePath):
        command = "7z a %s.zip  -p%s -r %s" % (
            os.path.join(currentProjectFilePath, root), root, os.path.join(currentProjectFilePath, root))
        log(command)
        os.system(command)


if __name__ == '__main__':
    # print '输入参数列表:'
    if len(sys.argv) > 1:
        for index in range(len(sys.argv)):
            if index == 1:
                currentProjectFilePath = sys.argv[index]
    else:
        currentProjectFilePath = os.getcwd()

    # deleteUnuseResoure()
    # generateConfigJson()
    zipFile()
