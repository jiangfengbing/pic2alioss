#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import oss2
import datetime
import random
import string

__author__ = "Jiang Fengbing"
__copyright__ = "Copyright 2020 Jiang Fengbing. All rights reserved."


def save_path(path):
    open('path.txt', 'w').write(path)


def save_url(url):
    open('url.txt', 'w').write(url)


def load_config():
    try:
        data = open('config.json', 'r').read()
        return json.loads(data)
    except IOError:
        pass
    return None


def gen_suffix(n):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))


def gen_remote_path(path):
    file_name = path.split('/')[-1]
    date = datetime.datetime.now().date()
    url_suffix = gen_suffix(4)
    return 'wf/%d-%02d-%02d/%s/%s' % (date.year, date.month, date.day, url_suffix, file_name)


def full_url(remote_path, conf):
    return '%s/%s' % (conf['urlPrefix'].rstrip('/'), remote_path)


def get_endpoint(conf):
    endpoint = conf['endpoint']
    if endpoint.find('http') < 0:
        return 'https://' + endpoint
    return endpoint


def upload_pic(path, conf):
    bucket_name = conf['bucket']
    remote_path = gen_remote_path(path)
    bucket = oss2.Bucket(oss2.Auth(conf['accessKeyId'], conf['accessKeySecret']),
        get_endpoint(conf), bucket_name)
    try:
        ret = bucket.put_object_from_file(remote_path, path)
        if ret.status not in [200, 201]:
            return False, '上传失败!'
    except oss2.exceptions.OssError as oe:
        return False, oe.message
    except IOError:
        return False, '文件打开失败!'
    return True, full_url(remote_path, conf)


def main():
    conf = load_config()
    if not conf:
        print('请配置图床!')
        return

    lines = sys.stdin.readlines()
    if lines:
        path = lines[0]
        path = path.rstrip()
        ext = path.split('.')[-1]
        ext = ext.lower()
        if ext in ['jpg', 'jpeg', 'png', 'bmp', 'tif', 'tiff', 'gif', 'ico', 'svg']:
            save_path(path)
            ret, msg = upload_pic(path, conf)
            if ret:
                save_url(msg)
        else:
            msg = '你选中的不是图片文件!'
        print(msg)

if __name__ == '__main__':
    main()
