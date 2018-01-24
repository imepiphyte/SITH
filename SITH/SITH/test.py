class Test:
    """
    Test class: for running the tests, comparing expected output to actual output and acting accordingly.
    """

    def __init__(self, actual_output, expected_output):
        "Constructor"
        self.actual_output = actual_output
        self.expected_output = expected_output

    def __str__(self):
        "ToString"
        return "[ Test output: {0} / Expected Output: {1} ]".format(self.actual_output, self.expected_output)

    def run_test(self):
        "Running a singular test."
        try:
            if self.expected_output == self.actual_output:
                return True
            else:
                return False
        except Exception:
            return False
