# classconvergence

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4732050.svg)](https://doi.org/10.5281/zenodo.4732050)

Plot the class distribution as a function of iteration from a Class2D or Class3D
job from RELION.

This tool was tested with star files produced by RELION-3.1.0. Earlier versions
of RELION are not supported.

## Acknowledgments

I would not have been able to put this tool together without the
[`starfile`](https://github.com/alisterburt/starfile) library.

## Installation

I recommend to install this tool in a dedicated conda environment. You can
create one like so (replace `ENV_NAME` with the name you want to give to this
environment):

```
$ conda deactivate
$ conda create --name ENV_NAME python=3.9
$ conda activate ENV_NAME
```

Once the conda environment is active, you can install the tool with the
following command:

```
$ pip install classconvergence
```

## Usage

```
$ classconvergence --help
Usage: classconvergence [OPTIONS] <job_directory>

  Plot the class distribution as a function of iteration from a Class2D or
  Class3D job from RELION.

Options:
  -c, --count        Plot particle counts per class (default, same effect as
                     not passing any option).

  -p, --percent      Plot percentages of particles per class (default:
                     counts).

  -o, --output TEXT  File name to save the plot (optional: with no file name,
                     simply display the plot on screen without saving it;
                     recommended file formats: .png, .pdf, .svg or any format
                     supported by matplotlib).

  -h, --help         Show this message and exit.
```
