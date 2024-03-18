from sklearn.impute import SimpleImputer
import sklearn.preprocessing as sp
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
def data_clean(df):
    df = df.drop(labels=['campaign_disc_ele', 'forecast_bill_12m', 'date_first_activ', 'forecast_cons',
                         'forecast_base_bill_ele', 'forecast_base_bill_year', 'activity_new', 'channel_sales'], axis=1)
    df = df.drop(labels=['id', 'date_activ', 'date_end', 'date_modif_prod', 'date_renewal'], axis=1)
    new_col = df.columns
    imp = SimpleImputer(strategy='most_frequent')
    imp.fit(df)
    df = imp.transform(df)
    df = pd.DataFrame(df)
    df.columns = new_col
    spl = sp.LabelEncoder()
    df['origin_up'] = spl.fit_transform(df['origin_up'])
    df['has_gas'] = spl.fit_transform(df['has_gas'])
    return df
df = pd.read_csv('ml_case_training_data.csv')
df1 = pd.read_csv('ml_case_training_output.csv')
df['churn'] = df1['churn']
df = data_clean(df)
# print(df)
Y = df['churn'].astype('int')
X = df.drop(labels=['churn'],axis=1)
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
model = LogisticRegression(solver='saga')
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
Churn_prediction = y_pred
print('Accuracy:', metrics.accuracy_score(y_test, y_pred))
fpr,tpr, thresholds = roc_curve(y_test,model.predict_proba(x_test)[:,1])
plt.plot(fpr,tpr,label='ROC')
plt.xlabel('FPR')
plt.ylabel('TPR')
# plt.show()
df = pd.read_csv('ml_case_test_data.csv')
df = data_clean(df)
y_pred = model.predict(df)
y_pred_proba = model.predict_proba(df)
df = pd.read_csv('ml_case_test_output_template.csv',index_col=[0])
df['Churn_prediction'] = y_pred
df['Churn_probability'] = y_pred_proba[:,1]
df.to_csv('ml_case_test_output.csv')