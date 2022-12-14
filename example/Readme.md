
## `mfig` Examples:

- [Tabel of Contents](#mfig-examples)
    - [2 images with index inside](#2-images-with-index-inside)
    - [2 images with index inside with a shift](#2-images-with-index-inside-with-a-shift)
    - [4 images in 2x2 grid with index inside](#4-images-in-2x2-grid-with-index-inside)
    - [4 images in 2x2 grid with index at top left corner](#4-images-in-2x2-grid-with-index-at-top-left-corner)
    - [4 images in 2x2 grid with index at top left corner with spacing inbetween rows](#4-images-in-2x2-grid-with-index-at-top-left-corner-with-spacing-inbetween-rows)
    - [4 images in 2x2 grid with index at bottom](#4-images-in-2x2-grid-with-index-at-bottom)
    - [4 images in 2x2 grid with no index](#4-images-in-2x2-grid-with-no-index)
    - [6 images in 2x3 grid with index at top left corner](#6-images-in-2x3-grid-with-index-at-top-left-corner)
    - [6 images in 2x3 grid with index at bottom](#6-images-in-2x3-grid-with-index-at-bottom)



#### 2 images with index inside
```bash
mfig -i image.pdf image.pdf -o out.pdf -v 0 -it i
```
![Alt text](images/out1-1.jpg)
&nbsp;

#### 2 images with index inside with a shift
```bash
mfig -i image.pdf image.pdf -o out.pdf -v 0 -it i -s -0.3 0.3
```
![Alt text](images/out2-1.jpg)
&nbsp;


#### 4 images in 2x2 grid with index inside
```bash
mfig -i image.pdf image.pdf image.pdf image.pdf -o out.pdf -v 0 -it i
```
![Alt text](images/out3-1.jpg)
&nbsp;


#### 4 images in 2x2 grid with index at top left corner
```bash
mfig -i image.pdf image.pdf image.pdf image.pdf -o out.pdf -v 0 -it t
```
![Alt text](images/out4-1.jpg)
&nbsp;


#### 4 images in 2x2 grid with index at top left corner with spacing inbetween rows
```bash
mfig -i image.pdf image.pdf image.pdf image.pdf -o out.pdf -v 1 -it t
```
![Alt text](images/out10-1.jpg)
&nbsp;


#### 4 images in 2x2 grid with index at bottom
```bash
mfig -i image.pdf image.pdf image.pdf image.pdf -o out.pdf -v 0 -it b
```
![Alt text](images/out5-1.jpg)
&nbsp;


#### 4 images in 2x2 grid with no index
```bash
mfig -i image.pdf image.pdf image.pdf image.pdf -o out.pdf -v 0 -it n
```
![Alt text](images/out6-1.jpg)

&nbsp;

#### 6 images in 2x3 grid with index at top left corner
```bash
mfig -i image.pdf image.pdf image.pdf image.pdf image.pdf image.pdf -o out.pdf -pr 3 -w 0.27 -v 0 -it t -v 1
```
![Alt text](images/out7-1.jpg)
&nbsp;


#### 6 images in 2x3 grid with index at bottom

```bash
mfig -i image.pdf image.pdf image.pdf image.pdf image.pdf image.pdf -o out.pdf -pr 3 -w 0.32 -v 0 -it b
```
![Alt text](images/out8-1.jpg)
&nbsp;