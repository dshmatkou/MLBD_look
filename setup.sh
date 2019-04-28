# setup feature_extractor

echo "Cloning Models ... "
cd feature_extractor
git clone https://github.com/tensorflow/models/

echo "Cloning checkpoints ... "
mkdir checkpoints
cd checkpoints
wget http://download.tensorflow.org/models/resnet_v1_101_2016_08_28.tar.gz
tar -xzf resnet_v1_101_2016_08_28.tar.gz
cd ..


