## TensorBoard (Visualization Toolkit)
Some features that TensorBoard provides: 
  - Tracking and visualizing metrics such as loss and accuracy
  - Visualizing the model graph
  - Viewing histograms of weights, biases, or other tensors as they change over time
  - Displaying images, text, and audio data
    
## Train, Test and Validation Set
- `Train Set` : The sample of data used to fit (train) the model.
- `Test Dataset` : The sample of data used for the final evaluation of model’s performance.
- `Validation Dataset` : A portion of Train Set. The sample of data used to provide an evaluation of model’s performance while tuning model hyperparameters.

## Overfitting and Underfitting
- Overfitting :
  -  Model performs well on training data but performs poorly on data not seen during training. Model has memorized the training data instead of learning the relationships between features and labels.
  -  Strategies to reduce overfitting:
      1. Using fewer layers (shallow networks) and fewer neurons per layer (narrow networks).
      2. Use Dropouts
      3. User Regularisation
      4. Early Stoppping
- Underfitting : 
  - Model cannot capture the underlying trend of the data. Model neither getting a good accuracy in training data, nor in test/validation data.
  - Strategies to reduce underfitting:
      1. Increase the complexity of model
   

## Bias and Variance
- Bias :  Represents how unfair is something towards others
- Variance : Represents how likely something changes with respect to others

## Early Stopping, Regularization and Dropouts
1. Early Stopping
   - Every end of epoch, check and stop training if validation accuracy decrease steadily, while train acciracy increases.
2. Regularization
  - Technique which makes slight modifications to the learning algorithm such that the model generalizes better (Generalization refers to model's ability to adapt properly to new, previously unseen data). This in turn improves the model’s performance on the unseen data as well.
3. Dropouts
   -In Deep Neural Networks, the chances of overfitting are very high. Therefore, Dropout acts as a regularization to the NN. It makes the model more robust.
   - The percentage of neurons to be dropped is a hyperparameter that can be tuned based on the amount of overfitting on the data.
    - By dropping a unit out, we mean temporarily removing it from the network, along with all its incoming and outgoing connections.
    - It can be used with most types of layers, such as dense fully connected layers. Dropout may be implemented on any or all hidden layers in the network as well as the visible or input layer. 
