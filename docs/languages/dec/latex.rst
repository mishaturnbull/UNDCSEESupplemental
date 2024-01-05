.. index::
   single: latex
   single: pdf
   triple: programming language; declarative; latex

.. _topics/languages/dec/latex:

LaTeX
=====

LaTeX (pronounced "Lay-Tek") is a document typesetting system created by Leslie
Lamport.  Primarily, it is nowadays used to generate PDF files from static code
in a non-WYSIWYG workflow.

.. seealso::

   * `LaTeX Project homepage <https://www.latex-project.org/>`_
   * `TeX Live <https://www.tug.org/texlive/>`_, a TeX distribution and
     compiler
   * `MiKTex <https://miktex.org/>`_, a TeX distribution and compiler

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

