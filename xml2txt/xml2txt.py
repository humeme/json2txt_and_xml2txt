#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/1/23 17:40
# @Author    : humeme
# @Site      : retoo
# @File      : xml2txt.py
# @Software: PyCharm

import os
import json
import xml.etree.ElementTree as xml_tree
import glob
path1 = "C:/D-text/Demo/_01_code/_02_python/_01_freTime_test/xml2txt/XML/"
path2 = "C:/D-text/Demo/_01_code/_02_python/_01_freTime_test/xml2txt/X03txt/"
files = glob.glob (path1 + '*.xml')

def int_float(x):
    return int(float(x))
for file in files:
    direct = file.replace("\\","/").split("/")[-1].replace("xml","txt")
    with open(os.path.join(path2+direct), "w") as f:
        #content = xml.loads(open(file, "r"))
        tree = xml_tree.parse(file)
        root = tree.getroot()

        # Image shape.
        size = root.find('size')
        shape = [int(size.find('height').text),
                 int(size.find('width').text),
                 int(size.find('depth').text)]
        # Find annotations.
        bboxes = []
        labels = []
        labels_text = []
        difficult = []
        truncated = []
        for obj in root.findall('object'):
            label = int(obj.find('name').text)
            isdifficult = obj.find('difficult')
            if isdifficult is not None:
                difficult.append(int(isdifficult.text))
            else:
                difficult.append(0)

            istruncated = obj.find('truncated')
            if istruncated is not None:
                truncated.append(int(istruncated.text))
            else:
                truncated.append(0)
            bbox1 = list(obj.find ('polygen').find("points_x").text.strip().split(",")[0:4])
            bbox2 = list(obj.find ('polygen').find("points_y").text.strip().split(",")[0:4])
            box = list(zip(bbox1, bbox2))
            str1 = "{},{},{},{},{},{},{},{},{}".format(int_float(box[0][0]), int_float(box[0][1]), int_float(box[1][0]), int_float(box[1][1]), \
                                                       int_float(box[2][0]),int_float(box[2][1]), int_float(box[3][0]), int_float(box[3][1]),
                                                       label)
            f.write (str1 + "\n")
    f.close()
print ("success")