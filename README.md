# Credit Scoring Model Project

## Overview
This project focuses on developing a Credit Scoring Model for a buy-now-pay-later service in partnership with an eCommerce company. The dataset contains transaction records, and the aim is to analyze the data and engineer relevant features that will help in predicting credit risk.

## Notebooks

### 1. `data_cleaning.ipynb`
This notebook is responsible for cleaning the dataset to prepare it for analysis. Key steps include:
- **Loading the Data**: Importing the dataset into a DataFrame.
- **Handling Missing Values**: Identifying and imputing or removing missing values.
- **Data Type Conversion**: Ensuring that columns are of the correct data type for analysis.
- **Dropping Unnecessary Columns**: Removing columns that do not contribute to the analysis or modeling.

### 2. `EDA.ipynb`
This notebook performs Exploratory Data Analysis (EDA) on the cleaned dataset. The main objectives include:
- **Overview of the Data**: Understanding the structure, number of rows, columns, and data types.
- **Summary Statistics**: Analyzing central tendency, dispersion, and distribution shape.
- **Distribution Analysis**: Visualizing numerical and categorical feature distributions to identify patterns and outliers.
- **Correlation Analysis**: Understanding relationships between numerical features.
- **Outlier Detection**: Using box plots to identify potential outliers.


### 3. `Feature_Engineering.ipynb`
This notebook focuses on feature engineering to enhance the dataset for modeling. Key tasks include:
- **Aggregate Features**: Creating new features such as total transaction amount, average transaction amount, transaction count, and standard deviation of transaction amounts for each customer.
- **Time-Based Features**: Extracting features from the transaction timestamp (hour, day, month, year).
- **Encoding Categorical Variables**: Applying Weight of Evidence (WOE) transformation to categorical features for better model interpretability.
- **Handling Missing Values**: Implementing strategies for filling or removing missing values in the dataset.
- **Normalization/Standardization**: Scaling numerical features to ensure they are on a similar scale, improving model performance.
### 4. `Default_Estimator_and_WOE_Binning.ipynb`
This notebook focuses on feature engineering using the RFMS (Recency, Frequency, Monetary, Seniority) formalism and applying Weight of Evidence (WoE) binning for customer risk classification. The main steps include:
 - **RFMS Feature Engineering**: Calculating Recency, Frequency, Monetary, and Seniority features from the transaction data.
 - **Risk Label Assignment**: Classifying customers as 'good' or 'bad' based on their RFMS score.
 - **WoE Binning**: Transforming RFMS features using WoE based on the RiskLabel.
 - **Information Value (IV) Calculation**: Evaluating the importance of each RFMS feature using IV to assess predictive power.
### 5. `Modelling.ipynb`
This notebook trains the machine learning models:
 - **Model Selection**: Random Forest and Gradient Boosting Machines.
 - **Data Splitting**: Dividing data into training and testing sets.
 - **Model Training**: Fitting the models to training data.
 - **Hyperparameter Tuning**: Optimizing models using Grid and Random Search.
 - **Overfitting Prevention**: Using cross-validation and regularization techniques.
 - **Model Evaluation**: Assessing metrics like Accuracy, Precision, Recall, F1 Score, and ROC-AUC.
 - **Ensemble models**: Voting Classifier that combines both Random Forest and Gradient Boosting for making an efficient credit scoring model
 
## Installation
To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yohannestayez/Credit-Scoring-Model.git
   ```

2. **Navigate into the project directory**:
   ## Project Structure

The repository is structured as follows:

```
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml
├──app
│   ├── main.py
│   └── requirements.txt
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│   └── __init__.py
├── notebooks/
│   ├── __init__.py
│   ├── EDA.ipynb
│   ├── data_cleaning.ipynb
│   ├── Feature_Engineering.ipynb
│   ├── Modelling.ipynb
│   └── Default_Estimator_and_WOE_Binning.ipynb
├── tests/
│   └── __init__.py
├── scripts/
│    ├── __init__.py
├── Dockerfile
├──.dockerignore


```

3. **Set up a virtual environment**
4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the project**


6. **Create Docker container**

```bash
docker build -t app-name .

docker run -p 80:80 app-name
```


## Requirements
To run the notebooks, you will need:
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Scorecardpy
- Pickle

## Conclusion
The outputs from the EDA, feature engineering and WOE binning notebooks will be utilized in subsequent modeling tasks to the developed robust credit scoring model. Your contributions and feedback are welcome!

---

