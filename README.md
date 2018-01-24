# SITH

## SITH: Simplified Test Harness

This is just a quick and dirty implementation of a simple testing harness, in the vein of the XUnit family. Don't use this one for proper systems development; use Python's own `unittest` module instead.

This is just an academic exercise.

## Layout

This is a modular system; one Harness contains a list of Test objects.

The role of the Test object is just to compare one expected output to a real output-- use it for modules.

The role of the Harness object is to provide an interface to run Test objects in the list sequentually, listing successes to failures.

## Usage

Again: don't, use `unittest`, but if you insist:

```python

import SITH.Harness
import SITH.test

...

test_harness = SITH.Harness()
test_test1 = SITH.Test(1, 1)
test_test2 = SITH.Test(1, 2)

test_harness.add_test(test_test1)
test_harness.add_test(test_test2)

print(test_harness.run_tests()) # should output (1, 1)

```

## Testing

To run unit tests on my implementation:

`python3 -m unittest test_harness.py`

`python3 -m unittest test_harness.py`

There are not nearly enough unit tests and the tests themselves are not nearly thorough enough (how about running a test suite with no tests, or running a test suite with a non-Test object in it?  (these I overlooked, and may fix at some point))

## Licensing

Do whatever you want with it, fam.
