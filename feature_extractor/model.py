from feature_extractor.feature_extractor.raw_feature_extractor import FeatureExtractor
from feature_extractor.example_feat_extract import raw_feature_extraction_queue


class Model(object):
    def __init__(self, path_to_checkpoint):
        """
        path_to_checkpoint: path to pre-trained checkpoint file
        """
        self.path_to_checkpoint = path_to_checkpoint
        self.network_name = 'resnet_v1_101'
        self.batch_size = 1

        # size of vector
        self.num_classes = 1000
        self.preproc_func = None
        self.num_preproc_threads = 2
        self.layer_names = ["resnet_v1_101/logits"]

        # Initialize the feature extractor
        self.feature_extractor = FeatureExtractor(
            network_name=self.network_name,
            checkpoint_path=self.path_to_checkpoint,
            batch_size=self.batch_size,
            num_classes=self.num_classes,
            preproc_func_name=self.preproc_func,
            preproc_threads=self.num_preproc_threads
        )

    def extract_features(self, image_as_matrix):
        # Feature extraction example using a filename queue to feed images
        feature_dataset = raw_feature_extraction_queue(
            self.feature_extractor, image_as_matrix, self.layer_names,
            self.batch_size, self.num_classes
        )

        layer_name = self.layer_names[0]

        return list(feature_dataset[layer_name][0][0][0])


if __name__ == "__main__":
    model = Model('./feature_extractor/checkpoints/resnet_v1_101.ckpt')

    image_str = None
    with open('./feature_extractor/data/rider-1.jpg', 'rb') as f:
        image_str = f.read()

    model.extract_features(image_str)
