import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import pandas as pd


fields = ['level', 'time', 'health', 'score']
df = pd.read_csv("1111111.csv", skipinitialspace=True, usecols=fields)

x = np.array(df[['health', 'time', 'score']])
y = np.array(df['level'])

model = LinearRegression()
model.fit(x, y)
# model = LinearRegression().fit(x, y)
X = sm.add_constant(x)
model = sm.OLS(y, X).fit()
predictions = model.predict(X)

#create statistics
final_model = model.summary()
print(final_model)


# fields = ['health', 'level']
# df = pd.read_csv("1111111.csv", skipinitialspace=True, usecols=fields)
#
# x = np.array(df['level']).reshape((-1, 1))
# y = np.array(df['health'])
#
# model = LinearRegression()
# model.fit(x, y)
# model = LinearRegression().fit(x, y)
# r_sq = model.score(x, y)
# y_pred = model.predict(x)
# print('predicted response:', y_pred, sep='\n')