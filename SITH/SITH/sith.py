import SITH.test as st
import SITH.harness as sh

if __name__ == '__main__':

    # building a few tests
    test_test1 = st.Test(1, 1)
    test_test2 = st.Test(1, 2)

    print(test_test1)
    print(test_test2)

    # building harness
    test_harness = sh.Harness()

    # adding tests to harness
    test_harness.add_test(test_test1)
    test_harness.add_test(test_test2)

    print(test_harness)

    print(test_harness.run_tests())

