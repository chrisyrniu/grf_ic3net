 #!/bin/bash

python -u main.py \
  --env_name grf \
  --nagents 3 \
  --nprocesses 4 \
  --num_epochs 1000 \
  --hid_size 128 \
  --detach_gap 10 \
  --lrate 0.0015 \
  --max_steps 100 \
  --ic3net \
  --recurrent \
  --save \
  --save_every 10 \
  --scenario academy_3_vs_1_with_keeper \
  --num_controlled_lagents 3 \
  --num_controlled_ragents 0 \
  --reward_type scoring \
  --plot \
  --plot_env ic3_scoring_1000_hid_128_adv_0 \
  | tee train.log

#  --render \
