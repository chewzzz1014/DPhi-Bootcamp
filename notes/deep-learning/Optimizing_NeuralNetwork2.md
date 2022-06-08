## Gradieny Descent
- `Gradient of loss function with respect ti weights in the network`.
- An efficient optimization algorithm that minimises cost function by attempting to find a local or global minima of a function.
- `Convergence` : A point in which Gradient Descent has reached and makes very small changes in cost funtion.

## Batch Gradient Descent
- All the training data is taken into consideration to take a single step. Take the average of the gradients of all the training examples and then use that mean gradient to update the parameters.
- `Great for relatively smooth error function curves`.
- Problem: Inefficient to calculate all gradients of large datasets. Batch Gradient Descent can be very slow.

## Stochastic Gradient Descent
- Randomize (shuffle) the whole training set. Then for updation of every parameter, use only one training example in every iteration to compute the gradient of cost function.
- Adv: 
    - Faster for large datasets.
    - Easier to fit into memory.
    - Large datasets can converge faster as it causes updates to the parameters more frequently.
- Problem : Lower accuracy.


## Mini-batch Gradient Descent
- Mixture of Gradient Descent and Stochastic Gradient Descent
- Use a batch of a fixed number of training examples which is less than the actual dataset and call it a `mini-batch`.
- Steps :
        1. Pick a mini-batch
        2. Feed the mini-batch to Neural Network
        3. Calculate the mean gradient of the mini-batch
        4. Use the mean gradient we calculated in step 3 to update the weights.
        5. Repeat steps 1–4 for the mini-batches we created.
- Adv: 
        - Able to update parameters more frequently 
        - Faster computations.
   
   
| Parameters | Batch Gradient Descent | Mini Batch GD | Stochastic GD |
|------------|------------------------|---------------|---------------|
|Accuracy|High|Moderate|Low|
|Time Consuming|High|Moderate|Low|

## Vanishing and Exploding Gradient
- Why use ReLu instead of Sigmoid and Softmax in hidden layers?
   - In case of sigmoid and tanh activation functions, if weights are large, then the gradient will be very (vanishingly) small, prevents the weights from changing their value. 
   - This is because the derivative of weights will increase very slightly or possibly get smaller and smaller every iteration.
   - By using RELU / Leaky RELU (a variation of ReLU Activation Function) as the activation function, it's relatively robust to the vanishing/exploding gradient issue (especially for shallow networks).
   - Leaky ReLUs will never have 0 gradient. They never die and training continues.
        
## Random Initialization

## Weight Initialization
- While initializing the training of neural networks, parameters (typically the weights) are initialized in a number of diﬀerent ways:
   - Constant Values, eg, 0 and 1
   - Values sampled from some distribution, typically a uniform distribution or normal distribution
   - Other sophisticated schemes like Xavier Initialization

- Importance :
   - Determine how quickly the network converges or whether it converges at all.
   - Their distribution aﬀects the gradients and, therefore, the eﬀectiveness of training.
   - Prevent layer activation outputs from exploding or vanishing during the forward propagation of a deep neural network.

- `Symmetry breaking`: All neurons learn the exact same thing.

- Weight Initialization Techniques:
   - Zero Initialization:
      - All the weights to be zero. All the the neurons of all the layers performs the same calculation, giving the same output.
      - Complexity of the whole neural network is same as that of a single neuron and the predictions would be nothing better than random.
      - Weights can be initialised to 1 too. That does perform better than initializing them to 0 but is still not able to break symmetry and perform well.
   - Random Initialization:
      - Weights are initialized very close to zero, but randomly. This helps in breaking symmetry and every neuron is no longer performing the same computation.
      - Random Initialization in deep neural netwrok may lead to vanishing gradients or exploding gradients.
   - Uniform Initialization
   - He init Initialization
   - Xavier Initialization
   - Kaiming Initialization

- Weight shoul be `small, diffrent from each other and have good variance`.
