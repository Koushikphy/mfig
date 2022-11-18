## `mfig`: A tool for merging multiple figures into one


1. __Installation__  
Download and install the package from the latest [release section](https://github.com/Koushikphy/mfig/releases/latest) or directly install it using 
```
pip install https://github.com/Koushikphy/mfig/releases/download/0.2.0/mfig-0.2.0.tar.gz
```

1. __Usage__  
Run the installed `mfig` utility to use this tool. Description of different arguments, can also be checked with `mfig -h` option.


| Argument    |  Description|
| ----------- | ----------- 
|    `-i`     | List of input figures |
|    `-o`     | Output file name  | 
|    `-it`    | Position of the subfigure index, possible values are: <br> `i` (inner), <br>`b` (bottom), <br>`t` (top-right corner),<br> `n` (no index) |
|    `-ir`    | Number of figures in one row |
|    `-w`     | Width of each figures. |
|    `-v`     | Verticle space between each rows |
|    `-s`     | Shift as x,y coordinate in position <br> for inner index type option |
