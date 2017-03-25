#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

 Author:      konia
 Mail:        konka@maxln.com
 Time:        2017.03.22

 Filename:    program.py

 Relative:    requests
 Description: fetch `oreilly` free webops books ["pdf", "mobi", "epub"]

"""
import re
import os
import requests

def main():
    download_path = "download"
    headers = {"User-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"}
    free_url = "http://www.oreilly.com/webops/free/"

    free_page = requests.get(free_url, headers=headers).content
    book_name = re.findall(r'free\/([^\.]+)\.csp', free_page)

    for item, book in enumerate(book_name):
        book_dir = "%s/%s" % (download_path, book)

        if not os.path.exists(book_dir):
            os.makedirs(book_dir)

        print "BOOK(%02d): %s%s.csp" % (item+1, free_url, book)

        for file_extend in ["pdf", "mobi", "epub"]:
            file_link = "http://www.oreilly.com/webops-perf/free/files/%s.%s" % (book, file_extend)
            file_path = "%s/%s.%s" % (book_dir, book, file_extend)

            if not os.path.isfile(file_path):
                data = requests.get(file_link, headers=headers).content
                with open(file_path, 'wb') as filehandle:
                    filehandle.write(data)

                print "    > file save: %s" % file_path
            else:
                print "    > file exist: %s" % file_path



if __name__ == "__main__":
    main()
