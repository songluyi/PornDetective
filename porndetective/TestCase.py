# -*- coding: utf-8 -*-
# 2017/1/3 15:04
"""
-------------------------------------------------------------------------------
Function:   Test for fun~
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""

from porndetective import PornDetective
from porndetective import LoadWay
import unittest
import os
class PornDetectiveTest(unittest.TestCase):
    def test_img_url(self):
        # perhaps the img_url may cause the bad request to lead unittest failure
        # by the way, the cat img can be divided into porn pic class. This part will be optimized
        url_test_list =\
            ['http://www.haopic.me/wp-content/uploads/2015/04/20150430102011596.jpg'
            , 'http://www.anhuiyubo.com/a/img/b/c/f/1/2/d/16352.jpg'
            ,'http://www.qqgxzlw.cn/uploads/allimg/121207/10324M3N-6.jpg']
        LoadWay.url_pic_list(url_test_list)

    def test_folder(self):
        folder_path=os.getcwd()
        LoadWay.folder_way(folder_path)

    def test_img(self):
        img = 'test.jpg'
        test=PornDetective(img)
        test.parse()
        test.showSkinRegions()
if __name__=="__main__":
    # if ResourceWarning: unclosed file shows , Don't worry.It caused by Image.open function.
    unittest.main()