=============================================
 Some Experiments Around Dirichlet Processes
=============================================

Pólya's Urn — Basic
===================

* Random generator of elements of an unordered set.
* Giant urn containing some number of balls of each colour.
* To get a sample, draw from the urn.
* Replace the ball and *add another* of the same colour

**Every observation increases the likelihood of that observation.**


Pólya's Urn — Dirichlet Process
===============================

* Urn intially has one black ball.
* To generate a sample, draw a ball from the urn.

  * As before, except:

    * If we draw black, select a new colour that has never been in the urn.

Alpha
=====

* More generally, start with alpha black balls.
* alpha can be fractional, but breaks analogy.


