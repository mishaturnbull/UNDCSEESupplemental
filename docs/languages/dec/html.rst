.. index::
   single: html
   triple: programming language; declarative; html

.. _topics/languages/dec/html:

HTML
====

HyperText Markup Language (HTML) is a derivative of XML designed for use in the
`the tubes <https://xkcd.com/181/>`_.  It is what almost all modern (static)
webpages are written in.

.. todo::

   Seealso links to CSS (and XML), when those pages are written (ideally by
   someone without disdain for web development)

.. seealso::

   * `WHATWG Living Standard <https://html.spec.whatwg.org/multipage/>`_, the
     official "always updated" HTML specification
     
     * https://stackoverflow.com/a/34984276 , an interesting note on W3C vs
       WHATWG (and why I chose to put the WHATWG link there instead of W3C's
       standard)

   * HTML also frequently includes :ref:`topics/languages/imp/javascript` to
     improve interactability

Syntax
------

As a derivative of XML, much of HTML's basic syntax derives from that.
However, there are many tags which have meaning.

.. code-block:: html
   :caption: Example HTML
   :linenos:

   <!DOCTYPE HTML>

   <!-- HTML comments are wrapped in this kind of tag (and may span multiple
   lines) -->

   <html>
       <head>
           <meta charset="utf-8" />
           <title>This is the title of a page!</title>
       </head>
       <body>
           This is just some regular text, floating out and about in the body.

           <p>This is a paragraph!</p>

           <b>This text is bold.</b>

           <a href="https://example.com">This text is a link to example.com</a>
       </body>
   </html>

HTML files typically end in ``.html``.  Any modern web browser can open an HTML
file and render it; this is really all that happens when browsing the internet
(the only difference is where the HTML is -- on your machine, or being
downloaded from the remote server).

