# tenpinbowling

[![license: MIT](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/avramidis/sodecl/blob/master/LICENSE)
<!-- [![Build Status](https://travis-ci.org/avramidis/sodecl.svg?branch=master)](https://travis-ci.org/avramidis/sodecl) -->

tenpinbowling is a Python package that can be used to calculate the score of a 10 pin bowling game. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To get the code you will need git. To install git on Ubuntu use the following commands in a terminal

```
sudo apt update
sudo apt install git
```

To pull the repository from github use the following command in a terminal

```
git clone https://github.com/avramidis/tenpinbowling.git
```

You will need Python version 3, to install it use the following command in a terminal

```
sudo apt install python3
```

### Installing

To install tenpinbowling package use the following command in a terminal

```
python3 setup.py install
```

### Example

An example code that uses tenpinbowling is the following

```python
import tenpinbowling.score
frames = [[4, 3], [5, 4], [4, 4]]
score = tenpinbowling.score.getScore(frames)
```

If the run was successful the output will be 24.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* This readme file is based on the template found at https://gist.github.com/PurpleBooth/109311bb0361f32d87a2
