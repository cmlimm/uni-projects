## matrixman ##
Python module written in C dedicated to working with matrixes

## Installation ##
Run following commands in your command line:

    git clone https://github.com/cmlimm/matrix_module.git
    cd matrix_module
    python setup.py install

## Using the module ##
|name         |args                  |example                           |result                      |
|:------------|:---------------------|:---------------------------------|:---------------------------|
|**fill**     |int, int, float       |fill(2, 2, 3.0)                   |[[3.0, 3.0], [3.0, 3.0]]    |
|**randfill** |int, int, float, float|randfill(2, 2, 0.0, 1.0)          |[[0.2, 0.1], [0.4, 0.5]]    |
|**identity** |int                   |identity(2)                       |[[1.0, 0.0], [0.0, 1.0]]    |
|**add**      |list, list            |add([1.0, 2.0], [1.0, 2.0])       |[2.0, 4.0]                  |
|**sub**      |list, list            |add([1.0, 2.0], [1.0, 2.0])       |[0.0, 0.0]                  |
|**transpose**|list                  |transpose([[1.0, 2.0],[3.0, 4.0]])|[[1.0, 2.0], [3.0, 4.0]]    |
|**mult**     |list, float           |mult([[1.0, 2.0],[3.0, 4.0]], 2.0)|[[2.0, 4.0], [6.0, 8.0]]    |
|**negative** |list                  |negative([[1.0, 2.0],[3.0, 4.0]]) |[[-1.0, -2.0], [-3.0, -4.0]]|
|**dot**      |list, list            |dot([[1.0, 2.0]],[[1.0],[2.0]])   |[[5.0]]                     |

## Uninstall module ##
Run following commands in your command line:

    python setup.py install --record files.txt
    xargs rm -rf < files.txt
