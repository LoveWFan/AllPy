#!/usr/bin/python3

import xml.sax


class ShapeHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.gradient = ""
        self.corners = ""
        self.solid = ""

    # 元素开始调用
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "gradient":
            # bl_gradient_angle	integer
            # bl_gradient_centerX	float
            # bl_gradient_centerY	float
            # bl_gradient_centerColor	color
            # bl_gradient_endColor	color
            # bl_gradient_startColor	color
            # bl_gradient_gradientRadius	dimension
            # bl_gradient_type	linear、radial、sweep
            # bl_gradient_useLevel
            print("app:bl_gradient_type=", "\"" + attributes["android:type"] + "\"")
            print("app:bl_gradient_startColor=", "\"" + attributes["android:startColor"] + "\"")
            print("app:bl_gradient_endColor=", "\"" + attributes["android:endColor"] + "\"")
            print("app:bl_gradient_angle=", "\"270\"")
        if tag == "solid":
            # bl_solid_color color
            print("app:bl_solid_color=", "\"" + attributes["android:color"] + "\"")
        if tag == "corners":
            # bl_corners_radius dimension
            attrilibs = attributes.getNames()
            if 'android:radius' in attrilibs:
                print("app:bl_corners_radius=", "\"" + attributes["android:radius"] + "\"")
            if 'android:bottomLeftRadius' in attrilibs:
                print("app:bl_corners_bottomLeftRadius=", "\"" + attributes["android:bottomLeftRadius"] + "\"")
            if 'android:bottomRightRadius' in attrilibs:
                print("app:bl_corners_bottomRightRadius=", "\"" + attributes["android:bottomRightRadius"] + "\"")
            if 'android:topLeftRadius' in attrilibs:
                print("app:bl_corners_topLeftRadius=", "\"" + attributes["android:topLeftRadius"] + "\"")
            if 'android:topRightRadius' in attrilibs:
                print("app:bl_corners_topRightRadius=", "\"" + attributes["android:topRightRadius"] + "\"")

# 元素结束调用
def endElement(self, tag):
    self.CurrentData = ""


# 读取字符时调用
def characters(self, content):
    if self.CurrentData == "gradient":
        self.gradient = content
    elif self.CurrentData == "corners":
        self.corners = content
    elif self.CurrentData == "solid":
        self.solid = content


if (__name__ == "__main__"):
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # 关闭命名空间
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = ShapeHandler()
    parser.setContentHandler(Handler)

    parser.parse("demo.xml")
