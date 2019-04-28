![Alt text](onion.jpg?raw=true "Look")


# Usage
1. ``git clone https://github.com/ShmatkovD/MLBD_look.git``
2. ``cd MLBD_look``
3. ``apt install python3 python3-pip python3-dev cython3``
4. ``pip3 install .``
5. ``python3 manage.py runserver``
6. ``curl http://127.0.0.1:8000/endpoint/?x=2&y=4``

# Model usage
7. Copy data into ``./feature_extractor/data/`` 
8. ``git clone https://github.com/tensorflow/models/`` into the folder `./feature_extractor/models`.
9. ``python3 example_feat_extract.py --network resnet_v1_101 --checkpoint ./checkpoints/resnet_v1_101_2016_08_28/resnet_v1_101.ckpt --image_path ./data/ --layer_names resnet_v1_101/logits --num_classes 1000`` with `cwd=feature_extractor`.
10. Out log file is `./feature_extractor/features.h5`
 

# Feature Extractor Usage
1. Models will be taken from https://github.com/tensorflow/models/
2. Put models into feature_extractor/models
3. Checkpoints from http://download.tensorflow.org/models/resnet_v1_101_2016_08_28.tar.gz
4. Unpack into feature_extractor/checkpoints
