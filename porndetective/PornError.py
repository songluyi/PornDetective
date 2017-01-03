# -*- coding: utf-8 -*-
# 2016/12/30 13:16
"""
-------------------------------------------------------------------------------
Function:   porn_detective error file
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import logging
logfile = "porn_detective.log"
logging.basicConfig(filename=logfile,level=logging.DEBUG)
class PornDetectiveError(object):
    pass

class InvalidInputObject(PornDetectiveError):
    logging.error('wrong input object, please check your input.'
                  'check path if folder!'
                  ' check integrity if image!'
                  'check http format if url ! ')
    pass
class WrongUrlName(PornDetectiveError):
    logging.error('the url tail is not a formal pic format perhaps it looks like xxx.jpg?=xxx.Modify it!')
    pass
def check_for_errors(logfile = "porn_detective.log"):
    inf = open(logfile)
    text = inf.read()
    inf.close()
    # All error conditions result in "Error" somewhere in logfile
    if text.find("Error") != -1:
        raise PornDetectiveError