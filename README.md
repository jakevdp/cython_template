# Package Template for a Project Using Cython

[![build status](http://img.shields.io/travis/jakevdp/cython_template/master.svg?style=flat)](https://travis-ci.org/jakevdp/cython_template)
[![license](http://img.shields.io/badge/license-BSD-blue.svg?style=flat)](https://github.com/jakevdp/cython_template/blob/master/LICENSE)

This is a package template for a Python project using Cython. There are many
different ways to build cython extensions within a project, as seen in the
[Cython documentation](http://docs.cython.org/src/quickstart/build.html).

This template borrows utility scripts used in the [scipy](http://scipy.org)
and [scikit-learn](http://scikit-learn.org) projects, which give the template
a few nice features:

- Cython is required when the package is built, but not when the package is
  installed from a distributed source. That means that cython-generated C
  code is not included in the git repository, but *is* automatically included
  in any distribution.
- The ``__check_build`` submodule includes scripts which detect whether the
  package has been properly built, and raise useful errors if this is not the
  case. This is especially important for when users try to import the package
  from the source directory without first building/compiling the cython
  sources.

This repository has a very permissive BSD license: please use the contents to
help setup your own cython-driven packages!