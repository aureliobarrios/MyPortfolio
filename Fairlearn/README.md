# Building A Fair ML Model Using Fairlearn For Loan Acceptance Prediction

### Maintaining Accuracy While Providing Fairness In Loan Acceptance For Sensitive Attributes Like Race & Sex

###### By: Aurelio Barrios

There is a dangerous belief that algorithms remove human biases. In recent times we have seen how machine learning algorithms have reflected human biases in their implementations, see [Vox article](https://www.vox.com/recode/2020/2/18/21121286/algorithms-bias-discrimination-facial-recognition-transparency). It is easy to think that machine learning models are unbiased and fair, but it is our responsibility to ensure that the machine learning models being deployed today do not implement the biases of yesterday. This project aims to provide a fair machine learning model that will accurately classify whether to approve a loan whilst also maintaining fairness across sensitive attributes like race and sex. Through this project I learned that there is not a big tradeoff between fairness and accuracy. It is entirely possible to maintain a respectable accuracy whilst also eliminating discriminatory biases in our models.  

### What Is Shown In This Project

* Domain of Project
  * Finance (Loan Approval)
  * Building Ethical Machine Learning Models
* Machine Learning Task
  * Binary classification. Predict wether to accept or decline a loan application based on given features.
* Metrics
  * Machine learning model will be evaluated using balanced accuracy
  * Fairlearn model implementation will be evaluated using the following
    * Demographic parity difference
    * Equalized odds difference
    * Demographic parity ratio

### How To Use This Project

* Have Python installed locally, versions >= 3.5 will work.
* HMDA California 2017 dataset. Other HMDA datasets will work as well. Due to GitHub file size limits data must be downloaded locally: [zip file download (1.38GB)](https://files.consumerfinance.gov/hmda-historic-loan-data/hmda_2017_ca_all-records_labels.zip)
* Must have [Fairlearn](https://fairlearn.org) package installed locally. Install using command.

```
pip install fairlearn
```

### Contents

* **Report.pdf**: A report that complements this project used to delve deeper into the project process, findings, conclusion and provide visualizations.
* **cleaningForModels.ipynb**: Initial data cleaning process used in order to prepare raw data for future ML models.
* **fairModel.ipynb**: ML model implementation and fairness building using Fairlearn.
