# Kaggle Tabular Playground Series Dec 21 Competition

### A Machine Learning Kaggle Competition Start to Finish

###### By: Aurelio Barrios

This project is used to showcase a brief approach to a [kaggle machine learning competition](https://www.kaggle.com/c/tabular-playground-series-dec-2021/overview) start to finish. Although the process shown in this project is not extensive it aims to provide a basis on which to build on. This project showcases data analysis processes like feature engineering, feature selection as well as machine learning tasks like hyper-parameter tuning.

### What Is Shown In This Project

* Domain of Project
  * Machine Learning
* Machine Learning Task
  * Classification. Predicting the Cover Type (predominant king of tree cover) using forest features.
* Metrics
  * Machine Learning Models will be evaluated locally using balanced accuracy
  * Kaggle submissions also evaluated on accuracy on their specific test set

### How To Use This Project

* Have Python installed locally, versions >= 3.5 preferred
* Due to GitHub file size limitations users must download kaggle data locally using command
```
kaggle competitions download -c tabular-playground-series-dec-2021
```

### Contents

* **main.ipynb**: A jupyter notebook outlining my full machine learning process from start to finish for this competition
* **training_1**: A folder that has the latest TensorFlow NN model used for this project
* **data/submission1.csv**: My first submission using a SGD classifier achieving 89.8% accuracy
* **data/submission2.csv**: My second submission using a TensorFlow NN model achieving 93.4% accuracy
* **data/sample_submission.csv**: Sample submission file provided by kaggle
