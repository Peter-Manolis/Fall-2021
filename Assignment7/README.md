# Assignment 7

- Username: pmanolis
- Commit hash used for grading: 3eec2eed27f4b5f4486e73841ec7b52ccff5fffc

- Graded by: Ethan Stone

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



## Total Score: 63.5/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (22.5/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `Fraction`:4.8/11
    - TA Comments: You have to use the get method in the add,mul etc function to get the denominator and numerator, you cannot just do other.numerator/denominator


- Problem 2:
    - `encrypt`: 1.1/2
    - `decrypt`: 1.1/2
    - `encryptsentence`: 2.0/5
    - `decryptsentence`: 1.0/4
    - TA Comments: Your encrypt and decrypt functions do not return the correct value - should be moving it by (x+-n)%27


- Problem 3:
    - `getaminoacids`: 3.5/5
    - `getDNA`: 5.0/5
    - `translate`: 3.0/3
    - TA Comments: Good job!


- Problem 4:
    - `Function`:1.0/13
    - TA Comments: Your point function should return return self.f(x) - you have it returning a string which causes an error in every other function



## Code Review & style (41/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to be a proper python code.
3. Your logic has to be correct.
4. You may pass our test cases but lose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.


- Problem 1:
    - `Fraction`:7/11
    - TA Comments: See above


- Problem 2:
    - `encrypt`: 0/2
    - `decrypt`: 0/2
    - `encryptsentence`: 5/5
    - `decryptsentence`: 4/4
    - TA Comments: See above


- Problem 3:
    - `getaminoacids`: 5/5
    - `getDNA`: 5/5
    - `translate`: 3/3
    - TA Comments: Good job!


- Problem 4:
    - `Function`:12/13
    - TA Comments: See above


## Unittest Results
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_Fraction_5_basic
ERROR: Test case for function: Fraction_eq_repr
ERROR: Input: (5, 7)
ERROR: Actual output: frac(0,5/7)
ERROR: Expected output: frac(5/7)
ERROR: 'frac(5/7)' != 'frac(0,5/7)'
- frac(5/7)
+ frac(0,5/7)
?      ++

ERROR: ----------------------------------------------------------------------------
ERROR: 'frac(5/7)' != 'frac(0,5/7)'
- frac(5/7)
+ frac(0,5/7)
?      ++
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 219, in test_a_Fraction_5_basic
    self.assertEqual(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'frac(5/7)' != 'frac(0,5/7)'
- frac(5/7)
+ frac(0,5/7)
?      ++

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_Fraction_5_basic
ERROR: Test case for function: Fraction_eq_repr
ERROR: Input: (1, 2)
ERROR: Actual output: frac(0,1/2)
ERROR: Expected output: frac(1/2)
ERROR: 'frac(1/2)' != 'frac(0,1/2)'
- frac(1/2)
+ frac(0,1/2)
?      ++

ERROR: ----------------------------------------------------------------------------
ERROR: 'frac(1/2)' != 'frac(0,1/2)'
- frac(1/2)
+ frac(0,1/2)
?      ++
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 219, in test_a_Fraction_5_basic
    self.assertEqual(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'frac(1/2)' != 'frac(0,1/2)'
- frac(1/2)
+ frac(0,1/2)
?      ++

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_Fraction_5_basic
ERROR: Test case for function: Fraction_eq_repr
ERROR: Input: (4, 5)
ERROR: Actual output: frac(0,4/5)
ERROR: Expected output: frac(4/5)
ERROR: 'frac(4/5)' != 'frac(0,4/5)'
- frac(4/5)
+ frac(0,4/5)
?      ++

ERROR: ----------------------------------------------------------------------------
ERROR: 'frac(4/5)' != 'frac(0,4/5)'
- frac(4/5)
+ frac(0,4/5)
?      ++
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 219, in test_a_Fraction_5_basic
    self.assertEqual(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'frac(4/5)' != 'frac(0,4/5)'
- frac(4/5)
+ frac(0,4/5)
?      ++

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_Fraction_2_hard
ERROR: Test case for function: Fraction_all
ERROR: Input: ((2, 4), (4, 8))
ERROR: Actual output: frac(1,0/32)
ERROR: Expected output: ((4, 4), 'frac(1,0/1)')
ERROR: False is not true
ERROR: ----------------------------------------------------------------------------
ERROR: False is not true
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 309, in test_c_Fraction_2_hard
    self.assertTrue(actual_output.__repr__() == expected_output[1])
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 680, in assertTrue
    raise self.failureException(msg)
AssertionError: False is not true
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_Fraction_2_hard
ERROR: Test case for function: Fraction_all
ERROR: Input: ((27, 9), (12, 3))
ERROR: Actual output: frac(7,0/27)
ERROR: Expected output: ((7, 1), 'frac(7,0/1)')
ERROR: False is not true
ERROR: ----------------------------------------------------------------------------
ERROR: False is not true
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 309, in test_c_Fraction_2_hard
    self.assertTrue(actual_output.__repr__() == expected_output[1])
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 680, in assertTrue
    raise self.failureException(msg)
AssertionError: False is not true
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_Fraction_2_hard
ERROR: Test case for function: Fraction_all
ERROR: Input: ((1, 2), (4, 1))
ERROR: Actual output: frac(2,0/2)
ERROR: Expected output: ((4, 2), 'frac(2,0/1)')
ERROR: False is not true
ERROR: ----------------------------------------------------------------------------
ERROR: False is not true
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 330, in test_c_Fraction_2_hard
    self.assertTrue(actual_output.__repr__() == expected_output[1])
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 680, in assertTrue
    raise self.failureException(msg)
AssertionError: False is not true
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_Fraction_2_hard
ERROR: Test case for function: Fraction_all
ERROR: Input: ((6, 7), (1, 2))
ERROR: Actual output: frac(0,6/14)
ERROR: Expected output: ((3, 7), 'frac(3/7)')
ERROR: False is not true
ERROR: ----------------------------------------------------------------------------
ERROR: False is not true
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 330, in test_c_Fraction_2_hard
    self.assertTrue(actual_output.__repr__() == expected_output[1])
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 680, in assertTrue
    raise self.failureException(msg)
AssertionError: False is not true
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_Fraction_2_hard
ERROR: Test case for function: Fraction_all
ERROR: Input: ((4, 3), (1, 2))
ERROR: Actual output: frac(0,4/6)
ERROR: Expected output: ((2, 3), 'frac(2/3)')
ERROR: False is not true
ERROR: ----------------------------------------------------------------------------
ERROR: False is not true
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 330, in test_c_Fraction_2_hard
    self.assertTrue(actual_output.__repr__() == expected_output[1])
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 680, in assertTrue
    raise self.failureException(msg)
AssertionError: False is not true
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_d_encrypt_2
ERROR: Test case for function: encrypt
ERROR: Input: ('a', 27) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: |
ERROR: Expected output: a
ERROR: 'a' != '|'
- a
+ |

ERROR: ----------------------------------------------------------------------------
ERROR: 'a' != '|'
- a
+ |
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'a' != '|'
- a
+ |

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_d_encrypt_2
ERROR: Test case for function: encrypt
ERROR: Input: ('a', 28) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: }
ERROR: Expected output: b
ERROR: 'b' != '}'
- b
+ }

ERROR: ----------------------------------------------------------------------------
ERROR: 'b' != '}'
- b
+ }
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'b' != '}'
- b
+ }

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_d_encrypt_2
ERROR: Test case for function: encrypt
ERROR: Input: ('z', 2) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: |
ERROR: Expected output: a
ERROR: 'a' != '|'
- a
+ |

ERROR: ----------------------------------------------------------------------------
ERROR: 'a' != '|'
- a
+ |
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'a' != '|'
- a
+ |

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_e_decrypt_2
ERROR: Test case for function: decrypt
ERROR: Input: ('a', 27) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: F
ERROR: Expected output: a
ERROR: 'a' != 'F'
- a
+ F

ERROR: ----------------------------------------------------------------------------
ERROR: 'a' != 'F'
- a
+ F
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'a' != 'F'
- a
+ F

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_e_decrypt_2
ERROR: Test case for function: decrypt
ERROR: Input: ('b', 28) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: F
ERROR: Expected output: a
ERROR: 'a' != 'F'
- a
+ F

ERROR: ----------------------------------------------------------------------------
ERROR: 'a' != 'F'
- a
+ F
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'a' != 'F'
- a
+ F

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_e_decrypt_2
ERROR: Test case for function: decrypt
ERROR: Input: ('a', 2) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: _
ERROR: Expected output: z
ERROR: 'z' != '_'
- z
+ _

ERROR: ----------------------------------------------------------------------------
ERROR: 'z' != '_'
- z
+ _
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'z' != '_'
- z
+ _

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_f_encryptsentence_5
ERROR: Test case for function: encrypt_sentence
ERROR: Input: ('this is a secret message about the class', 5) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: ymnx{nx{f{xjhwjy{rjxxflj{fgtzy{ymj{hqfxx
ERROR: Expected output: ymnxenxefexjhwjyerjxxfljefgtzyeymjehqfxx
ERROR: 'ymnxenxefexjhwjyerjxxfljefgtzyeymjehqfxx' != 'ymnx{nx{f{xjhwjy{rjxxflj{fgtzy{ymj{hqfxx'
- ymnxenxefexjhwjyerjxxfljefgtzyeymjehqfxx
?     ^  ^ ^      ^       ^     ^   ^
+ ymnx{nx{f{xjhwjy{rjxxflj{fgtzy{ymj{hqfxx
?     ^  ^ ^      ^       ^     ^   ^

ERROR: ----------------------------------------------------------------------------
ERROR: 'ymnxenxefexjhwjyerjxxfljefgtzyeymjehqfxx' != 'ymnx{nx{f{xjhwjy{rjxxflj{fgtzy{ymj{hqfxx'
- ymnxenxefexjhwjyerjxxfljefgtzyeymjehqfxx
?     ^  ^ ^      ^       ^     ^   ^
+ ymnx{nx{f{xjhwjy{rjxxflj{fgtzy{ymj{hqfxx
?     ^  ^ ^      ^       ^     ^   ^
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'ymnxenxefexjhwjyerjxxfljefgtzyeymjehqfxx' != 'ymnx{nx{f{xjhwjy{rjxxflj{fgtzy{ymj{hqfxx'
- ymnxenxefexjhwjyerjxxfljefgtzyeymjehqfxx
?     ^  ^ ^      ^       ^     ^   ^
+ ymnx{nx{f{xjhwjy{rjxxflj{fgtzy{ymj{hqfxx
?     ^  ^ ^      ^       ^     ^   ^

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_f_encryptsentence_5
ERROR: Test case for function: encrypt_sentence
ERROR: Input: ('aaaaazzzzzzzz', 10) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: kkkkk
ERROR: Expected output: kkkkkiiiiiiii
ERROR: 'kkkkkiiiiiiii' != 'kkkkk\x84\x84\x84\x84\x84\x84\x84\x84'
- kkkkkiiiiiiii
+ kkkkk

ERROR: ----------------------------------------------------------------------------
ERROR: 'kkkkkiiiiiiii' != 'kkkkk\x84\x84\x84\x84\x84\x84\x84\x84'
- kkkkkiiiiiiii
+ kkkkk
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'kkkkkiiiiiiii' != 'kkkkk\x84\x84\x84\x84\x84\x84\x84\x84'
- kkkkkiiiiiiii
+ kkkkk

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_f_encryptsentence_5
ERROR: Test case for function: encrypt_sentence
ERROR: Input: ('aaaaa zzzzzzzz', 81) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: ²²²²²{ËËËËËËËË
ERROR: Expected output: aaaaa{zzzzzzzz
ERROR: 'aaaaa{zzzzzzzz' != '²²²²²{ËËËËËËËË'
- aaaaa{zzzzzzzz
+ ²²²²²{ËËËËËËËË

ERROR: ----------------------------------------------------------------------------
ERROR: 'aaaaa{zzzzzzzz' != '²²²²²{ËËËËËËËË'
- aaaaa{zzzzzzzz
+ ²²²²²{ËËËËËËËË
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'aaaaa{zzzzzzzz' != '²²²²²{ËËËËËËËË'
- aaaaa{zzzzzzzz
+ ²²²²²{ËËËËËËËË

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_g_decryptsentence_4
ERROR: Test case for function: decrypt_sentence
ERROR: Input: ('ymnxenxefexjhwjyerjxxfljefgtzyeymjehqfxx', 5) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: this`is`a`secret`message`about`the`class
ERROR: Expected output: this is a secret message about the class
ERROR: 'this is a secret message about the class' != 'this`is`a`secret`message`about`the`class'
- this is a secret message about the class
?     ^  ^ ^      ^       ^     ^   ^
+ this`is`a`secret`message`about`the`class
?     ^  ^ ^      ^       ^     ^   ^

ERROR: ----------------------------------------------------------------------------
ERROR: 'this is a secret message about the class' != 'this`is`a`secret`message`about`the`class'
- this is a secret message about the class
?     ^  ^ ^      ^       ^     ^   ^
+ this`is`a`secret`message`about`the`class
?     ^  ^ ^      ^       ^     ^   ^
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'this is a secret message about the class' != 'this`is`a`secret`message`about`the`class'
- this is a secret message about the class
?     ^  ^ ^      ^       ^     ^   ^
+ this`is`a`secret`message`about`the`class
?     ^  ^ ^      ^       ^     ^   ^

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_g_decryptsentence_4
ERROR: Test case for function: decrypt_sentence
ERROR: Input: ('kkkkkiiiiiiii', 10) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: aaaaa________
ERROR: Expected output: aaaaazzzzzzzz
ERROR: 'aaaaazzzzzzzz' != 'aaaaa________'
- aaaaazzzzzzzz
+ aaaaa________

ERROR: ----------------------------------------------------------------------------
ERROR: 'aaaaazzzzzzzz' != 'aaaaa________'
- aaaaazzzzzzzz
+ aaaaa________
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'aaaaazzzzzzzz' != 'aaaaa________'
- aaaaazzzzzzzz
+ aaaaa________

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_g_decryptsentence_4
ERROR: Test case for function: decrypt_sentence
ERROR: Input: ('aaaaa{zzzzzzzz', 81) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output:  ))))))))
ERROR: Expected output: aaaaa zzzzzzzz
ERROR: 'aaaaa zzzzzzzz' != '\x10\x10\x10\x10\x10 ))))))))'
- aaaaa zzzzzzzz
+  ))))))))

ERROR: ----------------------------------------------------------------------------
ERROR: 'aaaaa zzzzzzzz' != '\x10\x10\x10\x10\x10 ))))))))'
- aaaaa zzzzzzzz
+  ))))))))
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'aaaaa zzzzzzzz' != '\x10\x10\x10\x10\x10 ))))))))'
- aaaaa zzzzzzzz
+  ))))))))

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_h_getaminoacids_3
ERROR: Test case for function: get_amino_acids
ERROR: Input: Isoleucine, I, ATT, ATC, ATA
Leucine, L, CTT, CTC, CTA, CTG, TTA, TTG
Valine, V, GTT, GTC, GTA, GTG
Phenylalanine, F, TTT, TTC
Methionine, M, ATG
CYSteine, C, TGT, TGC
Alanine, A, GCT, GCC, GCA, GCG
Glycine, G, GGT, GGC, GGA, GGG
Proline, P, CCT, CCC, CCA, CCG
Threonine, T, ACT, ACC, ACA, ACG
Serine, S, TCT, TCC, TCA, TCG, AGT, AGC
Tyrosine, Y, TAT, TAC
Tryptophan, W, TGG
Glutamine, Q, CAA, CAG
Asparagine, N, AAT, AAC
Histidine, H, CAT, CAC
Glutamic_acid, E, GAA, GAG
AsparTic acid, D, GAT, GAC
Lysine, K, AAA, AAG
Arginine, R, CGT, CGC, CGA, CGG, AGA, AGG
Stop_codons, -, TAA, TAG, TGA
ERROR: Actual output: {('ATT', 'ATC', 'ATA'): ['Isoleucine', 'I'], ('CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'): ['Leucine', 'L'], ('GTT', 'GTC', 'GTA', 'GTG'): ['Valine', 'V'], ('TTT', 'TTC'): ['Phenylalanine', 'F'], ('ATG',): ['Methionine', 'M'], ('TGT', 'TGC'): ['CYSteine', 'C'], ('GCT', 'GCC', 'GCA', 'GCG'): ['Alanine', 'A'], ('GGT', 'GGC', 'GGA', 'GGG'): ['Glycine', 'G'], ('CCT', 'CCC', 'CCA', 'CCG'): ['Proline', 'P'], ('ACT', 'ACC', 'ACA', 'ACG'): ['Threonine', 'T'], ('TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'): ['Serine', 'S'], ('TAT', 'TAC'): ['Tyrosine', 'Y'], ('TGG',): ['Tryptophan', 'W'], ('CAA', 'CAG'): ['Glutamine', 'Q'], ('AAT', 'AAC'): ['Asparagine', 'N'], ('CAT', 'CAC'): ['Histidine', 'H'], ('GAA', 'GAG'): ['Glutamic_acid', 'E'], ('GAT', 'GAC'): ['AsparTicacid', 'D'], ('AAA', 'AAG'): ['Lysine', 'K'], ('CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'): ['Arginine', 'R'], ('TAA', 'TAG', 'TGA'): ['Stop_codons', '-']}
ERROR: Expected output: {('ATT', 'ATC', 'ATA'): ['Isoleucine', 'I'], ('CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'): ['Leucine', 'L'], ('GTT', 'GTC', 'GTA', 'GTG'): ['Valine', 'V'], ('TTT', 'TTC'): ['Phenylalanine', 'F'], ('ATG',): ['Methionine', 'M'], ('TGT', 'TGC'): ['CYSteine', 'C'], ('GCT', 'GCC', 'GCA', 'GCG'): ['Alanine', 'A'], ('GGT', 'GGC', 'GGA', 'GGG'): ['Glycine', 'G'], ('CCT', 'CCC', 'CCA', 'CCG'): ['Proline', 'P'], ('ACT', 'ACC', 'ACA', 'ACG'): ['Threonine', 'T'], ('TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'): ['Serine', 'S'], ('TAT', 'TAC'): ['Tyrosine', 'Y'], ('TGG',): ['Tryptophan', 'W'], ('CAA', 'CAG'): ['Glutamine', 'Q'], ('AAT', 'AAC'): ['Asparagine', 'N'], ('CAT', 'CAC'): ['Histidine', 'H'], ('GAA', 'GAG'): ['Glutamic_acid', 'E'], ('GAT', 'GAC'): ['AsparTic acid', 'D'], ('AAA', 'AAG'): ['Lysine', 'K'], ('CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'): ['Arginine', 'R'], ('TAA', 'TAG', 'TGA'): ['Stop_codons', '-']}
ERROR: {('AT[746 chars]arTicacid', 'D'], ('AAA', 'AAG'): ['Lysine', '[107 chars]'-']} != {('AT[746 chars]arTic acid', 'D'], ('AAA', 'AAG'): ['Lysine', [108 chars]'-']}
Diff is 1047 characters long. Set self.maxDiff to None to see it.
ERROR: ----------------------------------------------------------------------------
ERROR: {('AT[746 chars]arTicacid', 'D'], ('AAA', 'AAG'): ['Lysine', '[107 chars]'-']} != {('AT[746 chars]arTic acid', 'D'], ('AAA', 'AAG'): ['Lysine', [108 chars]'-']}
Diff is 1047 characters long. Set self.maxDiff to None to see it.
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 414, in test_h_getaminoacids_3
    self.assertEqual(actual_output, amino_acid_dict)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1128, in assertDictEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: {('AT[746 chars]arTicacid', 'D'], ('AAA', 'AAG'): ['Lysine', '[107 chars]'-']} != {('AT[746 chars]arTic acid', 'D'], ('AAA', 'AAG'): ['Lysine', [108 chars]'-']}
Diff is 1047 characters long. Set self.maxDiff to None to see it.
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_m_Function_4_point
ERROR: Test case for function: x
ERROR: Input: ('x', (0, 1, -1))
ERROR: Actual output: [None, None, None]
ERROR: Expected output: [0, 1, -1]
ERROR: unsupported operand type(s) for -: 'list' and 'list'
ERROR: ----------------------------------------------------------------------------
ERROR: unsupported operand type(s) for -: 'list' and 'list'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 522, in test_m_Function_4_point
    self.assertAlmostEqual(actual_output, expected_output, 2)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 860, in assertAlmostEqual
    diff = abs(first - second)
TypeError: unsupported operand type(s) for -: 'list' and 'list'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_m_Function_4_point
ERROR: Test case for function: x + x
ERROR: Input: ('x + x', (0, 1, -1))
ERROR: Actual output: [None, None, None]
ERROR: Expected output: [0, 2, -2]
ERROR: unsupported operand type(s) for -: 'list' and 'list'
ERROR: ----------------------------------------------------------------------------
ERROR: unsupported operand type(s) for -: 'list' and 'list'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 522, in test_m_Function_4_point
    self.assertAlmostEqual(actual_output, expected_output, 2)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 860, in assertAlmostEqual
    diff = abs(first - second)
TypeError: unsupported operand type(s) for -: 'list' and 'list'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_m_Function_4_point
ERROR: Test case for function: x*x + 1
ERROR: Input: ('x*x + 1', (-2, 0, 2))
ERROR: Actual output: [None, None, None]
ERROR: Expected output: [5, 1, 5]
ERROR: unsupported operand type(s) for -: 'list' and 'list'
ERROR: ----------------------------------------------------------------------------
ERROR: unsupported operand type(s) for -: 'list' and 'list'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 522, in test_m_Function_4_point
    self.assertAlmostEqual(actual_output, expected_output, 2)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 860, in assertAlmostEqual
    diff = abs(first - second)
TypeError: unsupported operand type(s) for -: 'list' and 'list'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_n_Function_4_derivative
ERROR: Test case for function: 1/x
ERROR: Input: ('1/x', (10,))
ERROR: Actual output: [None]
ERROR: Expected output: [-0.010000000000287557]
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ----------------------------------------------------------------------------
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 549, in test_n_Function_4_derivative
    self.assertAlmostEqual(actual, expected, 2)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 860, in assertAlmostEqual
    diff = abs(first - second)
TypeError: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_n_Function_4_derivative
ERROR: Test case for function: x**2 - x
ERROR: Input: ('x**2 - x', (2,))
ERROR: Actual output: [None]
ERROR: Expected output: [2.999999999908631]
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ----------------------------------------------------------------------------
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 549, in test_n_Function_4_derivative
    self.assertAlmostEqual(actual, expected, 2)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 860, in assertAlmostEqual
    diff = abs(first - second)
TypeError: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_n_Function_4_derivative
ERROR: Test case for function: x**2
ERROR: Input: ('x**2', (3,))
ERROR: Actual output: [None]
ERROR: Expected output: [5.999999999772853]
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ----------------------------------------------------------------------------
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 549, in test_n_Function_4_derivative
    self.assertAlmostEqual(actual, expected, 2)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 860, in assertAlmostEqual
    diff = abs(first - second)
TypeError: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_n_Function_4_derivative
ERROR: Test case for function: 2*x
ERROR: Input: ('2*x', (-1, 0, 1))
ERROR: Actual output: [None, None, None]
ERROR: Expected output: [2.0, 2.0, 2.0]
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ----------------------------------------------------------------------------
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 549, in test_n_Function_4_derivative
    self.assertAlmostEqual(actual, expected, 2)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 860, in assertAlmostEqual
    diff = abs(first - second)
TypeError: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_n_Function_4_derivative
ERROR: Test case for function: 10
ERROR: Input: ('10', (-1000, 0, 199))
ERROR: Actual output: [None, None, None]
ERROR: Expected output: [0.0, 0.0, 0.0]
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ----------------------------------------------------------------------------
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 549, in test_n_Function_4_derivative
    self.assertAlmostEqual(actual, expected, 2)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 860, in assertAlmostEqual
    diff = abs(first - second)
TypeError: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_o_Function_4_integral
ERROR: Test case for function: 1/x
ERROR: Input: ('1/x', (1, 2))
ERROR: Actual output: None
ERROR: Expected output: 0.6932539682539682
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ----------------------------------------------------------------------------
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 574, in test_o_Function_4_integral
    self.assertAlmostEqual(actual_output, expected_output, 2)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 860, in assertAlmostEqual
    diff = abs(first - second)
TypeError: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_o_Function_4_integral
ERROR: Test case for function: x**2 - x
ERROR: Input: ('x**2 - x', (1, 4))
ERROR: Actual output: None
ERROR: Expected output: 13.5
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ----------------------------------------------------------------------------
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 574, in test_o_Function_4_integral
    self.assertAlmostEqual(actual_output, expected_output, 2)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 860, in assertAlmostEqual
    diff = abs(first - second)
TypeError: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_o_Function_4_integral
ERROR: Test case for function: x**2
ERROR: Input: ('x**2', (0, 3))
ERROR: Actual output: None
ERROR: Expected output: 9.0
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ----------------------------------------------------------------------------
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 574, in test_o_Function_4_integral
    self.assertAlmostEqual(actual_output, expected_output, 2)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 860, in assertAlmostEqual
    diff = abs(first - second)
TypeError: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_o_Function_4_integral
ERROR: Test case for function: 2*x
ERROR: Input: ('2*x', (0, 1))
ERROR: Actual output: None
ERROR: Expected output: 1.0
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ----------------------------------------------------------------------------
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 574, in test_o_Function_4_integral
    self.assertAlmostEqual(actual_output, expected_output, 2)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 860, in assertAlmostEqual
    diff = abs(first - second)
TypeError: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_o_Function_4_integral
ERROR: Test case for function: 2*x
ERROR: Input: ('2*x', (-1, 1))
ERROR: Actual output: None
ERROR: Expected output: 0.0
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ----------------------------------------------------------------------------
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 574, in test_o_Function_4_integral
    self.assertAlmostEqual(actual_output, expected_output, 2)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 860, in assertAlmostEqual
    diff = abs(first - second)
TypeError: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_o_Function_4_integral
ERROR: Test case for function: 10
ERROR: Input: ('10', (-9, 10))
ERROR: Actual output: None
ERROR: Expected output: 190.0
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ----------------------------------------------------------------------------
ERROR: unsupported operand type(s) for -: 'NoneType' and 'float'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/pmanolis/Assignment7/a7_hidden_test.py", line 574, in test_o_Function_4_integral
    self.assertAlmostEqual(actual_output, expected_output, 2)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 860, in assertAlmostEqual
    diff = abs(first - second)
TypeError: unsupported operand type(s) for -: 'NoneType' and 'float'
ERROR: ============================================================================
```
```
