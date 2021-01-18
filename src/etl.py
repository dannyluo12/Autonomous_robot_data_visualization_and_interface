import os 
import pandas as pd
import shutil

def get_data(indir_origin_bag, indir_gmapping_bag, indir_rtab_bag, outdir_origin_bag, outdir_gmapping_bag, outdir_rtab_bag):

    '''
    Reads the data by creating a symlink between the 
    location of the downloaded data and /data
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
    directory1 = "raw"
    parent_dir = "./data/"
    data_link=os.path.join(parent_dir, directory1)
    os.mkdir(data_link)


    # create the symlink
#     os.symlink(data_link, indir)
    os.symlink(indir_origin_bag, outdir_origin_bag)
    os.symlink(indir_gmapping_bag, outdir_gmapping_bag)
    os.symlink(indir_rtab_bag, outdir_rtab_bag)

    return 


if __name__ == '__main__':
    main()