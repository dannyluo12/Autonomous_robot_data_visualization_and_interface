import os
def run_viz(map_,stepsize,step_dir, out_dir, start_x,start_y,end_x,end_y):
    os.system("python ./src/generate_rrt_vis.py -start {} {} -stop {} {} -p {} -s {} -step_dir {} -out_dir {}".format(start_x,start_y,end_x,end_y,map_,stepsize,step_dir,out_dir))

