import sys
import json
import os

sys.path.insert(0, 'src')

from generate_rrt_vis import *

# TODO 
# create run.py script to output results of project (make re-creatable)
points_cfg = json.load(open('config/rrt_vis_points.json'))
mapping_cfg = json.load(open('config/rrt_vis_mapping.json'))


def main(targets):
    #TODO
    if 'test' in targets: 
        ros_csv_data = points_func(**data_cfg)
        csv_data_plots = mapping_data(**test_plots_cfg)
        # python generate_rrt_vis.py -start 100 150 -stop 350 350 -p test_track.png -s 20 # will have to try to run this
        print('')
 
if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)