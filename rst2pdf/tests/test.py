# -*- coding: utf-8 -*-

from autotest import PathInfo, globjoin
from autotest import run_single_test as run_single

import sys, os
import nose.plugins.skip

class RunTest:
    def __init__(self,f):
        self.description = os.path.basename(f)
        
    def __call__(self,f):
        key, errcode = run_single(f)
	if key in ['incomplete','unknown']:
            raise nose.plugins.skip.Skip
        assert key == 'good', '%s is not good: %s'%(f,key)

def test():
    testfiles = globjoin(PathInfo.inpdir, '*.txt')
    results = {}
    for fname in testfiles:
        yield RunTest(fname), fname

def setup():
    PathInfo.add_coverage()
