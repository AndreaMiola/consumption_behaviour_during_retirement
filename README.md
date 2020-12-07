Consumption Behaviour During Retirement
===========================================================

This is a tentative work to reproduce a paper of Haider And Stephen (2007) made by Andrea Miola.
I prepare this project for the course of "Programming and Practice for Economist" for the MSc in Economics at the University of Bonn.
I based my work on the Python Template for Reproducible Research Projects in Economics ([Gaudecker, 2020](https://econ-project-templates.readthedocs.io/en/stable/getting_started.html#)).



Getting started
----------------

## Table of Contents
- [Getting started](#getting-started)  
	- [Preparing your system](#preparing-your-system)
	- [Clone the repository](#clone-the-repository)  
	- [Create and activate conda environment](#create-and-activate-conda-environment)
	- [Pre-commit hooks](#pre-commit-hooks)
	- [Run the project with waf](#run-the-project-with-waf)
- [Documentation](#documentation)
- [Project idea](#project-idea)
- [Notes](#notes)
- [Main references](#main-references)


## [Getting started](#table-of-contents)

The contents of this section are totally inspired by the documentation that you can find at this [webpage](https://econ-project-templates.readthedocs.io/en/stable/getting_started.html#). If you want to have a full picture of how to prepare your project I suggest you to read it.

### [Preparing your system](#table-of-contents)
A series of programs are required for the project and they must be setup in your PATH:
(A full description is written [here](https://econ-project-templates.readthedocs.io/en/stable/getting_started.html#preparing-your-system))

* [Miniconda](http://conda.pydata.org/miniconda.html) or Anaconda
* A modern LaTeX distribution (e.g. [TeXLive](www.tug.org/texlive/), [MacTex](http://tug.org/mactex/), or [MikTex](http://miktex.org/))
* The text editor [Atom](https://atom.io/), unless you know what you are doing.
* Working on PowerShell for Windows user, or on terminal for Mac and Linux, is strongly recommended.


### [Clone the repository](#table-of-contents)

Clone the repository into a folder on your machine:


	$ cd /dest/dir && git clone https://github.com/AndreaMiola/consumption_behaviour_during_retirement.git


### [Create and activate conda environment](#table-of-contents)

If you want to use the conda environment:

On your terminal (of course in the path of the project) type:

	$ conda env create -f environment.yml.

If you need to update the environment, type: 
	
	
	$ conda env update consumption_behaviuor_during_retirment

To activate it, type:

	$ conda activate consumption_behaviuor_during_retirment


### [Pre-commit hooks](#table-of-contents)

Pre-commit have to be installed in order for them to have an effect if you want to implement any changes. 

	$ pre-commit install

And for run them

	$ pre-commit run

### [Run the project with waf](#table-of-contents)

I used waf.py to build the project. To configure it, type on your terminal:

	$ python waf.py configure

All programs used within this project template need to be found on your path.

If everything looks green and the last line of the output says 'configure' finished successfully you are good. So, type:

	$ python waf.py build

At this point, you may find all the outputs (tables, figure, documentation, research paper) in the bld folder.

If you need it, the command named distclean is provided to remove the build directory and the lock file created during the configuration.

	$ python waf.py distclean


## [Documentation](#table-of-contents)

For a better comprehension of the project and for its structure please read the documentation.

## [Notes](#notes)

- I had some problems to import module 'visualizing_data'. The description of this file is unfortunately not in the documentation.
- Waf highlights some warnings that I was not able to solve, but the build finishes successfully. 

## [Project idea](#table-of-contents)

Literature have found a decrease in consumption at the retirement period. The idea of this project is to use an European panel data (SHARE) to replicate the results of the Haider And Stephen (2007) paper. Implementing a fixed effect estimation on panel data I measured the effect on actual year of retirment and on the expected one. The results of this analysis, even though they are not significant, predict a decline in consumption both on the actual and on the expected period.



## [Main references](#table-of-contents)


Haider, S. J., & Stephens Jr, M. (2007). Is there a retirement-consumption puzzle? Evidence using subjective retirement expectations. The review of economics and statistics, 89(2), 247-264. [here](https://www.mitpressjournals.org/doi/abs/10.1162/rest.89.2.247)

Von Gaudecker, H.M. (2019). Templates for reproducible research projects in economics. [here](https://zenodo.org/record/2533241#.XlXDdy2ZMnE).
