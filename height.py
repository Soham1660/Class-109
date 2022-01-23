import pandas as pd
import statistics
import csv
df=pd.read_csv("height.csv")
height=df["Height(Inches)"].tolist()
weight=df["Weight(Pounds)"].tolist()
height_mean=statistics.mean(height)
weight_mean=statistics.mean(weight)
height_median=statistics.median(height)
weight_median=statistics.median(weight)
height_mode=statistics.mode(height)
weight_mode=statistics.mode(weight)
print("mean,median,mode  is {},{}and{}".format(height_mean,height_median,height_mode))
print("mean,median,mode  is {},{}and{}".format(weight_mean,weight_median,weight_mode))
height_stdev=statistics.stdev(height)
weight_stdev=statistics.stdev(weight)
height_first_stdev_start,height_first_stdev_end=height_mean-height_stdev,height_mean + height_stdev
height_second_stdev_start,height_second_stdev_end=height_mean-(2*height_stdev),height_mean + (2*height_stdev)
height_third_stdev_start,height_third_stdev_end=height_mean-(3*height_stdev),height_mean + (3*height_stdev)
weight_first_stdev_start,weight_first_stdev_end=weight_mean-weight_stdev,weight_mean + weight_stdev
weight_second_stdev_start,weight_second_stdev_end=weight_mean-(2*weight_stdev),weight_mean + (2*weight_stdev)
weight_third_stdev_start,weight_third_stdev_end=weight_mean-(3*weight_stdev),weight_mean + (3*weight_stdev)
height_data1=[result for result in  height if result > height_first_stdev_start and result <height_first_stdev_end]
height_data2=[result for result in  height if result > height_second_stdev_start and result <height_second_stdev_end]
height_data3=[result for result in  height if result > height_third_stdev_start and result <height_third_stdev_end]
weight_data1=[result for result in  weight if result > weight_first_stdev_start and result <weight_first_stdev_end]
weight_data2=[result for result in  weight if result > weight_second_stdev_start and result <weight_second_stdev_end]
weight_data3=[result for result in  weight if result > weight_third_stdev_start and result <weight_third_stdev_end]
print("{}%ofdata for height in 1 stdev".format(len(height_data1)*100.0/len(height)))
print("{}%ofdata for height in 2 stdev".format(len(height_data2)*100.0/len(height)))
print("{}%ofdata for height in 3 stdev".format(len(height_data3)*100.0/len(height)))
print("{}%ofdata for weight in 1 stdev".format(len(weight_data1)*100.0/len(weight)))
print("{}%ofdata for weight in 2 stdev".format(len(weight_data2)*100.0/len(weight)))
print("{}%ofdata for weight in 3 stdev".format(len(weight_data3)*100.0/len(weight)))