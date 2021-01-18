import sys
import json
import os

sys.path.insert(0, 'src')

from etl import get_data
from util import convert_notebook
from eda import eda_func
from plot import plot_data


def main(targets):

    # make sure to load up the config files
    data_cfg = json.load(open('config/data-params.json'))
    gmapping_cfg = json.load(open('config/gmapping-params.json'))
    rtab_cfg = json.load(open('config/rtab-params.json'))
    gmapping_plots_cfg = json.load(open('config/gmapping-plots-params.json'))
    rtab_plots_cfg = json.load(open('config/rtab-plots-params.json'))
    test_cfg = json.load(open('config/eda-params.json'))
    test_plots_cfg = json.load(open('config/plots-params.json'))
        
        
    if 'test' in targets: 
        ros_csv_data = eda_func(**test_cfg)
        csv_data_plots = plot_data(**test_plots_cfg)
        print('Data pipeline process of converting ".bag" file into ".csv" file completed for test target. The resulting data and plots can be seen in the "data/test/..." path.') 
     
    if 'data' in targets:
        getting_data = get_data(**data_cfg)
        print('Data from project successfully pulled intp /data/raw folder.')
        
    if 'eda' in targets:
        perform_eda = eda_func(gmapping_cfg)
        rtab_csv_data = eda_func(**rtab_cfg)
        print('Rosbag data successfully transformed into csv data and eda performed')
        
    if 'plot' in targets:
        gmapping_plot = plot_data(**gmapping_plots_cfg)
        rtab_plot = plot_data(**rtab_plots_cfg)
        print('Csv data generated from eda process now successfully plotted')
        
    if 'all' in targets:
        getting_data = get_data(**data_cfg)
        gmapping_csv_data = eda_func(**gmapping_cfg)
        rtab_csv_data = eda_func(**rtab_cfg)
        gmapping_plot = plot_data(**gmapping_plots_cfg)
        rtab_plot = plot_data(**rtab_plots_cfg)
        print('Data pipeline process of converting respective ".bag" file into ".csv" file completed. The resulting data and plots can be seen in the "data/post_eda/..." path.')  

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)