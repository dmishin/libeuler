Lib Euler
=========

A library of some simple number-theoretic and some other functions, written mainly while solving problems from the projecteuler.net

Written for Python 3, but should be easy to backport.

Features
--------

The set of cuntions is assorted and incomplete. Primes and prime factorization, decimal and other digits, phi and mu functions, Fibonacci numbers etc. Also provides classes for modular arithmetics and rational numbers.

Installation
------------

python setup.py install


Examples
--------

First primes below 50:

    from libeuler.numtheor import primes
    print( primes( 50 ) )

    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


