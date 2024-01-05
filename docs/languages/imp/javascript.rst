.. index::
   single: javascript
   triple: programming language; imperative; javascript

.. _topics/languages/imp/javascript:

JavaScript
==========

.. todo::

   I *hate* JavaScript.  Quite a lot.  And am not very good at it.

   Someday, someone who doesn't may wish to (re)write this page with less
   anger.

JavaScript is an interpreted, weakly-typed, imperative programming language
commonly used in web applications.  It is frequently seen embedded in
:ref:`topics/languages/dec/HTML` to make pages interactive.

.. seealso::

   * `ECMAScript standard
     <https://ecma-international.org/publications-and-standards/standards/ecma-262/>`_
     that more or less officially defines JavaScript

     * https://stackoverflow.com/a/30113184, a bit of background on why that
       page is called ECMAScript.  TL;DR: JavaScript is a language ("the"
       language) that implements the ECMAScript standard

   * Javascript is frequently seen alongside :ref:`topics/languages/dec/HTML`

   Note that "Java" is not on this list.  Java is to JavaScript as ham is to a
   hamster -- sharing in naming only.

Syntax
------

.. code-block:: javascript
   :caption: Hello World in Javascript
   :linenos:

   const heading = document.querySelector("h1");
   heading.textContent = "Hello, world!";

