import statistics
import pandas as pd
import random
import plotly.figure_factory as ff

data = pd.read_csv("data.csv");
dataList = data["reading_time"].tolist();
population_mean = statistics.mean(dataList);
print("Population Mean:",population_mean);
fig = ff.create_distplot([dataList],["Reading Time"],show_hist=False);
fig.show();

def random_mean(counter):
  dataSet = []
  for i in range(0,counter):
    randomIndex = random.randint(0,len(dataList))
    value = dataList[randomIndex];
    dataSet.append(value)
  sample_mean = statistics.mean(dataSet)
  return sample_mean 



def setup():
  meanList = []
  for i in range(0,100):
    mean_set = random_mean(30);
    meanList.append(mean_set)
  sampling_mean = statistics.mean(meanList)
  print("Sampling Mean:",sampling_mean)
  showFig(meanList);

def showFig(mean_list):
  df = mean_list
  fig = ff.create_distplot([df],["Reading Time"],show_hist=False)
  fig.show()


setup();