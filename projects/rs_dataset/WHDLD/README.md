# EndoCV2020EDD

## Description

This project supports **`WHDLD`**, which can be downloaded from [here](https://sites.google.com/view/zhouwx/dataset#h.p_hQS2jYeaFpV0).

[1] Shao, Z.; Yang, K.; Zhou, W. Performance Evaluation of Single-Label and Multi-Label Remote Sensing Image Retrieval Using a Dense Labeling Dataset. Remote Sens. 2018, 10(6), 964.

[2] Shao, Z., Zhou, W., Deng, X., Zhang, M., & Cheng, Q. Multilabel Remote Sensing Image Retrieval Based on Fully Convolutional Network. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 2020, 13, 318-328. 

### Dataset Overview

WHDLD is a dense labeling dataset that can be used for multi-label tasks such as remote sensing image retrieval (RSIR)  and classification, and other pixel-based tasks like semantic segmentation (also called classification in remote sensing). We labeled the pixels of each image with the following 6 class labels, i.e., building, road, pavement, vegetation, bare soil and water.

### Visualization

![classes](https://cdn.jsdelivr.net/gh/hzz12138/typora_img/img/202304171742210.png)

## Usage

### Prerequisites

- Python v3.8
- PyTorch v1.10.0
- pillow (PIL) v9.3.0
- scikit-learn (sklearn) v1.2.0
- [MMCV](https://github.com/open-mmlab/mmcv) v2.0.0rc4
- [MMEngine](https://github.com/open-mmlab/mmengine) v0.2.0 or higher
- [MMSegmentation](https://github.com/open-mmlab/mmsegmentation) v1.0.0rc5


### Dataset Preparing

- Download dataset from [here](https://edd2020.grand-challenge.org/Data/) and save it to the `data/` directory .
- Decompress data to path `data/`. This will create a new folder named `data/EndoCV2020EDD/`, which contains the original image data.
- run script `python tools/prepare_dataset.py` to format data and change folder structure as below.
- run script `python ../../tools/split_seg_dataset.py` to split dataset. For the Bacteria_detection dataset, as there is no test or validation dataset, we sample 20% samples from the whole dataset as the validation dataset and 80% samples for training data and make two filename lists `train.txt` and `val.txt`. As we set the random seed as the hard code, we eliminated the randomness, the dataset split actually can be reproducible.

```none
  mmsegmentation
  ├── mmseg
  ├── projects
  │   ├── rs_dataset
  │   │   ├── WHDLD
  │   │   │   ├── configs
  │   │   │   ├── datasets
  │   │   │   ├── tools
  │   │   │   ├── data
  │   │   │   │   ├── train
  │   │   │   │   │   ├── images
  │   │   │   │   │   │   ├── xxx.jpg  
  │   │   │   │   │   │   ├── ...
  │   │   │   │   │   │   ├── xxx.jpg  
  │   │   │   │   │   ├── labels
  │   │   │   │   │   │   ├── xxx.png  
  │   │   │   │   │   │   ├── ...
  │   │   │   │   │   │   ├── xxx.png
  │   │   │   │   ├── val
  │   │   │   │   │   ├── images
  │   │   │   │   │   │   ├── xxx.jpg  
  │   │   │   │   │   │   ├── ...
  │   │   │   │   │   │   ├── xxx.jpg  
  │   │   │   │   │   ├── labels
  │   │   │   │   │   │   ├── xxx.png  
  │   │   │   │   │   │   ├── ...
  │   │   │   │   │   │   ├── xxx.png
```

### Training commands

Train models on a single server with one GPU.

```shell
mim train mmseg ./configs/${CONFIG_FILE}
```

### Testing commands

Test models on a single server with one GPU.

```shell
mim test mmseg ./configs/${CONFIG_FILE}  --checkpoint ${CHECKPOINT_PATH}
```

<!-- List the results as usually done in other model's README. [Example](https://github.com/open-mmlab/mmsegmentation/tree/dev-1.x/configs/fcn#results-and-models)
You should claim whether this is based on the pre-trained weights, which are converted from the official release; or it's a reproduced result obtained from retraining the model in this project. -->

## Results

### EndoCV2020EDD

***Note: The following experimental results are based on the data randomly partitioned according to the above method described in the dataset preparing section.***

|     Method      | Backbone | Crop Size |   lr   | mIoU  | mDice |                                       config                                       |         download         |
| :-------------: | :------: | :-------: | :----: | :---: | :---: | :--------------------------------------------------------------------------------: | :----------------------: |
| fcn_unet_s5-d16 |   unet   |  512x512  |  0.01  | 76.48 | 84.68 |  [config](./configs/fcn-unet-s5-d16_unet_1xb16-0.01-20k_EndoCV2020EDD-512x512.py)  | [model](<>) \| [log](<>) |
| fcn_unet_s5-d16 |   unet   |  512x512  | 0.001  | 61.06 | 63.69 | [config](./configs/fcn-unet-s5-d16_unet_1xb16-0.001-20k_EndoCV2020EDD-512x512.py)  | [model](<>) \| [log](<>) |
| fcn_unet_s5-d16 |   unet   |  512x512  | 0.0001 | 58.87 | 62.42 | [config](./configs/fcn-unet-s5-d16_unet_1xb16-0.0001-20k_EndoCV2020EDD-512x512.py) | [model](<>) \| [log](<>) |
