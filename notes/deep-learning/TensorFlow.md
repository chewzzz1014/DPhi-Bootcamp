## Tensorflow
- Deep Learning library/framework open-sourced by Google.
- TensorFlow Lite: Lightweight library for deploying models on mobile and embedded devices
- TensorFlow Extended: End-to-end platform for preparing data, training, validating, deploying models in large production environments.

## Keras
- Deep Learning API (tool that enables data exchange among 2 applications) written in Python
- Runs on TensorFlow
- Goal: Enable fast experimentation

## tf.Keras
- Tensorflow specific implementation of Keras

## Tensor
- Primary data structures used by neural networks (the building blocks of Deep Learning)
- Perform neural networkds transformation, input and output
- Tensors are `Multi-dimensional arrays with an uniform type (dtype)`.
- Tensors are immutable. Cant'be updated and can only create new tensor.
- Rank of tensor based on dimension:
    - Rank 0 tensor : Scalar
    - Rank 1 tensor : Vector
    - Rank 2 tensor : Matrix
    - Rank >2 : Tensor

## Tensor ( Name, Shape, Data Type)
        Tensor ( "Const: 0", shape=(), dtype=string)
        
## Tensor - Rank, Axes and Shape
 - Rank, axes, shape are tensor attributes
 1. `Rank`:  
     - Number od dimensions present within the tensor.
     - Rank-2 tensor indicates we have a matrix/2d-array/2d-tensor
     - Number of dimension = Number of indices needed to refer to an element. E.g., a[2] (Rank 1 tensor) for list and a[2][3] (Rank 2 tensor) for 2-dimensional list.
     
2. `Axes`:
     - Specific dimension of a tensor. Rank 2 tensor has 2 axes.
     - Element exists/runs along axes
     - Length of axes indicate how many indices are available along the axes. Eg, for axis with a length of 3, and we have a tensor called t, `t[0], t[1], t[2]` is available.

3. `Shape`:
     - Determined by length of each axis
     - How many indices are available along axes


Source: https://deeplizard.com/learn/video/AiyK0idr4uM 
        
