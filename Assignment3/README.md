# Assignment 3

- Username: pmanolis
- Commit hash used for grading: e5c4ffba0fee8b64fe2814a28f0c26e2dfde0a3d

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



## Total Score: 93.1/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (47.1/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `N`: 2.0/3
    - `N_t`: 3.0/3
    - `W`: 3.0/3
    - `L`: 2.0/2
    - TA Comments: All good!

- Problem 2:
    - `q`: 3.0/4
    - TA Comments: Roots are real even if discriminant is zero.

- Problem 3:
    - `amt`: 5.6/6
    - TA Comments: Your function `m` only returns `True` if element is present in list, but does not return `False` if element is not found.

- Problem 4:
    - `f`: 5.0/5
    - TA Comments: All good!


- Problem 5:
    - `arithmetic_mean`, `geo_mean`, `har_mean`, `RMS_mean`: 8.0/8
    - TA Comments: All good!


- Problem 6:
    - `F`, `V`, `C`: 7.0/7
    - TA Comments: All good!


- Problem 7:
    - `Mortgage`, `total_paid`: 4.0/4
    - TA Comments: All good!


- Problem 8:
    - `is_geo`: 4.5/5
    - TA Comments: The condition on line 192 does not do anything meaningful. It is evaluated as follows: `if ( ((x1/x0) != 0 ) or ( (x1*x0)) != ((x2/x1) ) or ( (x2*x1)) != 0 ):`.



## Code Review & style (46/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to a proper python code.
3. Your logic has to correct.
4. You may pass our test cases but loose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.

- Problem 1:
    - `N`: 3/3
    - `N_t`: 3/3
    - `W`: 2/3
    - `L`: 2/2
    - TA Comments: Good job!

- Problem 2:
    - `q`: 3/4
    - TA Comments: Docking points for missing a condition.

- Problem 3:
    - `amt`: 5/6
    - TA Comments: You missed a critical piece of logic from `m`.

- Problem 4:
    - `f`: 5/5
    - TA Comments: Good job!


- Problem 5:
    - `arithmetic_mean`, `geo_mean`, `har_mean`, `RMS_mean`: 8/8
    - TA Comments: Good job!


- Problem 6:
    - `F`, `V`, `C`: 7/7
    - TA Comments: Good job!


- Problem 7:
    - `Mortgage`, `total_paid`: 4/4
    - TA Comments: Good job!


- Problem 8:
    - `is_geo`: 4/5
    - TA Comments: You were in the right direction, but still just short of the correct thing.


## Unittest Results
ERROR: -------------------------------------
ERROR: Failed test case:   File "/home/sara/Desktop/Spring-2022/Gradingdata/Assignment3/pmanolis/a3_hidden_test.py", line 63, in test_N_1_negative
    check_assertion(result, self.assertAlmostEqual, 2, 183.94, a3.N, 500, -0.25, 4)

ERROR: Input: (500, -0.25, 4) -- ignore the outermost () and the trailing ,
ERROR: 183.94 != 184 within 2 places (0.060000000000002274 difference)
ERROR: ======================================

ERROR: -------------------------------------
ERROR: Failed test case:   File "/home/sara/Desktop/Spring-2022/Gradingdata/Assignment3/pmanolis/a3_hidden_test.py", line 64, in test_N_1_negative
    check_assertion(result, self.assertAlmostEqual, 2, 151.63, a3.N, 250, -0.25, 2)

ERROR: Input: (250, -0.25, 2) -- ignore the outermost () and the trailing ,
ERROR: 151.63 != 152 within 2 places (0.37000000000000455 difference)
ERROR: ======================================

ERROR: -------------------------------------
ERROR: Failed test case:   File "/home/sara/Desktop/Spring-2022/Gradingdata/Assignment3/pmanolis/a3_hidden_test.py", line 205, in test_amt_1_test_m
    check_assertion(result, self.assertEqual, None, False, a3.m, -1, no_tax)

ERROR: Input: (-1, [2, 1]) -- ignore the outermost () and the trailing ,
ERROR: False != None
ERROR: ======================================

ERROR: -------------------------------------
ERROR: Failed test case:   File "/home/sara/Desktop/Spring-2022/Gradingdata/Assignment3/pmanolis/a3_hidden_test.py", line 206, in test_amt_1_test_m
    check_assertion(result, self.assertEqual, None, False, a3.m, 3, no_tax)

ERROR: Input: (3, [2, 1]) -- ignore the outermost () and the trailing ,
ERROR: False != None
ERROR: ======================================

ERROR: -------------------------------------
ERROR: Failed test case:   File "/home/sara/Desktop/Spring-2022/Gradingdata/Assignment3/pmanolis/a3_hidden_test.py", line 360, in test_geo_1_input_bounds
    check_assertion(result, self.assertEqual, None, 0, a3.is_geo, [])

ERROR: Input: ([],) -- ignore the outermost () and the trailing ,
ERROR: list index out of range
ERROR: ======================================

ERROR: -------------------------------------
ERROR: Failed test case:   File "/home/sara/Desktop/Spring-2022/Gradingdata/Assignment3/pmanolis/a3_hidden_test.py", line 361, in test_geo_1_input_bounds
    check_assertion(result, self.assertEqual, None, 0, a3.is_geo, [1])

ERROR: Input: ([1],) -- ignore the outermost () and the trailing ,
ERROR: list index out of range
ERROR: ======================================

ERROR: -------------------------------------
ERROR: Failed test case:   File "/home/sara/Desktop/Spring-2022/Gradingdata/Assignment3/pmanolis/a3_hidden_test.py", line 137, in test_q_1_dis_zero
    check_assertion(result, self.assertEqual, None, True, a3.q, (4,4,1))

ERROR: Input: ((4, 4, 1),) -- ignore the outermost () and the trailing ,
ERROR: True != 0
ERROR: ======================================

ERROR: -------------------------------------
ERROR: Failed test case:   File "/home/sara/Desktop/Spring-2022/Gradingdata/Assignment3/pmanolis/a3_hidden_test.py", line 138, in test_q_1_dis_zero
    check_assertion(result, self.assertEqual, None, True, a3.q, (5,5,5/4))

ERROR: Input: ((5, 5, 1.25),) -- ignore the outermost () and the trailing ,
ERROR: True != 0
ERROR: ======================================

ERROR: -------------------------------------
ERROR: Failed test case:   File "/home/sara/Desktop/Spring-2022/Gradingdata/Assignment3/pmanolis/a3_hidden_test.py", line 139, in test_q_1_dis_zero
    check_assertion(result, self.assertEqual, None, True, a3.q, (1/4,5,25))

ERROR: Input: ((0.25, 5, 25),) -- ignore the outermost () and the trailing ,
ERROR: True != 0
ERROR: ======================================

