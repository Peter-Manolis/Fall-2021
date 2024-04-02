# Assignment 8

- Username: pmanolis
- Commit hash used for grading: e9c84d86ea3ec4cdbf24ce555853022e93e99071

- Graded by: Tim Chan

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



## Total Score: 92.6/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (44.6/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `step`:10.0/10
    - TA Comments: TA did not add any comments.


- Problem 2:
    - `distance`: 5.0/5
    - `brute`: 3.6/5
    - TA Comments: There are some circumstances where it does not enter that if statement on 79. So the tuples never get assigned and are empty. The logic is all there though which is good.


- Problem 3:
    - `productivity`: 10.0/10
    - TA Comments: TA did not add any comments.


- Problem 4:
    - `permutation`:10.0/10
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `Vector`:6.0/10
    - TA Comments: In mul you're supposed to return a single number not a vector. In neg, you set it to only negate if i>0, but you're supposed to negate even if the number is less than 0. So -6 would become 6.



## Code Review & style (48/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to be a proper python code.
3. Your logic has to be correct.
4. You may pass our test cases but lose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.


- Problem 1:
    - `step`:10/10
    - TA Comments: TA did not add any comments.


- Problem 2:
    - `distance`: 5/5
    - `brute`: 4/5
    - TA Comments: TA did not add any comments.


- Problem 3:
    - `productivity`: 10/10
    - TA Comments: TA did not add any comments.


- Problem 4:
    - `permutation`:10/10
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `Vector`:9/10
    - TA Comments: Logic's all there just some bugs and cases that you forgot to consider.


## Unittest Results
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_brute_5
ERROR: Test case for function: brute
ERROR: Input: [(1, 1), (4, 5)]
ERROR: Actual output: [(), (), 5.0]
ERROR: Expected output: [(1, 1), (4, 5), 5]
ERROR: (1, 1) not found in [(), (), 5.0]
ERROR: ----------------------------------------------------------------------------
ERROR: (1, 1) not found in [(), (), 5.0]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/pmanolis/a8_hidden_test.py", line 188, in test_c_brute_5
    self.assertIn(expected_output[i], actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1096, in assertIn
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: (1, 1) not found in [(), (), 5.0]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_brute_5
ERROR: Test case for function: brute
ERROR: Input: [(0, 0), (4, 3), (100, 200)]
ERROR: Actual output: [(), (), 5.0]
ERROR: Expected output: [(0, 0), (4, 3), 5]
ERROR: (0, 0) not found in [(), (), 5.0]
ERROR: ----------------------------------------------------------------------------
ERROR: (0, 0) not found in [(), (), 5.0]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/pmanolis/a8_hidden_test.py", line 188, in test_c_brute_5
    self.assertIn(expected_output[i], actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1096, in assertIn
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: (0, 0) not found in [(), (), 5.0]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_i_Vector_1_mul
ERROR: Test case for function: Vector_mul
ERROR: Input: [(0, 5, 6), (1, 10, -1)]
ERROR: Actual output: <0, 50, -6>
ERROR: Expected output: 44
ERROR: 'int' object has no attribute '_Vector__v'
ERROR: ----------------------------------------------------------------------------
ERROR: 'int' object has no attribute '_Vector__v'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/pmanolis/a8_hidden_test.py", line 398, in test_i_Vector_1_mul
    self.assertEqual(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 819, in _baseAssertEqual
    if not first == second:
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/pmanolis/a8.py", line 177, in __eq__
    return len(self.__v)==sum([self.__v[i]==other.__v[i]for i in range(len(self.__v))])
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/pmanolis/a8.py", line 177, in <listcomp>
    return len(self.__v)==sum([self.__v[i]==other.__v[i]for i in range(len(self.__v))])
AttributeError: 'int' object has no attribute '_Vector__v'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_i_Vector_1_mul
ERROR: Test case for function: Vector_mul
ERROR: Input: [(-1, 0, 1), (10, 10, 10)]
ERROR: Actual output: <-10, 0, 10>
ERROR: Expected output: 0
ERROR: 'int' object has no attribute '_Vector__v'
ERROR: ----------------------------------------------------------------------------
ERROR: 'int' object has no attribute '_Vector__v'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/pmanolis/a8_hidden_test.py", line 398, in test_i_Vector_1_mul
    self.assertEqual(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 819, in _baseAssertEqual
    if not first == second:
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/pmanolis/a8.py", line 177, in __eq__
    return len(self.__v)==sum([self.__v[i]==other.__v[i]for i in range(len(self.__v))])
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/pmanolis/a8.py", line 177, in <listcomp>
    return len(self.__v)==sum([self.__v[i]==other.__v[i]for i in range(len(self.__v))])
AttributeError: 'int' object has no attribute '_Vector__v'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_k_Vector_1_neg
ERROR: Test case for function: Vector_neg
ERROR: Input: (3, -3)
ERROR: Actual output: (-3, -3)
ERROR: Expected output: (-3, 3)
ERROR: Tuples differ: (-3, 3) != (-3, -3)

First differing element 1:
3
-3

- (-3, 3)
+ (-3, -3)
?      +

ERROR: ----------------------------------------------------------------------------
ERROR: Tuples differ: (-3, 3) != (-3, -3)

First differing element 1:
3
-3

- (-3, 3)
+ (-3, -3)
?      +
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/pmanolis/a8_hidden_test.py", line 446, in test_k_Vector_1_neg
    self.assertEqual(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1046, in assertTupleEqual
    self.assertSequenceEqual(tuple1, tuple2, msg, seq_type=tuple)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Tuples differ: (-3, 3) != (-3, -3)

First differing element 1:
3
-3

- (-3, 3)
+ (-3, -3)
?      +

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_k_Vector_1_neg
ERROR: Test case for function: Vector_neg
ERROR: Input: (-6, 0, 6)
ERROR: Actual output: (-6, 0, -6)
ERROR: Expected output: (6, 0, -6)
ERROR: Tuples differ: (6, 0, -6) != (-6, 0, -6)

First differing element 0:
6
-6

- (6, 0, -6)
+ (-6, 0, -6)
?  +

ERROR: ----------------------------------------------------------------------------
ERROR: Tuples differ: (6, 0, -6) != (-6, 0, -6)

First differing element 0:
6
-6

- (6, 0, -6)
+ (-6, 0, -6)
?  +
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/pmanolis/a8_hidden_test.py", line 446, in test_k_Vector_1_neg
    self.assertEqual(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1046, in assertTupleEqual
    self.assertSequenceEqual(tuple1, tuple2, msg, seq_type=tuple)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Tuples differ: (6, 0, -6) != (-6, 0, -6)

First differing element 0:
6
-6

- (6, 0, -6)
+ (-6, 0, -6)
?  +

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_n_Vector_2_all
ERROR: Test case for function: Vector_all
ERROR: Input: Multiple operations on vectors
ERROR: Actual output: <-2, -4, -6>
ERROR: Expected output: <0, 0, 0>
ERROR: '<0, 0, 0>' != '<-2, -4, -6>'
- <0, 0, 0>
+ <-2, -4, -6>

ERROR: ----------------------------------------------------------------------------
ERROR: '<0, 0, 0>' != '<-2, -4, -6>'
- <0, 0, 0>
+ <-2, -4, -6>
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/pmanolis/a8_hidden_test.py", line 521, in test_n_Vector_2_all
    self.assertEqual("<0, 0, 0>", actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: '<0, 0, 0>' != '<-2, -4, -6>'
- <0, 0, 0>
+ <-2, -4, -6>

ERROR: ============================================================================
```
```
