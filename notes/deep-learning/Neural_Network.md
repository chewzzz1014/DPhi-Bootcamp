## Neural Network
- Complex structures made of artificial neurons that can take in multiple inputs to produce a single output.
- Consists of an input and output layer, with >= 1 hidden layers.
- `Input Layer`: Inputs are measure of dataset's features. Eg, dataset with 13 input features has 13 neurons at input layer.
- `Hidden Layer`: Number of neurons are assigned by us. We could find the optimal number of neurons in hidden layer through hyperparameter tuning.
- `Output Layer`: Produce the output
- `Weight`: The scalar multiplication. Assigned randomly for each connection, and updated as per their importance in predicting the output. `Back Propagation` updates the weight.

## Working of Neural Network
1. Forward Propagation : 
    - Feed on input data and generate output.
2. Gradient Descent :
    - Minimise loss/cost function and improve the performance of model. 
    - `Descent` mean moving downwards
    - Steps:
        1. Initially,  parameter values of the hypothesis are randomly initialized.
        2. Gradient Descent iteratively (one step at a time) adjusts the parameters and gradually finds the best values for them by minimizing the cost 
3. Backward Propagation : Errors are generated in forward propagation. To reduce these errors, traverse back from output layer to input layer and update the initially assigned weight.

## Clasification
- `Logistic Regression` is one of the techniques used for classification.
- `Linear Regression` is used to solve regression problems with continuous values
- Transformation from Linear Regression to Logistic Regression requires `Sigmoid function` that takes in any real value, and return an output probability between 0 and 1.

## Activation Function
1. An artificial neuron takes the inputs and their respective weights
2. It applies dot products between input values & its weights and sums them up.
3. It applies activation function on the summation and fires the output   


        Output = Activation ( Sum(Input * Weight + Bias ) )
        
- Determine whether a neuron should be activated(fired) or not, based on whether each neuron’s input is relevant for the model’s prediction.
- Introduce non-linearity into the output of a neuron.
- Types: `Sigmoid Function, ReLu, tanH, Leaky ReLU, Softmax Function`.

## Layers
- Dense Layer : Middle layer where which neurons receives input from all the neurons in the previous layer.
- Creating Model Using Layer API:
   - `Sequential Model` : Linear Stack of Layer. Build model layer by layer, and each layer has weights that correspond to the layer that follows it.
   - `Functional Model` : Graphs of Layers.

## Error/Loss Functions
- `Error` : Difference between actual output and predicted output
- `Loss Function` : Function that computes error

# Optimization Function
- `Optimization Function` : Function that modifies weights in backward propagation to minimize the error.
- Examples : Adam, RMSProp, SGD
