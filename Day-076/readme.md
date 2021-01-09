# Computation with NumPy and N Dimensional Arrays
## Day 76 - Advanced - \#100DaysOfCode

**To do:**
* Learn how to use NumPy to work with numerical data. 

**Requirements:**
* Use [`.arange()`](https://numpy.org/devdocs/reference/generated/numpy.arange.html) to create a vector `a` with 
  values ranging from 10 to 29. 
  
* Use Python slicing techniques on `a` to:
    * Create an array containing only the last 3 values of `a`
    * Create a subset with only the 4th, 5th, and 6th values
    * Create a subset of `a` containing all the values except for the first 12 (i.e., `[22, 23, 24, 25, 26, 27, 28, 29]`)
    * Create a subset that only contains the even numbers (i.e, every second number)

* Reverse the order of the values in `a`, so that the first element comes last

* Print out all the indices of the non-zero elements in this array: [6,0,9,0,0,5,0]

* Use NumPy to generate a 3x3x3 array with random numbers

* Use [`.linspace()`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) to create a vector `x` 
  of size 9 with values spaced out evenly between 0 to 100 (both included).

* Use [`.linspace()`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) to create another vector 
  `y` of size 9 with values between -3 to 3 (both included). Then plot `x` and `y` on a line chart using Matplotlib.

* Use NumPy to generate an array called `noise` with shape 128x128x3 that has random values. Then use Matplotlib's 
  [`.imshow()`](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.imshow.html) to display the array as an 
  image.

* Convert the image to black and white. The values in our `img` range from 0 to 255. 

* Manipulate the images by doing some operations on the underlying ndarrays. See if you can change the values in the 
  ndarray so that:
    1) You flip the grayscale image upside down
    
    2) Rotate the colour image
    
    3) Invert (i.e., solarize) the colour image. To do this you need to converting all the pixels to their "opposite" 
       value, so black (0) becomes white (255).
       
**Screenshots:**

![]()

![]()
