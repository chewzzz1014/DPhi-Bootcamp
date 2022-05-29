## Goal of Scaling
- Most of ML Alogrithms use Eucledian distance between 2 points in computations. Dataset with highly varying features in terms of maginitude, units and range may face problem when buliding its ML Model.

## Ways to Scale Features
1. Standardisation
    - Replace the values by thier Z scores.
    - Redistribute the features with `mean = 0` and `std = 1`
    - Implementation using `sklearn.preprocessing.scale`
    - Can be used for algorithms that assumes zero centric data. E.g., Principal Component Analysis (PCA)

2. Mean Normalisation
    - This distribution will have values between -1 and 1, with mean = 0
    - Can be used for algorithms that assumes zero centric data. E.g., Principal Component Analysis (PCA)

3. Min-Max Scaling
  - Produces values of range [0,1]

4. Unit Vector
  - Scaling is done by considering the whole feature length to be the unit length.
  - Produces values of range [0,1]
