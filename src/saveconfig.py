#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json

__author__ = "Jiang Fengbing"
__copyright__ = "Copyright 2020 Jiang Fengbing. All rights reserved."


def main():
    try:
        lines = sys.stdin.readlines()
        data = []
        for line in lines:
            line = line.rstrip()
            data.append(line)

        config = {
            'bucket': data[0],
            'endpoint': data[1],
            'accessKeyId': data[2],
            'accessKeySecret': data[3],
            'urlPrefix': data[4]
        }
        open('config.json', 'w').write(json.dumps(config))
        print('配置成功!')
        return
    except:
        pass
    print('配置失败!')


if __name__ == '__main__':
    main()
