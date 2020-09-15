# Bachelor-Thesis-on-Image-Processing-and-Machine-Learning
My Bachelor Thesis had the title 'The estimation and improvement of an image's score of attractiveness'.

The practical part of my thesis consisted of some steps i had to follow in order to obtain a system which can predict and improve the score of attractiveness of an image.

The first step was to extract a subset of images from the AVA database - a large scale dataset for Aesthetic Visual Analysis - and i worked with 5 different subsets, of 1000, 5000, 15000 random images and another 2 subsets of approximately 800 and 10000 images with a constant distribution of their scores. 

The second step was to extract features from these images, namely the HSV histograms for distribution of colors,on 8 bins each, resulting in a 24-values vector, and the pyramidal contrast of the image, having in total a 25-values vector of features for each image.

The third step was to feed this data, with the labels denoting the attractiveness' score of the images, in a machine learning algorithm, namely a Random Forest Regressor.

After training the Regressor and testing it, i tried improving the results by updating the machine learning model, using bagging and random features techniques as well as GridSearch. 

For the improvement of the image's score i used CLAHE (Contrast Limited Adaptive Histogram Equalization) algorithm followed by a slight filtering.

The final step was to design a Graphical User Interface so as the algorithm functionality can be tested.

In the written part of my Bachelor Thesis i briefly explained the theory behind the image analyzing techniques i used, the Random Forest Regressor algorithm and the image processing techniques, followed by a thorough and detailed walk-through of the steps and the results i obtained with the different models on the different data subsets, using examples of tested images and graphs of the errors and the data features extracted, in the end drawing my conclusions on what i obtained and how this project can be used in different areas like real-estate, art contests, photography and other domains. 
