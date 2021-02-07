import sys
import json
import os

sys.path.insert(0, 'src')

from src.generate_rrt_vis import *
from src.util import run_viz

# TODO 
# create run.py script to output results of project (make re-creatable)
points_cfg = json.load(open('config/rrt_vis_points.json'))
mapping_cfg = json.load(open('config/rrt_vis_mapping.json'))


def main(targets):
    #TODO
    if 'test' in targets: 
        run_viz(**mapping_cfg,**points_cfg)
        print('Successfully ran RRT visualization on maze.png, optimal navigation path can be viewed {}'.format(mapping_cfg['out_dir']))
        
    if 'data' in targets:
        # TODO
        # getting_data = get_data(**data_cfg)
        pass
        # print('Data from project successfully pulled into ...')
        
    # this target might not be necessary
    if 'eda' in targets:
    # TODO
    #    perform_eda = eda_func(gmapping_cfg)
    #    rtab_csv_data = eda_func(**rtab_cfg)
       pass
       # print('Rosbag data successfully transformed into csv data and eda performed')
        
    if 'plot' in targets:
    # TODO
        #gmapping_plot = plot_data(**gmapping_plots_cfg)
        #rtab_plot = plot_data(**rtab_plots_cfg)
        pass
        # print('... sucessfully plotted')
        
    if 'all' in targets:
    # TODO
        #getting_data = get_data(**data_cfg)
        #gmapping_csv_data = eda_func(**gmapping_cfg)
        #rtab_csv_data = eda_func(**rtab_cfg)
        #gmapping_plot = plot_data(**gmapping_plots_cfg)
        #rtab_plot = plot_data(**rtab_plots_cfg)
        pass
        # print('Data pipeline process of ... is successfull')
        
        
        
        
if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)