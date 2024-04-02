# Assignment 5

- Username: pmanolis
- Commit hash used for grading: e88c8982b483686a7e5c944ae3120b3124b0c09b

- Graded by: Sara Zomorodi

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



## Total Score: 98.3/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (49.3/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `makeProbability`:3.0/3
    - `entropy`: 3.0/3
    - TA Comments: TA did not add any comments.


- Problem 2:
    - `L`: 7.0/7
    - TA Comments: TA did not add any comments.


- Problem 3:
    - `div9`: 7.0/7
    - TA Comments: TA did not add any comments.


- Problem 4:
    - `p`:3.0/3
    - `c`:3.0/3
    - `d`: 3.0/3
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `potato`: 6.8/7
    - TA Comments: It's failing for the test cases with size 2. Look at the condition of your while loop.


- Problem 6:
    - `msi`: 7.0/7
    - TA Comments: TA did not add any comments.


- Problem 7:
    - `dollars`: 6.5/7
    - TA Comments: The x=0 is the only test case that is failing. 

## Code Review & style (49/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to be a proper python code.
3. Your logic has to be correct.
4. You may pass our test cases but lose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.

- Problem 1:
    - `makeProbability`: 3/3
    - `entropy`: 3/3
    - TA Comments: TA did not add any comments.


- Problem 2:
    - `L`: 7/7
    - TA Comments: TA did not add any comments.


- Problem 3:
    - `div9`: 7/7
    - TA Comments: TA did not add any comments.


- Problem 4:
    - `p`: 3/3
    - `c`: 3/3
    - `d`: 3/3
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `potato`: 6.5/7
    - TA Comments: The only problem is for the lists of the size 2. It never enters the while loop.


- Problem 6:
    - `msi`: 7/7
    - TA Comments: TA did not add any comments.


- Problem 7:
    - `dollars`: 6.5/7
    - TA Comments: If x=0, it never enters the while loop. And it just returns none. But the whole logic is correct. 

## Unittest Results
```
ERROR: ============================================================================
ERROR: Failed test case: test_dollars_2_hidden
ERROR: Test case for function: dollars
ERROR: Input: (0,) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: None
ERROR: Expected output: [0, 0, 0, 0]
ERROR: [0, 0, 0, 0] != None
ERROR: ----------------------------------------------------------------------------
ERROR: [0, 0, 0, 0] != None
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/pmanolis/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: [0, 0, 0, 0] != None
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: potato
ERROR: Input: ([1, 2],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: []
ERROR: Expected output: [1, 2]
ERROR: Lists differ: [1, 2] != []

First list contains 2 additional elements.
First extra element 0:
1

- [1, 2]
+ []
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2] != []

First list contains 2 additional elements.
First extra element 0:
1

- [1, 2]
+ []
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/pmanolis/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2] != []

First list contains 2 additional elements.
First extra element 0:
1

- [1, 2]
+ []
ERROR: ============================================================================
```
```
