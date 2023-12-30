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

.. todo::

   INET outlinks to JavaScript (is there an official doc?  w3schools?)

.. seealso::

   * Javascript is frequently seen alongside :ref:`topics/languages/dec/HTML`

Syntax
------

.. code-block:: javascript
   :caption: Hello World in Javascript
   :linenos:

   const heading = document.querySelector("h1");
   heading.textContent = "Hello, world!";

