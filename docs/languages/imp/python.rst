.. index::
   single: python
   triple: programming language; imperative; python

.. _topics/languages/imp/python:

Python
======

Python is a high level, weakly-typed, interpreted, imperative programming
language.  It is generally considered a good language for early programming
education, for its quick write-run-debug cycle and (debatably) out-of-the-way
syntax.

.. seealso::

   * `Python 3 Documentation <https://docs.python.org/3/index.html>`_

.. attention::

   There are three major versions of Python: Python 1, Python 2, and Python 3.

   **USE PYTHON 3.**

   Py 2 has been past end of life since 2020.

Syntax
------

Python's syntax is whitespace-oriented, with scopes identified by their
indentation after a colon.  The language is *fairly* keyword-oriented rather
than symbol-oriented (`what? <https://xkcd.com/1306/>`_).  The language takes a
"batteries included" approach, supplying a standard library of importable
modules capable of a wide variety of tasks.

.. code-block:: python
   :caption: Example Python
   :linenos:

   # python comments start with hashtags

   import math

   def foo(x):
       """
       The foo(x) function accepts one argument ``x``, and returns the square
       root of x.
       """

       return math.sqrt(x)

   print("The square root of 9 is " + str(foo(9)))

.. code-block:: python
   :caption: An is-even function in Python
   :linenos:

   def is_even(i):
       """
       Given a positive integer ``i``, this function returns whether or not
       ``i`` is an even number (evenly divisible by 2).

       Figuring out how this works is a good exercise to understand Python data
       types, moving between them, string indexing, and "truthiness."
       """
       return not bool(int(bin(i)[2:][::-len(bin(i))][0]))

   if is_even(5):
       print("Five is even??")
   else:
       print("Five is odd.")

