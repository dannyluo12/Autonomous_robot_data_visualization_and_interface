import os 
import shutil
import bagpy
import rosbag
from bagpy import bagreader
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt

def plot_data(odom_data, standard_data, velocity_data, outdir):
    '''
    function to generate plots and save to outdirectory: "./data/test/data_plots"
    '''
    os.mkdir(outdir) # should create "./data/test/data_plots" folder path because data folder already created in func above
    velocity_df = pd.read_csv(velocity_data)
    odometry_df = pd.read_csv(odom_data)
    standard_df = pd.read_csv(standard_data)
    
    velocity_cleaned = velocity_df.drop(["Unnamed: 0"], axis=1)
    odometry_cleaned = odometry_df.drop(["Unnamed: 0"], axis=1)
    standard_cleaned = standard_df.drop(["Unnamed: 0"], axis=1)
    print('CSV data successfully cleaned')
    
    # velocity data plot
    plt.plot(velocity_cleaned['Time'], velocity_cleaned['linear.x'], color='black')
    plt.title('Linear Velocity Timeseries', fontsize=15)
    plt.xlabel('Time', fontsize=15)
    plt.ylabel('Linear Velocity', fontsize=15)
    plt.grid()
    plt.savefig(os.path.join(outdir, 'velocity_plt.png'))  
    print('Velocity plot succesfully added to path')
    
    # odometry data plot
    plt.plot(odometry_cleaned['Time'], odometry_cleaned['pose.x'], color='r', label='x position')
    plt.plot(odometry_cleaned['Time'], odometry_cleaned['pose.y'], color='g', label='y position')
    plt.plot(odometry_cleaned['Time'], odometry_cleaned['pose.z'], color='b', label='z position')
    plt.title('Position Odometry Timeseries', fontsize=15)
    plt.xlabel('Time', fontsize=15)
    plt.ylabel('Position Odometry', fontsize=15)
    plt.legend(fontsize=13)
    plt.grid()
    plt.savefig(os.path.join(outdir, 'odometry_plt.png')) 
    #second odom plot
    plt.plot(odometry_cleaned['Time'], odometry_cleaned['orientation.x'], color='r', label='x orientation')
    plt.plot(odometry_cleaned['Time'], odometry_cleaned['orientation.y'], color='g', label='y orientation')
    plt.plot(odometry_cleaned['Time'], odometry_cleaned['orientation.z'], color='b', label='z orientation')
    plt.title('Orientation (Directional) Odometry Timeseries', fontsize=15)
    plt.xlabel('Time', fontsize=15)
    plt.ylabel('Orientation (Direction) Odometry', fontsize=15)
    plt.legend(fontsize=13)
    plt.grid()
    plt.savefig(os.path.join(outdir, 'odometry_plt_2.png')) 
    print('Odometry plot succesfully added to path')
    
    # standard data plot
    plt.plot(standard_cleaned['Time'], standard_cleaned['data'], color='navy')
    plt.title('Standard Data Timeseries', fontsize=15)
    plt.xlabel('Time', fontsize=15)
    plt.ylabel('Standard Data', fontsize=15)
    plt.grid()
    plt.savefig(os.path.join(outdir, 'standard_plt.png')) 
    print('Standard plot succesfully added to path')   
    
    

if __name__ == '__main__':
    main()