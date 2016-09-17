Handwritting Recongnition on Digits using Canvas and Tensorflow

Using a simple MNIST trained model on Tensorflow for digit recognition. 
Based on this:
https://www.tensorflow.org/versions/master/tutorials/mnist/beginners/index.html

Uses HTML5 Canvas to draw the digit in canvasToGET.html

Click is used to toggle drawing on / off
Drawing area is 20 x 20 this is centered on a 28 x 28 canvas producing a white boarder
The white boarder is how the training set images have been prepared.
The pixels are extracted from the alpha channel and converted into JSON to be sent as a GET reqest.

On the backend the JSON is recieved by getToPredict.js running on node.js
Where it is saved as a txt file and predictDigit.py is executed

predictDigit.py reads the txt file, parses the JSON into an array.
It then loads the model created by saveModel.py
It runs the model on the array and print a prediction.