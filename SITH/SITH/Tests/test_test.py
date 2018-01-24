from unittest import TestCase
import SITH.test as st

class TestTest(TestCase):
    def test_run_test(self):
        test1 = st.Test(1, 1)
        self.assertTrue(test1.run_test())

        test2 = st.Test(1, 3)
        self.assertFalse(test2.run_test())
