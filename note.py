#
Plots in Matplotlib Python
Matplotlib is a data visualization library in Python. The pyplot, a sublibrary of matplotlib, is a collection of functions that helps in creating a variety of charts. Using matplotlib you can plot various plots very easily. Let’s take a look at various plots that it has to offer:-

Line Plot
Scatter Plot
Histogram
Bar Plot
Pie Chart
Box Plot
#

df = pd.read_csv('data.csv')
df.dropna(axis = 1,inplace = True)
df.head()

import matplotlib.pyplot as plt
%matplotlib inline

  Line
  
plt.plot([2,14,8,5,10])
  plt.show()

Scatter Plot

plt.scatter(x=df[''], y=df[''] )
  plt.show()


Histogram

  x=np.random.normal(150,10,250)
  plt.hist(x)
  plt.show()


Bar Plot

  plt.bar(df[''],df[''])
  plt.show()

Box Plot
  x=np.random.normal(50,10,250)
   plt.boxplot(x)
   plt.show()

Pie chart
   plt.pie([35,25,15])
   plt.show()

  plt.title()
  plt.scatter()
  plt.xlabel()
  plt.ylabel()
  plt.show() 
   
  plt.figure(figsize=(12,8))

  plt.scatter(x=df[''],y=df[''], alpha=0.5,label=' ') 
  
  plt.legend()

  plt.subplot2grid((4,4), (0,0), colspan=4)

  x.tight_layout()
