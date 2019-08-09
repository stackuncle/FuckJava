#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


with open ("./README.md", "w") as f:
    f.write("# 常见算法题")
    dirs = os.listdir("./")

    for sub_dir in dirs:
        if "md" in sub_dir or "py" in sub_dir:
            continue

        title = "\n## %s" % sub_dir
        f.write(title)
        files = os.listdir(sub_dir)
        files.sort()
        print title

        for md_file in files:
            sub_title = "\n- [%s](./%s/%s)" % (md_file[:-3], sub_dir, md_file)
            print sub_title
            f.write(sub_title)
        f.write("\n\n")

