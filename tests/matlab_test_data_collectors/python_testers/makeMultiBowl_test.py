from kwave.utils.mapgen import make_multi_bowl

from scipy.io import loadmat
import numpy as np
import os
from pathlib import Path



def test_makeMultiBowl():
    collected_values_folder = os.path.join(Path(__file__).parent, 'collectedValues/makeMultiBowl')
    num_collected_values = len(os.listdir(collected_values_folder))

    for i in range(num_collected_values):
        print(i)
        filepath = os.path.join(collected_values_folder, f'{i:06d}.mat')
        recorded_data = loadmat(filepath)

        params = recorded_data['params'][0]
        grid_size, bowl_pos, radius, diameter, focus_pos = params[:5]
        grid_size, radius, diameter = grid_size[0], radius[0], diameter[0]

        binary = bool(params[6])
        remove_overlap = bool(params[8])
        expected_multi_bowl = recorded_data['multiBowl']

        multi_bowl, _ = make_multi_bowl(grid_size, bowl_pos, radius, diameter, focus_pos, binary=binary, remove_overlap=remove_overlap)

        assert np.allclose(expected_multi_bowl, multi_bowl)

    print('make_multi_bowl(..) works as expected!')
