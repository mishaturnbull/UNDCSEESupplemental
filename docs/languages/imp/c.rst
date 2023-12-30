.. index::
   single: c
   triple: programming language; imperative; c

.. _topics/languages/imp/c:

C
==

The C language is a strong-typed, compiled, imperative programming language.
It is often considered low level, but `there are those who hold C as a high
level language <https://queue.acm.org/detail.cfm?id=3212479>`_ as well.

.. todo::

   INET add outlinks for C (*find* the official C standard?? docs??)

.. todo::

   seealso for the rest of the C family (C++, objC.  C# is a bastard child of
   Microsoft, C++, and Java, and shouldn't be counted as part of the C family)

Syntax
------

C syntax is often considered more explicit than some other languages, and
frequently involves explicit referencing of pointers to memory rather than
passing variables by value.

.. code-block:: c
   :caption: A hello world example in C
   :linenos:

   // C comments use double slashes

   /*
    * or, a /* to start a block comment, and the reverse to end them.
    */

   #include <stdio.h>

   int main() {
       printf("Hello, world!\n");
       return 0;
   }

