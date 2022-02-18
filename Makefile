NAME=DSLR

.PHONE: install test clean

install:
    @python3 -m pip install -r requirements.txt

clean:
    @python3 setup.py clean
    @rm-fr $(NAME)