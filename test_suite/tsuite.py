#! /usr/bin/env python
# -*- coding:utf-8 -*-

import unittest

import tc.tcase

def test_suite1():
    suite = unittest.makeSuite(tc.tcase.Testrun)
    return suite

test_suite1()