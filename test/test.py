#!/usr/bin/env python

import sys, unittest

def main(argv=sys.argv):
    import test_fibonacci

    suite_test_fibonacci = unittest.makeSuite(test_fibonacci.TestFibonacci)

    alltests = unittest.TestSuite((
        suite_test_fibonacci,
    ))

    unittest.TextTestRunner(verbosity=2).run(alltests)

#=============================================================================

if __name__ == '__main__':
    sys.exit(main())
