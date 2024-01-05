.. index::
   single: java
   triple: programming language; imperative; java

.. _topics/languages/imp/java:

Java
====

Java is a high-level, object-oriented, strongly typed, imperative programming
language.  By design, it is platform independent; running on an abstracted Java
Virtual Machine (JVM).

.. seealso::

   * `Oracle's official Java documentation
     <https://docs.oracle.com/en/java/>`_.  In most cases, you probably want
     the `Java SE subpage <https://docs.oracle.com/en/java/javase/21/>`_.

Syntax
------

..
   I don't really know what to say about java syntax here... personally, I hate
   it, so maybe I'm not the best person for this section lol -misha

.. code-block:: java
   :caption: A hello world example in Java
   :linenos:

   // Java comments, similar to C, are double slashes

   /* or, block comments start with /*
    * and end with the reverse
    */

   public class HelloWorld {
       public static void main(String[] args) {
           System.out.println("Hello, world!");
       }
   }

