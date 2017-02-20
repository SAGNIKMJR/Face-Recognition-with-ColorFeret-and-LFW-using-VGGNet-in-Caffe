#!/usr/bin/env sh
# Create the imagenet lmdb inputs
# N.B. set the path to the imagenet train + val data dirs
set -e

EXAMPLE=/home/sagnik/Desktop/CS231N_Image_recognition_with_CNN/Downloaded_prototxt_and_models/VGG_S_CNN_fd8800eeb36e276cd6f9
#EXAMPLE=examples/imagenet
DATA=/home/sagnik/Desktop/CS231N_Image_recognition_with_CNN/Face_Image_Databases/vggnet
#DATA=data/ilsvrc12
TOOLS=/root/caffe/build/tools
#TOOLS=build/tools

TRAIN_DATA_ROOT=/home/sagnik/Desktop/CS231N_Image_recognition_with_CNN/Face_Image_Databases/vggnet/train/
VAL_DATA_ROOT=/home/sagnik/Desktop/CS231N_Image_recognition_with_CNN/Face_Image_Databases/vggnet/val/

# Set RESIZE=true to resize the images to 256x256. Leave as false if images have
# already been resized using another tool.
RESIZE=false
if $RESIZE; then
  RESIZE_HEIGHT=256
  RESIZE_WIDTH=256
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi

if [ ! -d "$TRAIN_DATA_ROOT" ]; then
  echo "Error: TRAIN_DATA_ROOT is not a path to a directory: $TRAIN_DATA_ROOT"
  echo "Set the TRAIN_DATA_ROOT variable in create_imagenet.sh to the path" \
       "where the ImageNet training data is stored."
  exit 1
fi

if [ ! -d "$VAL_DATA_ROOT" ]; then
  echo "Error: VAL_DATA_ROOT is not a path to a directory: $VAL_DATA_ROOT"
  echo "Set the VAL_DATA_ROOT variable in create_imagenet.sh to the path" \
       "where the ImageNet validation data is stored."
  exit 1
fi

echo "Creating train lmdb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $TRAIN_DATA_ROOT \
    $DATA/train1/train.txt \
    $EXAMPLE/ORL_train_lmdb

echo "Creating val lmdb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $VAL_DATA_ROOT \
    $DATA/val1/val.txt \
    $EXAMPLE/ORL_val_lmdb

echo "Done."
