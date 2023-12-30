.. index::
   single: markdown
   triple: programming language; declarative; markdown

.. _topics/languages/dec/markdown:

Markdown
========

Markdown is a declarative "markup" language designed to easily convey meaning
in both plaintext (source) format and when rendered.  Most commonly, markdown
engines produce HTML as output which is viewable in any web browser, though
other engines exist which transform markdown directly to PDF.

.. todo::

   INET Markdown outbound links -- need at least official spec

.. seealso::

   * :ref:`topics/languages/dec/restructuredtext`, a comparable markup language
     leaning more towards "prettier when rendered"

Syntax
------

Plain Markdown syntax is notable for its simplicity.  It uses hashtags to
denote headings, asterisks for emphasis, and backticks for monospaced font.
Multiple hashtags indicate leveled headings, and multiple asterisks indicate
italics/bold/both.

.. code-block:: markdown
   :caption: Example plain Markdown
   :linenos:

   # This is a level 1 heading

   That heading is equivalent to `<h1>This is a level 1 heading</h1>` in HTML.
   That snip of HTML will be monospaced, because it is wrapped in backticks.

   *This text is in italics*, **this text in bold**, ***and this in both
   italics and bold***.

.. todo::

   Github-flavored markdown syntax (maybe Bitbucket too?  though, from
   experience, that standard does NOT match perfectly with what bitbucket
   *actually* does)

