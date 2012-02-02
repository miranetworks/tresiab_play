#!/usr/bin/env python

import sys, unittest, junitxml

def main(argv=sys.argv):
    import test_fibonacci

   # suite_test_fibonacci = unittest.makeSuite(test_fibonacci.TestFibonacci)

   # alltests = unittest.TestSuite((
   #     suite_test_fibonacci,
   # ))
   # 
   # unittest.TextTestRunner(verbosity=2).run(alltests)


    with open('output/test_fibonacci.xml', 'w') as test_output:
        result = junitxml.JUnitXmlResult(test_output)
        result.startTestRun()
        suite = unittest.TestLoader().loadTestsFromTestCase(test_fibonacci.TestFibonacci)
        suite.run(result)
        result.stopTestRun()


#=============================================================================

if __name__ == '__main__':
    sys.exit(main())
