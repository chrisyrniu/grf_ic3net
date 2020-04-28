#!/bin/bash

python -u test.py \
  --env_name grf \
  --nagents 3 \
  --nprocesses 1 \
  --num_epochs 200 \
  --hid_size 256 \
  --detach_gap 10 \
  --lrate 0.001 \
  --max_steps 100 \
  --ic3net \
  --recurrent \
  --scenario academy_3_vs_1_with_keeper \
  --num_controlled_lagents 3 \
  --num_controlled_ragents 0 \
  --reward_type scoring \
  --run_num 2 \
  --ep_num 270 \
  | tee test.log

#  --render \