#!/user/local/bin/python
# -*- coding:utf-8 -*-
import os
import sys
import uuid
from googletrans import Translator

DEBUGMODE = True

currentProjectFilePath = ''
quality = "75"


def unzipIcons():
    for root, dirs, files in os.walk(currentProjectFilePath):
        for name in files:
            if name.startswith("icons"):
                command = "7z x -tZip -y %s -o%s" % (
                    os.path.join(root, name), os.path.join(root, "icon"))
                log(command)
                os.system(command)
                command = "del %s\\%s " % (root, name)
                log(command)
                os.system(command)


def renameTheme():
    for root in os.listdir(currentProjectFilePath):
        rootDir = os.path.join(currentProjectFilePath, root)
        if os.path.isdir(rootDir):
            themeId = uuid.uuid3(uuid.NAMESPACE_DNS, root).__str__()
            command = rootDir + "," + os.path.join(currentProjectFilePath, themeId)
            log(command)
            os.rename(rootDir, os.path.join(currentProjectFilePath, themeId))


def extactThemePreview():
    for root, dirs, files in os.walk(currentProjectFilePath):
        for name in files:
            if name.startswith("preview_") or name.startswith("default_lock_wallpaper"):
                fullname = os.path.join(root, name);
                str = fullname[0:fullname[0:fullname.rindex("\\")].rindex("\\")]
                command = "move %s %s" % (os.path.join(root, name), currentProjectFilePath[
                                                                    0:currentProjectFilePath.rindex(
                                                                        "\\")] + "\\rawThemePreview\\" + str[
                                                                                                         str.rindex(
                                                                                                             "\\") + 1:len(
                                                                                                             str)] + "_" + name)
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
            if name.endswith(".jpg") or name.endswith(".png"):
                fileName = os.path.join(root, name);
                if "fancy_icons" not in fileName:
                    compress(os.path.join(root, name))


def getJson():
    translator = Translator()  # initalize the Translator object
    jsonStr = ""
    for name in os.listdir(currentProjectFilePath):
        rootDir = os.path.join(currentProjectFilePath, name)
        if os.path.isdir(rootDir):
            themeId = uuid.uuid3(uuid.NAMESPACE_DNS, name).__str__()
            themeName = name.decode("gbk").encode("utf-8")
            if "+" in themeName:
                split = themeName.split("+")
                themeName = ""
                for str in split:
                    themeName = themeName + str

            translate_result = translator.translate(themeName, dest='en').text
            print translate_result
            jsonStr = jsonStr \
                      + ("{\"id\":\"" + themeId + "\",") \
                      + ("\"name\":\"" + translate_result + "\",") \
                      + ("\"themeId\":\"" + themeId + "\",") \
                      + ("\"previewUrls\":[")
            previewStr = "\"https://storage.googleapis.com/fantasylauncer/wallpaper/preview/" + themeId + "_" + "default_lock_wallpaper.webp" + "\","
            if os.path.isdir(os.path.join(rootDir, "preview")):
                for preview in os.listdir(os.path.join(rootDir, "preview")):
                    previewStr = previewStr + "\"https://storage.googleapis.com/fantasylauncer/wallpaper/preview/" + themeId + "_" + preview + "\","
            jsonStr = jsonStr + previewStr[0:len(previewStr) - 1]
            jsonStr = jsonStr + "],"
            jsonStr = jsonStr + (
                    "\"zipUrl\":\"https://storage.googleapis.com/fantasylauncer/wallpaper/preview/" + themeId + ".zip" + "\",") \
 \
                      + ("\"themeOS\":1,") \
                      + ("\"type\":0,") \
                      + ("\"tag\":\"\",") \
                      + ("\"free\":true,") \
                      + ("\"ver\":0,") \
                      + ("\"screenshotType\":0") \
                      + "},"
    print jsonStr


def deleteUnUseResource():
    for name in os.listdir(currentProjectFilePath):
        rootDir = os.path.join(currentProjectFilePath, name)
        if os.path.isdir(rootDir):
            for name in os.listdir(rootDir):
                if os.path.isfile(os.path.join(rootDir, name)) and not name.startswith("lockscreen"):
                    command = "del %s" % (os.path.join(rootDir, name))
                    log(command)
                    os.system(command)
            if os.path.isdir(os.path.join(rootDir, "preview")):
                for name in os.listdir(os.path.join(rootDir, "preview")):
                    if name.startswith("preview_launcher") or (
                            name.startswith("preview_icons") and not name.startswith("preview_icons_small")):
                        continue
                    else:
                        command = "del %s" % (os.path.join(rootDir, "preview\\" + name))
                        log(command)
                        os.system(command)


def zipFile():
    for root in os.listdir(currentProjectFilePath):
        command = "7z a %s.zip  -p%s -r %s" % (
            os.path.join(currentProjectFilePath, root), root, os.path.join(currentProjectFilePath, root))
        log(command)
        os.system(command)


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

    # unzipIcons()
    # deleteUnUseResource()
    # compressFolder()
    # getJson()
    renameTheme()
    extactThemePreview()
    generateConfigJson()
    zipFile()
