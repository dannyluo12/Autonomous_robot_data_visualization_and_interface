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
        get_coords = points_func(**points_cfg)
        get_track = mapping_data(**mapping_cfg)
        # python generate_rrt_vis.py -start 100 150 -stop 350 350 -p test_track.png -s 20 # will have to try to run this
        print('')
        
    if 'data' in targets:
        #getting_data = get_data(**data_cfg)
        print('Data from project successfully pulled into ...')
        
    # this target might not be necessary
    #if 'eda' in targets:
    #    perform_eda = eda_func(gmapping_cfg)
    #    rtab_csv_data = eda_func(**rtab_cfg)
    #    print('Rosbag data successfully transformed into csv data and eda performed')
        
    if 'plot' in targets:
        #gmapping_plot = plot_data(**gmapping_plots_cfg)
        #rtab_plot = plot_data(**rtab_plots_cfg)
        print('... sucessfully plotted')
        
    if 'all' in targets:
        #getting_data = get_data(**data_cfg)
        #gmapping_csv_data = eda_func(**gmapping_cfg)
        #rtab_csv_data = eda_func(**rtab_cfg)
        #gmapping_plot = plot_data(**gmapping_plots_cfg)
        #rtab_plot = plot_data(**rtab_plots_cfg)
        print('Data pipeline process of ... is successfull')
 
if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)