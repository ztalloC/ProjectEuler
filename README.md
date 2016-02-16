# Project Euler

[Project Euler](https://projecteuler.net/) is a website that offers
programming problems (typically math-related). The problems become
increasingly difficult and offers a challenge for all skill levels.

## History

I have been doing Project Euler for a few years on and off. My current
username is "Cosmic". The code in this repository are some of the solutions
to project euler questions. Most of my work has been in Python, but I have
written a few solutions in C/C++ and Java. Many of the earlier questions are
missing from this repository. Some of the code was lost while changing
computers and some of it was quick and low quality code and not worth
keeping.

Originally, I was not going to put this up on Github. This is because some
people will look up solutions to the questions and copy them (even though
it defeats the purpose of the site, which is learning). However, there are
many other sites with detailed solutions and explanations. Therefore, I
decided it would be better to share my existing code, rather than keep it to
myself.

As a compromise, I have renamed the "master" branch to "main". While this is
slightly unusual, according to [this stackoverflow answer](http://stackoverflow.com/a/15987482)
one can prevent branches from being indexed. This is because robots.txt allows
indexing for the "master" branch, but restricts other branches. In this manner,
I can share code with people who know my repository while making it harder for
people to cheat by searching on the internet.

## Usage

Most of the code can be ran standalone using python 2. Some problems need
data files, which need to be downloaded from the project euler site. These
problems have command line options for specifying the locations of the
input files (see the code for details).

The python code also uses [sympy](http://www.sympy.org/en/index.html) for
prime generation and factorization. In previous problems I wrote my own
prime-related code, but since it is so commonly used in problems, I decided
to replace my code with something faster. Not all of sympy is fast, so I
might change my code in the future.

## Other comments

The solution code in this repository has various levels of quality. All of
the code produces a solution, but some solutions finish instantly while
others can take up to a few minutes run. The project euler home page
specifies that all problems have solutions that take under a minute to run.
While ultimately one just needs a solution to finish a problem, some of the
code could be improved to be faster. Often I just start a problem by considering
how long a brute force solution would take and how much I can optimize it. For
earlier problems, this is sufficient, but later problems require intensive
thought and mathematical knowledge to solve.

![My progress](https://projecteuler.net/profile/Cosmic.png)
