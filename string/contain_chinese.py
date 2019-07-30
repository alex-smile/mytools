#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: alex-smile
# @date: 20190730

import os
import sys
import re


chinese_pattern = re.compile(u"[\u4e00-\u9fa5]+")


def is_file_contain_chinese(fpath):
    """
    Determine whether the content of the file contains Chinese.
    Returns True if it contains Chinese, otherwise returns False
    """
    with open(fpath, "rb") as fp:
        while True:
            content = fp.readline()
            if not content:
                return False
            if chinese_pattern.search(content.decode("utf-8")):
                return True


def get_fpath_list(file_list):
    fpath_list = []
    for fpath in file_list:
        if os.path.isfile(fpath):
            fpath_list.append(fpath)
        elif os.path.isdir(fpath):
            for root, dirs, files in os.walk(fpath):
                for filename in files:
                    fpath_list.append(os.path.join(root, filename))
        else:
            print "not file or dir: {}".format(fpath)
    return fpath_list


def contain_chinese(file_list):
    fpath_list = get_fpath_list(file_list)
    for fpath in fpath_list:
        if is_file_contain_chinese(fpath):
            print "file contain chinese: {}".format(fpath)


if __name__ == "__main__":
    contain_chinese(sys.argv[1:])
