#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=/home/siddharth/caffe_trial_db
DATA=/home/siddharth/caffe_trial_db
TOOLS=/home/siddharth/caffe/build/tools

$TOOLS/compute_image_mean $EXAMPLE/colfer_train_lmdb \
  $DATA/colfer_mean.binaryproto

echo "Done."
