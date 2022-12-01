Curve fitter

A simple tool for an optimization problem in the field of positron emission tomography: 2-tracer compartment model (2TCM).

![logo](https://user-images.githubusercontent.com/43485534/204952545-781da68d-362b-41b2-9f48-04f6fb72724a.png)

Determining the parameters K1, k2, k3, and k4, and Vb for a 2TCM is of physiological interest, but there is no easy and inexpensive way to do this. Accordingly, this repository will serve as the base for an extension in the open-source software 3D Slicer (https://www.slicer.org/).

Curve fitting a 2TCM is computationally interesting because it is an NP-hard problem. More specifically, the problem is nonconvex, has 5 variables, constrained, and continuous.

* Convex vs nonconvex: Non-convex problems are much harder to solve than convex problems. Convex problems can be solved by gradient descent, while non-convex problems require advanced techniques because they have multiple local minima.
* Number of variables: Increasing the number of variables multiplies the candidate space, making the search harder.
* Constrained vs unconstrained: Constrained problems are easier to solve than unconstrained problems. This is because unconstrained problems have more degrees of freedom, which in turn means that they have more local minima.
* Discrete vs continous: Discrete problems are easier to solve than continous problems. A constrained continuous problem with no precision constraints is equivalent to an unconstrained discrete problem.

