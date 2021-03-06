import os
import pandas as pd
import shutil

def run_viz(map_,stepsize,step_dir, out_dir, start_x,start_y,end_x,end_y):

    '''
    Creates data directory and run visualization code to be generated
    '''
    # first create the data directory
    directory = "data"
    parent_dir = "./"
    path = os.path.join(parent_dir, directory)
    
    #remove data dir if one already exists
    if (os.path.exists(path) and os.path.isdir(path)):
        shutil.rmtree(path)

    os.mkdir(path)
    
    # create a convenient hierarchical structure of folders inside /data
    directory1 = "viz_steps"
    directory2 = "viz_final"
    parent_dir = "./data/"
    data_link_1=os.path.join(parent_dir, directory1)
    data_link_2=os.path.join(parent_dir, directory2)
    os.mkdir(data_link_1)
    os.mkdir(data_link_2)
    
    os.system("python ./src/generate_rrt_vis.py -start {} {} -stop {} {} -p {} -s {} -step_dir {} -out_dir {}".format(start_x,start_y,end_x,end_y,map_,stepsize,step_dir,out_dir))

    return 

if __name__ == '__main__':
    main()