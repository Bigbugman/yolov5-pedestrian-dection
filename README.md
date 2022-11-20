# Comp9444-project
### Object detection on self-automated cars

Autonomous driving is one of the popular applications of neural networks and deep learning. Pedestrian detection in real-time is one of the most important topics. It has to be applied carefully due to the issue of safety. Nowadays, although there are many methods, there is improvement.

Complex models that are two-layered such as r-cnn and its variants, require significant amounts of time to do pedestrian detection. Light frameworks that are one-layered like MobileNetV3 and the Yolo series can detect in real-time however, perform worse than the traditional two-layered models.


### Training dataset
The training data source we have used can be found [here](https://universe.roboflow.com/pionc/caltech-6f68o) for data augmented dataset and [here](https://universe.roboflow.com/visdronedataset/caltech-ped) for the original dataset.

### Training models
To replicate our training method of each model, please refer to the folder `train_models/Training_Procedure.ipynb`

We strongly suggest you to run the commands for training in Colab, because you may need to alter the paths in commands for excuting successfully. And we are 100% sure that our commands recorded in the notebook are runable in Colab. By the way, the commands for local machine are runable in our own devices as well. (Colab Link:https://colab.research.google.com/)

### Results
The results of each model can be found in `results/runs/<result_type>/<model_name>` and contains the result of our training outcome that our analysis is based on.

### References: 
Yolov5:
Pytorch.org. (2019). PyTorch documentation — PyTorch master documentation. [online] Available at: https://pytorch.org/docs/stable/index.html.

SPD attention mechanism:
Sunkara, R. and Luo, T. (n.d.). No More Strided Convolutions or Pooling: A New CNN Building Block for Low-Resolution Images and Small Objects. [online] Available at: https://arxiv.org/pdf/2208.03641v1.pdf [Accessed 19 Nov. 2022].

ECA attention mechanism:
Wang, Q., Wu, B., Zhu, P., Li, P., Zuo, W. and Hu, Q. (2020). ECA-Net: Efficient Channel Attention for Deep Convolutional Neural Networks. arXiv:1910.03151 [cs]. [online] Available at: https://arxiv.org/abs/1910.03151.

‌SE attention mechanism:
Hu, J. (n.d.). Squeeze-and-Excitation Networks. [online] Available at: https://arxiv.org/pdf/1709.01507.pdf.

‌MobileNet v3:
‌Howard, A., Sandler, M., Chu, G., Chen, L.-C., Chen, B., Tan, M., Wang, W., Zhu, Y., Pang, R., Vasudevan, V., Le, Q.V. and Adam, H. (2019). Searching for MobileNetV3. [online] arXiv.org. Available at: https://arxiv.org/abs/1905.02244.

‌

