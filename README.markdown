# Stochastic SMT

This is to try out various ideas related to combining SMT solvers with probabilistic programming. Currently, there is a very minimal probabilistic language that supports sampling from distributions with deterministic constraints.

The code in ext/z3py/z3py is from the Z3 source available at [the Z3 website](http://research.microsoft.com/en-us/um/redmond/projects/z3/index.html). It has been packaged as a python library.

To use, you will need Python 2.6 and if you are not on OS X, to build the Z3 library for your system. The library should be placed in `ext/z3py/z3py`. Then, get that directory into `PYTHONPATH` using your favorite method.

Issue `python ssmt.py` for a test. This uses the SampleTreeSearch algorithm described in "Uniform Solution Sampling Using a Constraint Solver As an Oracle" (Ermon et al, UAI 2012) to produce samples.

