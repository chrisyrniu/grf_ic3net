# IC3Net and CommNet in Google Research Football
IC3Net and CommNet implementation in Google Research Football

## Requirements
* My [fork](https://github.com/chrisyrniu/football) version of Google Research Football
* PyTorch
* [visdom](https://github.com/facebookresearch/visdom)
* My grf wrapper:

`cd grf-envs`

`python setup.py develop`

## Run Training
`sh run_train.sh`

## Run Testing
`sh run_test.sh`

## Check Training Process and Results
* Use visdom
* Use plot_script.py and saved log file:

`python plot_script.py saved/ name Reward`

`python plot_script.py saved/ name Steps-Taken`

## Acknowledgement
This repository is revised from [IC3Net](https://github.com/IC3Net/IC3Net)



