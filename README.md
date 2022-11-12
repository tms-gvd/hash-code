# hash-code
Joint work of ZHANG and GAVIARD for [Hash-Code](https://storage.googleapis.com/coding-competitions.appspot.com/HC/2021/world_finals_2021.pdf)  
![coverage badge](./coverage.svg)

The docs site is live at https://tms-gvd.github.io/hash-code/

The purpose of this project is to train us to master the quality of software development, beyond of providing an exact solution.

The project is built into three main sections:

1. The [docs] section contains the documentation for the project code.
2. The [src] section contains the problem solving code.
3. The [tests] section contains all the unit tests.

Poetry is adopted in this project. Our entire project architecture and package versions are managed using Poetry. And we also put the documentation for the project code on a web by Sphinx and will be updated automatically by GitHub Actions scripts.

The problem to be solved is described in detail at this [File](https://storage.googleapis.com/coding-competitions.appspot.com/HC/2021/world_finals_2021.pdf).

The input of this problem is a text file, its format is like this:

<img src="https://p0.meituan.net/dpplatform/497ccc757e89ef2203a8c741fcb4bfda137023.png" alt="inputFormatExample" style="zoom: 40%;" />

The output of this problem is also a text file, its format is like this:

<img src="https://p0.meituan.net/dpplatform/3f0f2220d1bf297cad3da1dc38214b2786729.png" alt="outputformatExample" style="zoom: 40%;" />

The goal of the solution is to assign work to engineers to implement features that will benefit as many users as possible. And to be able to complete the development of all FEATURES within a specific deadline.

------------------------

In order to complete this project, our organizational division of labor is this.

- GAVIARD

  > 1. The [src] section.
  > 2. The [tests] section.

- ZHANG
  >1. The [docs] section.
  >2. GitHub Action scripts and this Readme.md.
