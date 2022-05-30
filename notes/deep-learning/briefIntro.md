## CPU, GPU and TPU
- `CPU (Central Processing Unit)`: Processes computer instructions
- `GPU (Graphics Processing Unit) a.k.a graphics cards/video cards`: Render images, video, 2D and 3D animation. Performs quick math calculations and free up CPU to do other things.
-  `TPU (Tensor Processing Unit)`: Designated arhitecture for DL/ML computation. Only Tensorflow models can run on it. Outperforms CPU and GPU for various DL models in terms of prediction per second.
-  `GPU and CPU` will reduce computation time to efficiently train a DL model with large dataset.

## GPU Packages for DL
1. CUDA
    - NVDIA's language/API for programming on graphics card.
    - One of easiest ways to write high performance programs run on GPU.
    - Accelerate DL and compute-intensive apps.

2. cuDNN
   - NVIDIA CUDA Deep Neural Network library (cuDNN) 
   - GPU-accelerated library for deep neural networks
  
  
 ## Setting up Tensorflow on Google Colab
   - Provides 3 runtime types: `CPU, GPU and TPU`
   - `Runtime -> Change runtime type -> type command: !pip install tensorflow`
          
          import tensorflow as tf
          
          # display tensorflow version
          print(tf.__version__)
