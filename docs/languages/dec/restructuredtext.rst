.. index::
   single: restructuredtext
   triple: programming language; declarative; restructuredtext

.. _topics/languages/dec/restructuredtext:

reStructuredText
================

*Behold: a description of rST, written in rST!*

reStructuredText is a markup syntax designed to be *readable* in source format,
but best when rendered.  It was originally created as part of the docutils
project, and now is commonly found in Sphinx documentation.

This document (and most of this website) is written in reStructuredText.

.. seealso::

   * The `docutils standard for rST <https://docutils.sourceforge.io/rst.html>`_
   * Sphinx's `extra documentation for rST
     <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_

     * Note that Sphinx's implementation of rST *extends* that of docutils; not
       everything Sphinx does will work in pure docutils.

   * :ref:`topics/languages/dec/markdown`, a comparable markup language leaning
     more towards "readable in source format"

Syntax
------

reStructuredText is comprised of paragraphs and directives, with roles and
inline markup mixed in.

.. code-block:: restructuredtext
   :caption: An example of rST
   :linenos:

   This is a heading
   =================

   This is a paragraph!  Hello, world!  Hello, world!  Hello, world!  Hello,
   world!  Hello, world!  Hello, world!  Hello, world!  Hello, world!

   .. code-block:: restructuredtext
      :caption: An example of rST, within an example of rST
      :linenos:

      This is the "show example code" block used to show this example!

