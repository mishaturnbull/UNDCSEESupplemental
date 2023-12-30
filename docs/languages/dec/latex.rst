.. index::
   single: latex
   single: pdf
   triple: programming language; declarative; latex

.. _topics/languages/dec/latex:

LaTeX
=====

LaTeX (pronounced "Lay-Tek") is a document typesetting system created by Donald
Knuth.  Primarily, it is nowadays used to generate PDF files from static code
in a non-WYSIWYG workflow.

.. todo::

   INET outbound links for LaTeX

.. todo::

   Seealso links for LaTeX compilers (at least miktex and pdftex)

Syntax
------

LaTeX source is often notable for lots of backslashes and curly braces.  It
uses backslashes as a command indicator, and curly braces for command
arguments.

.. code-block:: latex
   :caption: Example LaTeX code
   :linenos:

   \documentclass{article}

   % LaTeX comments use percent signs

   \title{A \LaTeX example}
   \author{Michael Turnbull}
   \date{\today}

   \begin{document}

   \maketitle

   Hello, world!  This is some text that will appear in a document.

   \end{document}

LaTeX files typically end in ``.tex``.  They require a compiler to be
transformed into desired output.

