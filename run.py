import sys
import json
import os

sys.path.insert(0, 'src')

from src.generate_rrt_vis import *
from src.util import run_viz

# TODO 
points_cfg_test = json.load(open('config/rrt_vis_points_test.json'))
points_cfg_all = json.load(open('config/rrt_vis_points_all.json'))
mapping_cfg_test = json.load(open('config/rrt_vis_mapping_test.json'))
mapping_cfg_all = json.load(open('config/rrt_vis_mapping_all.json'))



def main(targets):
    if 'test' in targets: 
        run_viz(**mapping_cfg_test,**points_cfg_test)
        print('Successfully ran RRT visualization on maze.png, optimal navigation path can be viewed {}'.format(mapping_cfg_test['out_dir']))
        
    if 'data' in targets:
        # TODO
        # getting_data = get_data(**data_cfg)
        pass
        # print('Data from project successfully pulled into ...')
        
    if 'plot' in targets:
    # TODO
        #gmapping_plot = plot_data(**gmapping_plots_cfg)
        #rtab_plot = plot_data(**rtab_plots_cfg)
        pass
        # print('... sucessfully plotted')
        
    if 'all' in targets:
        run_viz(**mapping_cfg_all,**points_cfg_all)
        print('Successfully ran RRT visualization on thunderhill_cropped.png, optimal navigation path can be viewed {}'.format(mapping_cfg_all['out_dir']))



if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)