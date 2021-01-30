""" Helper script to copy documents with Japanese filenames to a Kindle 4 and
    have them display properly.

    - mount Kindle with -o uni_xlate=1
    - run this script w/ the filename as command line parameter
    - move the file to the kindle and rename it to the output of this script

    example:
        $ sudo mount -o uni_xlate=1 /dev/sdb1 /mnt/sdb1

        $ python3 uni_xlate_filename.py バッタを倒しにアフリカへ
        :30d0:30c3:30bf:3092:5012:3057:306b:30a2:30d5:30ea:30ab:3078

        rename バッタを倒しにアフリカへ.pdf
        to :30d0:30c3:30bf:3092:5012:3057:306b:30a2:30d5:30ea:30ab:3078.pdf
"""

import sys

if len(sys.argv) < 2:
    print('Usage: python3 uni_xlate_filename.py <string>')
    sys.exit()

print(''.join(':' + hex(ord(c))[2:] for c in sys.argv[1]))
