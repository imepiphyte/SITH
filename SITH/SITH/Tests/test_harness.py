from unittest import TestCase
import SITH.test as st
import SITH.harness as sh

class TestHarness(TestCase):
    def test_add_test(self):
        test1 = st.Test(1, 1)
        test2 = st.Test(1, 2)
        test3 = st.Test(None, None)
        test4 = st.Test(None, 1)

        test_harness = sh.Harness()
        test_harness.add_test(test1)

        self.assertTrue(test_harness.test_suite)


    def test_run_tests(self):

        test1 = st.Test(1, 1)
        test2 = st.Test(1, 2)
        test3 = st.Test(None, None)
        test4 = st.Test(None, 1)

        test_harness = sh.Harness()
        test_harness.add_test(test1)
        test_harness.add_test(test2)
        test_harness.add_test(test3)
        test_harness.add_test(test4)

        self.assertEqual(test_harness.run_tests(), (2, 2))
