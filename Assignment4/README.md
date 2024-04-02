# Assignment 4

- Username: pmanolis
- Commit hash used for grading: af0945961ed0870967d99d5a09e8abd89e487271

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



## Total Score: 99.2/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (49.2/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `a`, `b`, `c`, `day`: 9.0/9
    - TA Comments: TA did not add any comments.


- Problem 2:
    - `q`: 8.0/8
    - TA Comments: TA did not add any comments.


- Problem 3:
    - `inner_prod`, `mag`, `angle`, `match`, `best_match`: 9.2/10
    - TA Comments: lst1 is only created in the case that score[i][2] is less than best_score, there is a couple cases in which this conditional will not be true, but lst1 is return regardless, hence the reference before assignment error.


- Problem 4:
    - `intersect`: 6.0/6
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `mean`, `variance`, `std`, `mean_centered`: 10.0/10
    - TA Comments: TA did not add any comments.


- Problem 6:
    - `equi`: 7.0/7
    - TA Comments: TA did not add any comments.



## Code Review & style (50/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to be a proper python code.
3. Your logic has to be correct.
4. You may pass our test cases but lose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.

- Problem 1:
    - `a`, `b`, `c`, `day`: 9/9
    - TA Comments: TA did not add any comments.


- Problem 2:
    - `q`: 8/8
    - TA Comments: TA did not add any comments.


- Problem 3:
    - `inner_prod`, `mag`, `angle`, `match`, `best_match`: 10/10
    - TA Comments: TA did not add any comments.


- Problem 4:
    - `intersect`: 6/6
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `mean`, `variance`, `std`, `mean_centered`: 10/10
    - TA Comments: TA did not add any comments.


- Problem 6:
    - `equi`: 7/7
    - TA Comments: TA did not add any comments.


## Unittest Results
```
ERROR: ============================================================================
ERROR: Failed test case: test_bestmatch_4_end_to_end
ERROR: Input: [[1], [1]]
ERROR: local variable 'lst1' referenced before assignment
ERROR: ----------------------------------------------------------------------------
ERROR: local variable 'lst1' referenced before assignment
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment4/pmanolis/a4_hidden_test.py", line 148, in test_bestmatch_4_end_to_end
    return_value = a4.best_match(a4.match(input))
  File "/home/sara/Spring-2022/Gradingdata/Assignment4/pmanolis/a4.py", line 95, in best_match
    return (lst1, lst2, best_score)
UnboundLocalError: local variable 'lst1' referenced before assignment
ERROR: ============================================================================
```
```
