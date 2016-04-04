# Package Template for a Project Using Cython

[![build status](http://img.shields.io/travis/jakevdp/cython_template/master.svg?style=flat)](https://travis-ci.org/jakevdp/cython_template)
[![license](http://img.shields.io/badge/license-BSD-blue.svg?style=flat)](https://github.com/jakevdp/cython_template/blob/master/LICENSE)

This is a package template for a Python project using Cython. There are many
different ways to build cython extensions within a project, as seen in the
[Cython documentation](http://docs.cython.org/src/quickstart/build.html), but
the best way to integrate Cython into a distributed package is not always clear.

This template borrows utility scripts used in the [scipy](http://scipy.org)
and [scikit-learn](http://scikit-learn.org) projects, which give the template
a few nice features:

- Cython is required when the package is built, but not when the package is
  installed from a distributed source. That means that cython-generated C
  code is not included in the git repository, but *is* automatically included
  in any distribution. Further, it means that Cython is a requirement for
  package developers, but not for package users.
- The ``__check_build`` submodule includes scripts which detect whether the
  package has been properly built, and raise useful errors if this is not the
  case. This is especially important for when users try to import the package
  from the source directory without first building/compiling the cython
  sources.

Note that any "*.pyx" files added to the repository will have to be explicitly
added to the ``setup.py`` file within the same directory: in most cases you
should be able to simply copy the example [``setup.py``](https://github.com/jakevdp/cython_template/blob/master/cython_template/setup.py) within this repository.

This repository has a very permissive BSD license: please feel free to
use the contents to help set up your own cython-driven packages!