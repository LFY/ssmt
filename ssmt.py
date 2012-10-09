#
# Stochastic SMT
#

from searchtreesample import *

# Global store of addresses, constraints, and variables

addr_idx = 0
constraints = []
variables = []

def reset():
    """Reset the global store to its initial state."""
    constraints = []
    variables = []
    addr_idx = 0

def gen_addr(name = None):
    """Generate an address w/ optional prefix NAME, which has default value "v"."""
    global addr_idx
    if name == None:
        name = "v"
    res = name + "_" + str(addr_idx)
    addr_idx += 1
    return res

def add_var(vartype, name = None):
    """Add a variable of the given type. We use z3py variables as random variables."""
    res = vartype(gen_addr(name))
    variables.append(res)
    return res

def observe(f):
    """Adds the constraint F to the distribution."""
    constraints.append(f)

def sample(num_samples, proc):
    """Produces NUM_SAMPLES distributed according to PROC, which contains statements
    that produce random variables / constraints."""

    reset()
    proc()

    final_formula = True if constraints == [] else And(*constraints)
    return map(lambda i: search_tree_sample(variables, final_formula, 2), range(num_samples))

# Tests

def randint(a, b, name = None):
    res = add_var(Int, name)
    constraints.append(And(res >= a, res <= b))
    return res

def flip(name = None):
    res = add_var(Bool, name)
    return res

def add(x, y):
    z = add_var(Int)
    constraints.append(z == x + y)
    return z

def cond(c, t, e, restype = Int):
    cv = add_var(Bool)
    res = add_var(restype)
    constraints.append(cv == c)
    constraints.append(Implies(cv, res == t))
    constraints.append(Implies(Not(cv), res == e))
    return res

def test():

    def model():
        b = flip(name = "b")
        x1 = randint(0, 10, name = "x1")
        x2 = randint(0, 10, name = "x2")
        x3 = add(x1, x2)
        observe(Implies(b, x3 == 6))
        observe(Implies(Not(b), x3 == 10))

    samples = sample(100, model)
    for s in samples:
        print s

test()
