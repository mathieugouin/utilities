#!/usr/bin/python

import sys
import codecs
import re
import os


def get_month(m):
    dic = {
        'janvier': 1,
        u'f\xe9vrier': 2,
        'mars': 3,
        'avril': 4,
        'mai': 5,
        'juin': 6,
        'juillet': 7,
        u'ao\xfbt': 8,
        'septembre': 9,
        'octobre': 10,
        'novembre': 11,
        u'd\xe9cembre': 12
        }

    if m in dic:
        return dic[m]
    else:
        print "ERROR: " + m
        return 0  # TBD


def get_new_name(old_name):
    new_name = old_name
    m = re.match(u"(.*?), (\d+) ([^ ]+) (\d{4})", old_name)
    if m:
        #print "  MATCH =", m.groups()
        new_name = u'{:04d}-{:02d}-{:02d}, {}'.format(int(m.group(4)), get_month(m.group(3)), int(m.group(2)), m.group(1))
    return new_name


def folder_find(d):
    print "ROOT = " + d

    for f in os.listdir(d):
        if os.path.isdir(os.path.join(d, f)):
            f = unicode(f, 'utf-8')
            print "  FOLDER   = " + f
            new_name = get_new_name(f)
            if new_name != f:
                print "  NEW_NAME = " + new_name
                # TBD rename when OK


def test_file():
    f = '/home/mgouin/ls.txt'
    for l in codecs.open(f, 'rt', encoding='utf-8').readlines():
        l = l.rstrip()
        print "LINE = " + l
        print "NEW_NAME = " + get_new_name(l)


def test_path():
    r = '/media/mgouin/GRAY_500GB/Photos/2014'
    folder_find(r)


def _main():
    print "_main()"

    #test_file()
    test_path()

    if len(sys.argv) > 1:
        for r in sys.argv[1:]:
            folder_find(r)


if __name__ == '__main__':
    _main()
