Handwriting Recognition on Digits using Canvas and TensorFlow

Based on a simple softmax MNIST trained model on TensorFlow for digit recognition.    
https://www.tensorflow.org/versions/master/tutorials/mnist/beginners/index.html     
With a second layer added with ReLU and randomised starting weights.    
Performance is improved from 92% to 96% from only softmax.  

Uses HTML5 Canvas to draw the digit in canvasToGET.html

Click to draw, Double click to clear canvas.   
Drawing area is 20 x 20 this is centered on a 28 x 28 canvas producing a white boarder  
The white boarder is how the training set images have been prepared.    
The pixels are extracted from the alpha channel(rgba) and converted into JSON to be sent as a GET request.

On the backend the JSON is recieved by getToPredict.js running on node.js   
Where it is saved as a txt file and predictDigit.py is executed

predictDigit.py reads the txt file, parses the JSON into an array.  
It then loads the model created by saveModel.py     
It runs the model on the array and print a prediction.

Coded and tested on:    
https://ide.c9.io/en10/mnist9.io/en10/mnist     
https://preview.c9users.io/en10/mnist/canvasToGET.html

install TensorFlow see installTF.txt    
https://www.tensorflow.org/versions/master/get_started/os_setup.html#pip-installation