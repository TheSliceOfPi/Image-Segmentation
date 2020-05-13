Edith Flores
Homework 4: 

Files Submitted:
seg.py
kmeans.py
cImage.py
Earth.gif
venus_fly_trap.gif
imgK.gif
Homework Cover Sheet ML-4.pdf
MLHW4.Report.pdf
readme.txt

--------seg.py-----------------
The program preprocess.py takes an image file and a number. Seg takes each pixel in the image file as a data sample and takes k as the number of means, and send them to the kmeans program to determine the k-mean clusters, and which their corresponding data samples. Seg creates a new image with the corresponding k mean clusters. The output is an image window with the original image and the new k-mean clustered image, the new image is then saved as imgK.gif.
To run: python3 seg.py <image filename> <number of k-means>


