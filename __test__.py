#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import unittest

from __get__ import check404

import logging
import sys
import random

reload(sys)
sys.setdefaultencoding('utf8')

#
# test
#

class common_Tests(unittest.TestCase):

  def test_check404(self):
    ret = check404("http://www.xuanran001.com/public/not_exist_file.html")
    msg = "Expect true, but return false"
    self.assertTrue(ret, msg='{0}'.format(msg))
    ret = check404("http://www.baidu.com/")
    msg = "Expect true, but return false"
    self.assertFalse(ret, msg='{0}'.format(msg))

def main():

    # create logger
    logger = logging.getLogger('getdesignlist')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler( sys.__stdout__ ) # Add this
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    # 'application' code
    #logger.debug('debug message')
    #logger.info('info message')
    #logger.warn('warn message')
    #logger.error('error message')
    #logger.critical('critical message')
    
    unittest.main()

if __name__ == '__main__':
    main()

# end
