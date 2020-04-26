import matplotlib.pyplot as plt
import matplotlib.colors as colors

import numpy as np
import sys
import glob

colors_map = {
    'ic3net': '#dc8d6d',
    'commnet': '#5785c1',
    'maddpg': '#78b38a',
    'maac': '#ba71af'
}

def read_file(vec, file_name, scalar, term):
    print(file_name)
    with open(file_name, 'r') as f:
        lines = f.readlines()
        if len(lines) < 2:
            return vec

        mean_reward = False
        for idx, line in enumerate(lines):
            if term not in line:
                continue
            epoch_idx = idx
            epoch_line = line
            while 'Epoch' not in epoch_line:
                epoch_idx -= 1
                epoch_line = lines[epoch_idx]

            epoch = int(epoch_line.split(' ')[1].split('\t')[0])
            if not scalar:
                floats = line.split('\t')[1]
                left_bracket = floats.find('[')
                right_bracket = floats.find(']')
                floats = np.fromstring(floats[left_bracket + 1:right_bracket], dtype=float, sep=' ')

                if epoch > len(vec):
                    vec.append([floats.mean()])
                else:
                    vec[epoch - 1].append(floats.mean())
            else:
                floats = line.split('\t')[0]
                if epoch > len(vec):
                    vec.append([float(floats.split(' ')[-1].strip())])
                else:
                    vec[epoch - 1].append(float(floats.split(' ')[-1].strip()))

    return vec

def parse_plot(files, scalar=False, term='Epoch'):
    coll = dict()
    for fname in files:
        f = fname.split('.')
        if 'ic3net' in fname:
            label = 'ic3net'
        elif 'commnet' in fname:
            label = 'commnet'
        elif 'maac' in fname:
            label = 'maac'
        else:
            label = 'maddpg'

        if label not in coll:
            coll[label] = []

        coll[label] = read_file(coll[label], fname, scalar, term)

    for label in coll.keys():
        coll[label] = coll[label][:1000]

        mean_values = []
        max_values = []
        min_values = []

        for val in coll[label]:
            mean = sum(val) / len(val)

            if term == 'Success':
                mean *= 100
            mean_values.append(mean)
            variance = np.std(val)

            if term == 'Success':
                variance *= 100
            variance = variance if variance < 20 else 20
            max_values.append(mean + variance)
            min_values.append(mean - variance)

        plt.plot(np.arange(len(coll[label])), mean_values, linewidth=1.5, label=label, color=colors_map[label])
        plt.fill_between(np.arange(len(coll[label])), min_values, max_values, color=colors.to_rgba(colors_map[label], alpha=0.2))

    term = 'Rewards' if term == 'Epoch' else term

    plt.xlabel('Epochs')
    plt.ylabel(term)
    plt.legend()
    plt.grid()
    plt.title('GFootball {} {}'.format(sys.argv[2], term))

files = glob.glob(sys.argv[1] + "*")
files = list(filter(lambda x: x.find(".pt") == -1, files))

# 'Epoch'/ 'Steps-taken'
term = sys.argv[3]
scalar = False
if term != 'Epoch':
    scalar = True
parse_plot(files, scalar, term)
plt.show()
