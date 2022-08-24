# MechEight test

This app is developed to pass the challenge from MechEight and achieve a position in its headquarters. The functionality of this is read a list of numbers and a number from the command line and determine if the sum of two different numbers inside of the list is equals to the expected result, then this will print out the pair values separated by a colon.

Install dependencies

```bash
python -m pip install requirements.txt
```

How to test

```bash
python -m pytest src
```

How to run

```bash
python src/app.py 1,9,5,0,20,-4,12,16,7 12
```

How to measure the execution

```bash
# if you have installed xclip you just run this
python -c "import random;print(','.join([str(random.randint(0,100)) for x in range(1001)]))" | xclip -selection c
# paste that result into the execution
time python src/app.py <list_of_numbers> 12
# with 1000 numbers a I found this execution results
# python src/app.py  12  0,07s user 0,02s system 96% cpu 0,086 total
```

Coverage

```bash
coverage run -m pytest src
coverage report -m
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
src/__init__.py           0      0   100%
src/test_two_sum.py      10      0   100%
src/test_utils.py         7      0   100%
src/two_sum.py            6      0   100%
src/utils.py              7      0   100%
---------------------------------------------------
TOTAL                    30      0   100%
```
