# Example of Unit tests

In this example, we will create a simple unit test for a function. As you work on your project, you will want to write unit tests for your functions. Unit tests are a way to test your code to make sure it works as expected. You can run unit tests to make sure your code is working as expected before you submit it. The unit tests will show you your code works without having to run the project and enter the same input over and over.

## Run the project to see what it does. 

```bash
python3 app.py
```

## Install the Test Library

We will be using pytest for testing 

```bash
pip3 install pytest
```

## Run the tests

The tests are in the `test_app.py` file. The `test_` prefix is important. The `test_` prefix tells pytest that this is a test.
When you run the tests, pytest will look for all files that start with `test_` and run all the functions that start with `test_`.

```bash
pytest
```

You should see something like this:

```
$ pytest
======================================================================================================= test session starts =======================================================================================================
platform darwin -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
rootdir: /Users/djm/Projects/test-python
collected 2 items                                                                                                                                                                                                                 

test_app.py ..                                                                                                                                                                                                              [100%]

======================================================================================================== 2 passed in 0.00s ========================================================================================================
```

Our 2 tests are passing!

## Modify the test, and see it fail

We want to be excited, when we greet someone. So let's modify the test to check for an exclamation mark. 

In test_app.py, change the test_greet functions to:

```python   
def test_greetDuane():
    response = app.greet('Duane')
    assert response == 'Hello Duane!'


def test_greetBob():
    response = app.greet('Bob')
    assert response == 'Hello Bob!'
```

You should see something like this:

```
$ pytest
======================================================================================================= test session starts =======================================================================================================
platform darwin -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
rootdir: /Users/djm/Projects/test-python
plugins: cov-4.0.0
collected 2 items                                                                                                                                                                                                                 

test_app.py FF                                                                                                                                                                                                              [100%]

============================================================================================================ FAILURES =============================================================================================================
_________________________________________________________________________________________________________ test_greetDuane _________________________________________________________________________________________________________

    def test_greetDuane():
        response = app.greet('Duane')
>       assert response == 'Hello Duane!'
E       AssertionError: assert 'Hello Duane' == 'Hello Duane!'
E         - Hello Duane!
E         ?            -
E         + Hello Duane

test_app.py:6: AssertionError
__________________________________________________________________________________________________________ test_greetBob __________________________________________________________________________________________________________

    def test_greetBob():
        response = app.greet('Bob')
>       assert response == 'Hello Bob!'
E       AssertionError: assert 'Hello Bob' == 'Hello Bob!'
E         - Hello Bob!
E         ?          -
E         + Hello Bob

test_app.py:11: AssertionError
===================================================================================================== short test summary info =====================================================================================================
FAILED test_app.py::test_greetDuane - AssertionError: assert 'Hello Duane' == 'Hello Duane!'
FAILED test_app.py::test_greetBob - AssertionError: assert 'Hello Bob' == 'Hello Bob!'
======================================================================================================== 2 failed in 0.02s ========================================================================================================
```

Can you tell from the output what's wrong?

## Update the code to make the tests pass
 
In app.py, change the return value to include an exclamation mark.

```python   
def greet(name):
    return f"Hello {name}!"
```

Now run the tests again, and they should be passing again.


```bash
pytest
```

## Run the tests with coverage

```bash
pip3 install pytest-cov

pytest --cov=.
```

You should see something like this:

```
$ pytest --cov=.
======================================================================================================= test session starts =======================================================================================================
platform darwin -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
rootdir: /Users/djm/Projects/test-python
plugins: cov-4.0.0
collected 2 items                                                                                                                                                                                                                 

test_app.py ..                                                                                                                                                                                                              [100%]

---------- coverage: platform darwin, python 3.10.9-final-0 ----------
Name          Stmts   Miss  Cover
---------------------------------
app.py            7      3    57%
test_app.py       7      0   100%
---------------------------------
TOTAL            14      3    79%


======================================================================================================== 2 passed in 0.01s ========================================================================================================
```

This shows us that we have 57% coverage on our real code. We have 2 tests, and 7 lines of code. 3 lines of code are not covered by the tests.
In this case, it's not a big deal. Since the main method is not covered. This is what takes the input and calls the function that does the real work. In a real project, you would want to cover most of your complex code. So you can be confident that it works as expected.

