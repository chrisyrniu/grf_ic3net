#!/bin/bash

python -u main.py \
  --env_name grf \
  --nagents 3 \
  --nprocesses 8 \
  --num_epochs 200 \
  --hid_size 128 \
  --detach_gap 10 \
  --lrate 0.001 \
  --max_steps 100 \
  --commnet \
  --recurrent \
  --save \
  --save_every 10 \
  --scenario academy_3_vs_1_with_keeper \
  --num_controlled_lagents 3 \
  --num_controlled_ragents 0 \
  --reward_type checkpoints \
  | tee train.log

#  --render \
