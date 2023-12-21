# Contributing guidelines

First off, please also see this repository's code of conduct.  All
contributions must be in accordance with that.

This repository welcomes contributions from past, present, and future UND
students as well as members of the general community so long as they are
constructive in nature and serve to better the information here.  Please
understand that all changes must be reviewed by moderators before being
accepted; this is done with GitHub's pull requests.  These moderators have the
final authority on whether or not to accept any changes.

## Git practices

Where possible, please sign your commits with one or more of the following
methods.  This is not *required*, but much appreciated.

1. (Most preferred) GPG public key signature (`git commit -S`)
2. (Preferred) Commit message signoff (`git commit -s`)

Where possible, please do *not* do any of the following:

1. Change history after it's been pushed (generally, this means no force pushes)

## Documentation practices

In order to keep information findable, please adhere to the following practices
as much as possible.  As with all programming standards, cleanliness takes
priority over these rules -- if following them makes the documentation worse,
don't hesitate to break the rules.  However, please be able to justify the
breaking.

1. Each page should get an index block at the top of the page.

   * These blocks (see Sphinx's ``index`` markup) should include as many index
     entries as are relevant to the page.  If in doubt, overindexing is
     preferred to underindexing.
   * As much as possible, use existing index terms!  We want to avoid the case
     where there's multiple terms in the index that mean the same thing -- for
     example, ``debuggers`` and ``debugger`` should be combined.  If you're
     first to a topic, congratulations -- you get to pick the index term!

2. Each page should get a unique label at the top of the page.

   * These labels generally look like ``.. _topic/vcs/git:`` in order to
     identify *what* is on the apge, and roughly the page tree it's under. 
   * Yes, I agree... it looks uglier that the label comes after the index.
     But, try it yourself and see - Sphinx doesn't handle the label mapping
     correctly if it's label-then-index!

3. Hard-wrap source lines to, at most, 80 characters

   * This helps with splitscreening on common monitors
   * In Vim, this can be aided with visual mode ``gq`` which will auto-wrap
     selected lines for you
   * Most editors have some equivalent ability

4. Avoid duplicating information

   * Having the same information in multiple places generally increases overall
     effort for readers and writers.  Readers can easily be confused as to
     which is the "correct" source of information (if they disagree), and
     writers now have to update multiple places with the same change if updates
     / corrections are needed.
   * If you find yourself in the common situation where it feels necessary to
     include information that's covered elsewhere, or snippets of it, add as
     little information as possible and then a ``.. seealso::`` at both ends of
     the "link".  For example, if I want to discuss TeXlive in the compilers
     section but it's already covered in documentation tools, I'd add a
     sentence or two about what it is, then add a seealso to the proper
     section.  I'd also add a seealso from the TeXlive page back to the
     compilers section.

5. Write and structure documentation such that it appears similarly structured
   in both HTML and PDF formats

