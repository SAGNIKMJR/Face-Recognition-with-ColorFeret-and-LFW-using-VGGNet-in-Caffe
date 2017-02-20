#!/usr/bin/env sh
set -e

/home/abc-5/caffe/build/tools/caffe train \
    --solver=/home/abc-5/Desktop/DOP17_SK_SM/Run1_20_2/solver_vggnet.prototxt --gpu=0 --weights=/home/abc-5/Desktop/DOP17_SK_SM/Run1_20_2/VGG_ILSVRC_19_layers.caffemodel $@

