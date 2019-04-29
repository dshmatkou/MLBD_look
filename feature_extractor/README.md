Adapted from [TF_FeatureExtraction](https://github.com/tomrunia/TF_FeatureExtraction)

This part is used for feature extraction from an image.

# Prepare Feature Extractor componets

```
./MLBD_look/setup.sh
```

Run this for downloading **checkpoints** (Resnet in our case, can be changed) and **tensorflow models**.

# Use Feature Extractor for data preparation

The tool can be used as a separate script for preparing data. Let's say you have a list of images, and you want to get a vector describing each image. 

Usage example:
```
python3 example_feat_extract.py 
--network resnet_v1_101 
--checkpoint ./checkpoints/resnet_v1_101_2016_08_28/resnet_v1_101.ckpt 
--image_path <path_to_image_folder> 
--layer_names resnet_v1_101/logits 
--num_classes 1000 
--out_file out.json
```

The tool can write the result into `json` file (if out_file has this extention), or to `HDF5` file (any other extention).
The tool is working with the directory with images as files. 

# Use Feature Extractor for raw image processing

As after upload, we are given a raw image bytes, the tool has the possibility to work with raw_image_bytes 

Usage example:
```
from feature_extractor.model import Model


path_to_checkpoint = <some_path>
model = Model(path_to_checkpoint)

with open('image_path.jpg', 'rb') as f:
    raw_image = f.read()
    features = model.extract_features(image_ar)
```
