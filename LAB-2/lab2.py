import pandas as pd
import warnings
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

def main():
    data = pd.read_csv("Face-Feat.txt")
    labels = data["Emotion"]
    inputs = data.drop("Emotion",axis=1)
    
    # 70/20/10
    data_in,test_in,data_out,test_out = train_test_split(inputs,labels,test_size=0.1,stratify=labels,random_state=42)

    train_in,val_in,train_out,val_out = train_test_split(data_in,data_out,test_size=0.2 / 0.9,stratify=data_out,random_state=42)

    #print(len(train_in), len(val_in), len(test_in))

    model1 = DecisionTreeClassifier()
    model1.fit(train_in,train_out)
    output = model1.predict(val_in)

    model2 = SVC()
    model2.fit(train_in,train_out)
    output = model2.predict(val_in)

    model3 = KNeighborsClassifier()
    model3.fit(train_in,train_out)
    output = model3.predict(val_in)
    
    param_grid = [{"kernel":["rbf","linear","poly"]}]
    model = GridSearchCV(SVC(),param_grid=param_grid)
    model.fit(train_in, train_out)
    output = model.predict(val_in)
    print("Your model accuracy is: ", accuracy_score(val_out,output)*100)
    print(model.best_params_)

    # =================================================
    # Exercise: try different amounts of neighbors
    model1_neigh = KNeighborsClassifier(n_neighbors=7)
    model1_neigh.fit(train_in,train_out)
    output = model1_neigh.predict(val_in)

    model2_neigh = KNeighborsClassifier(n_neighbors=8)
    model2_neigh.fit(train_in,train_out)
    output = model2_neigh.predict(val_in)

    model3_neigh = KNeighborsClassifier(n_neighbors=9)
    model3_neigh.fit(train_in,train_out)
    output = model3_neigh.predict(val_in)

    param_grid = [{"n_neighbors":[2,5,8]}]
    model_neigh = GridSearchCV(KNeighborsClassifier(),param_grid=param_grid)
    model_neigh.fit(train_in, train_out)
    output = model_neigh.predict(val_in)
    print("Your model accuracy is: ", accuracy_score(val_out,output)*100)
    print(model_neigh.best_params_)

    # =================================================
    # Exercise: try different amounts of criterions
    model_decision1 = DecisionTreeClassifier(criterion="gini")
    model_decision1.fit(train_in,train_out)
    output = model_decision1.predict(val_in)

    model_decision2 = DecisionTreeClassifier(criterion="entropy")
    model_decision2.fit(train_in,train_out)
    output = model_decision2.predict(val_in)

    model_decision3 = DecisionTreeClassifier(criterion="log_loss")
    model_decision3.fit(train_in,train_out)
    output = model_decision3.predict(val_in)

    param_grid = [{"criterion":["gini","entropy","log_loss"]}]
    model_decision = GridSearchCV(DecisionTreeClassifier(),param_grid=param_grid)
    model_decision.fit(train_in, train_out)
    output = model_decision.predict(val_in)
    print("Your model accuracy is: ", accuracy_score(val_out,output)*100)
    print(model_decision.best_params_)

if __name__ == "__main__":
    warnings.filterwarnings("ignore", category=FutureWarning)
    main()