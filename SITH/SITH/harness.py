class Harness:
    """
    Harness class: for running tests in batch, to calculate statistics at the end.
    """

    def __init__(self):
        "Constructor"
        self.test_suite = []
        self.successes = 0
        self.failures = 0
        self.has_ran = False

    def __str__(self):
        "ToString"
        return str(self.test_suite) + " / S:{0} / F: {1}".format(self.successes, self.failures)

    def add_test(self, test):
        "Adding a test."
        try:
            self.test_suite.append(test)
        except Exception:
            pass

    def run_tests(self):
        "Running all tests, getting results even if it has/has not ran."
        if not self.has_ran:
            for test in self.test_suite:
                try:
                    if test.run_test() == True:
                        self.successes = self.successes + 1
                    elif test.run_test() == False:
                        self.failures = self.failures + 1
                except Exception:
                    self.failures = self.failures + 1

        return (self.successes, self.failures)
