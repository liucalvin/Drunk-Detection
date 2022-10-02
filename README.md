# Fancy Drunk Detector Yeet Beans

Using facial recognition AI, we can detect drunkenness using a score based on drunk symptoms. Inherent facial traits that may swing "drunk" or "not drunk" will add or subtract to the "drunk score".

### Inspiration

Pushing one's limits while consuming alcohol is a serious issue. It can lead to health issues, mood issues, and the inhibition of good decision making. Often times "pushing the limits" is due to a person claiming that they do not feel the effects of alcohol and their friends saying that they do not "look drunk", despite the person actually being drunk.

### What it does

This is why we created Drunk Detector. Drunk Detector uses a picture of a person's face to determine if they are drunk or not. It considers many factors such as skin redness, dark circles, and smile to see if a person is feeling the effects of alcohol. The AI can also detect inherent facial features of different races that may make them "appear" more or less drunk, and take this into consideration when calculating the "drunk score".

### How we built it

We used the Face++ API for image recognition to gather various metrics from the inputted picture of a face and TensorFlow to train a binary classification model to determine whether or not the person depicted in the data is drunk.

### Challenges we ran into

Uploading images to the Face++ API was found to be difficult and we had a hard time training the TensorFlow model due to the fact that we have no machine learning experience.

### Accomplishments that we're proud of

One of our members had no coding experience at all going into this, we were able to work as a team and find ways for them to contribute without coding as well as introducing them to basic coding tasks that they could do.

### What we learned

We learned many different ways that drunkenness can appear on different people. The social aspect and eliminating of bias within our AI meant that we had to test our own biases and learn more about ourselves. We also learned a bunch about machine learning and APIs through practical experience using them for the first time on this project.

### What's next for Drunk Detector

Next, we want to implement it into cars to prevent people from starting them when they are feeling the effects of alcohol.
