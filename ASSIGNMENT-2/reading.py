# ---------------------------------------------
# IMPORTS
import pandas as pd
import warnings
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier

# ---------------------------------------------

def train_and_eval(model, train_in, train_out, val_in, val_out):
    model.fit(train_in, train_out)
    predicted_val = model.predict(val_in)
    return accuracy_score(val_out, predicted_val)

# CODE
warnings.filterwarnings("ignore")
dataset = pd.read_csv("dataset.csv")

labels = dataset["emotion"]
inputs = dataset.drop("emotion", axis=1)

data_in,test_in,data_out,test_out = train_test_split(inputs,labels,test_size=0.1,stratify=labels,random_state=42)

train_in,val_in,train_out,val_out = train_test_split(data_in,data_out,test_size=0.2 / 0.9,stratify=data_out,random_state=42)

SVC
model_2 = SVC(kernel="linear",probability=True)
print(
    "\nAccuracy of SVC: ",
    train_and_eval(model_2, train_in, train_out, val_in, val_out)
)

test_data = pd.read_csv("test_to_submit.csv")
predicted_emotions = model_2.predict(test_data)
with open("outputs", "w") as file:
    for emotion in predicted_emotions:
        file.write(f"{emotion}\n")

# param_grid = [
#     {"probability":[True,False]}
# ]

# best_model = GridSearchCV(SVC(), param_grid)
# best_model.fit(train_in, train_out)  # Fits on all combinations and keeps best model

# print(
#     "\n\nBest model with best parameters on test set: ",
#     accuracy_score(
#         test_out,
#         best_model.predict(test_in)
#     )
# )
# print(
#     "Best parameters of best model: ",
#     best_model.best_params_
# )




# Decision tree

# model_1 = DecisionTreeClassifier()
# print(
#     "\nAccuracy of Decision tree: ",
#     train_and_eval(model_1, train_in, train_out, val_in, val_out)
# )

# # SVC
# model_2 = SVC()
# print(
#     "\nAccuracy of SVC: ",
#     train_and_eval(model_2, train_in, train_out, val_in, val_out)
# )

# # K-Means
# model_3 = KNeighborsClassifier()
# print(
#     "\nAccuracy of K-Means: ",
#     train_and_eval(model_3, train_in, train_out, val_in, val_out)
# )

# # Gaussian Naive Bayes
# model_4 = GaussianNB()
# print(
#     "\nAccuracy of Gaussian Naive Bayes: ",
#     train_and_eval(model_4, train_in, train_out, val_in, val_out)
# )

# # Multi-layer Perceptron classifier
# model_5 = MLPClassifier()
# print(
#     "\nAccuracy of Multi-layer Perceptron classifier: ",
#     train_and_eval(model_5, train_in, train_out, val_in, val_out)
# )

# # Random forest classifier
# model_6 = RandomForestClassifier()
# print(
#     "\nAccuracy of Random forest classifier: ",
#     train_and_eval(model_6, train_in, train_out, val_in, val_out)
# )

# Hyperparameter search/tuning



# param_grid = [{"kernel":["rbf","linear","poly"]}]
# model = GridSearchCV(SVC(),param_grid=param_grid)
# model.fit(train_in, train_out)
# output = model.predict(val_in)
# print("Your model accuracy is: ", accuracy_score(val_out,output)*100)
# print(model.best_params_)


# model1_neigh = KNeighborsClassifier(n_neighbors=7)
# model1_neigh.fit(train_in,train_out)
# output = model1_neigh.predict(val_in)

# model2_neigh = KNeighborsClassifier(n_neighbors=8)
# model2_neigh.fit(train_in,train_out)
# output = model2_neigh.predict(val_in)

# model3_neigh = KNeighborsClassifier(n_neighbors=9)
# model3_neigh.fit(train_in,train_out)
# output = model3_neigh.predict(val_in)

# param_grid = [{"n_neighbors":[2,5,8]}]
# model_neigh = GridSearchCV(KNeighborsClassifier(),param_grid=param_grid)
# model_neigh.fit(train_in, train_out)
# output = model_neigh.predict(val_in)
# print("Your model accuracy is: ", accuracy_score(val_out,output)*100)
# print(model_neigh.best_params_)


# model_decision1 = DecisionTreeClassifier(criterion="gini")
# model_decision1.fit(train_in,train_out)
# output = model_decision1.predict(val_in)

# model_decision2 = DecisionTreeClassifier(criterion="entropy")
# model_decision2.fit(train_in,train_out)
# output = model_decision2.predict(val_in)

# model_decision3 = DecisionTreeClassifier(criterion="log_loss")
# model_decision3.fit(train_in,train_out)
# output = model_decision3.predict(val_in)

# param_grid = [{"criterion":["gini","entropy","log_loss"]}]
# model_decision = GridSearchCV(DecisionTreeClassifier(),param_grid=param_grid)
# model_decision.fit(train_in, train_out)
# output = model_decision.predict(val_in)
# print("Your model accuracy is: ", accuracy_score(val_out,output)*100)
# print(model_decision.best_params_)


# test_data = pd.read_csv("test_to_submit.csv")

# predictions_model1 = model1.predict(test_data)
# predictions_model2 = model2.predict(test_data)
# predictions_model3 = model3.predict(test_data)

# predictions_model_neigh = model_neigh.predict(test_data)

# predictions_model_decision1 = model_decision1.predict(test_data)

# predictions_model_decision2 = model_decision2.predict(test_data)

# predictions_model_decision3 = model_decision3.predict(test_data)

# final_model = predictions_model_decision1

# with open('outputs', 'w') as output_file:
#     for prediction in final_model:
#         output_file.write(prediction + '\n')