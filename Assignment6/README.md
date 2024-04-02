# Assignment 6

- Username: pmanolis
- Commit hash used for grading: 699e6ff62226ddaff0256bc40a1cf6d961aeb656

- Graded by: Derek Ronske

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



## Total Score: 81/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (41.0/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `C`:4.0/4
    - `B`: 6.0/6
    - TA Comments: TA did not add any comments.


- Problem 2:
    - `get_data`: 2.0/4
    - `pop`: 3.0/3
    - `error`: 3.0/3
    - TA Comments: Everything here is pretty much good, but you wouldn't need to include your repository's name, since the path is already being passed into the function to be read, which should handle everything in the relevant path.


- Problem 3:
    - `isogram`: 5.0/10
    - TA Comments: All of the test cases passed, but using methods that are not permitted.


- Problem 4:
    - `Hex`:8.0/10
    - TA Comments: There seems to be some issue with when a value is repeated in the hex definition. It may be easier to traverse the list backwards instead of reversing it separately.


- Problem 5:
    - `div_11`: 10.0/10
    - TA Comments: TA did not add any comments.


## Code Review & style (40/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to be a proper python code.
3. Your logic has to be correct.
4. You may pass our test cases but lose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.


- Problem 1:
    - `C`: 4/4
    - `B`: 6/6
    - TA Comments: TA did not add any comments.


- Problem 2:
    - `get_data`: 4/4
    - `pop`: 3/3
    - `error`: 3/3
    - TA Comments: TA did not add any comments.


- Problem 3:
    - `isogram`: 0/10
    - TA Comments: The count() function not allowed for this assignment!


- Problem 4:
    - `Hex`: 10/10
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `div_11`: 10/10
    - TA Comments: Everything looks good, but at the end, you could just return the boolean within your condiitonal instead of writing the entire conditional branch out!

## Unittest Results
```
INFO: Guessed "   " as the file separator expected by the get_data function
INFO: Guessed "   " as the file separator expected by the get_data function
INFO: Guessed "   " as the file separator expected by the get_data function
ERROR: ============================================================================
ERROR: Failed test case: test_e_getdata_2_filename_test
ERROR: Test case for function: get_data
ERROR: Input: ('SomeFolder', 'some_file')
ERROR: Actual output: C200-Assignments-pmanolis/SomeFolder/some_file
ERROR: Expected output: Correctly constructed file path
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_e_getdata_2_filename_test
ERROR: Test case for function: get_data
ERROR: Input: ('Assignment6', 'pop.txt')
ERROR: Actual output: C200-Assignments-pmanolis/Assignment6/pop.txt
ERROR: Expected output: Correctly constructed file path
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_i_Hex_10
ERROR: Test case for function: Hex
ERROR: Input: ('11',) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: 2
ERROR: Expected output: 17
ERROR: 17 != 2
ERROR: ----------------------------------------------------------------------------
ERROR: 17 != 2
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment6/pmanolis/a6_hidden_test.py", line 94, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: 17 != 2
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_i_Hex_10
ERROR: Test case for function: Hex
ERROR: Input: ('FFFFF',) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: 75
ERROR: Expected output: 1048575
ERROR: 1048575 != 75
ERROR: ----------------------------------------------------------------------------
ERROR: 1048575 != 75
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment6/pmanolis/a6_hidden_test.py", line 94, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: 1048575 != 75
ERROR: ============================================================================
```
```
