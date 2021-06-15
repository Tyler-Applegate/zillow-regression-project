# Zillow Bestimate
## Tyler Applegate, Florence Cohort
### 2021_06_15

### Project Objectives:
- Create a README.md ith project and business goals, as well as data dictionay and initial hypothoses.
- Create a function (or functions) to automate the process of connecting to the Codeup Database, and acquiring the zillow dataframe.
- Save these functions to aquire.py so they can be imported into the final_report notebook.
- Create a series of functions to automate the process of cleaning and preparing the newly acquired zillow dataframe to get it ready for the exploratory, modeling, and MVP stages of the pipeline.
- Save these functions to prepare.py so they can be imported into the final_report notebook.
- Clearly define at least two hypotheses, set an alpha, run necessary statistical testing, reject, or fail to reject each null hypothesis, and document findings are key takeaways.
- Establish a baseline accuracy, model improvement goals.
- Train at least 3 different regression models.
- Evaluate these models on the train, and validate data sets.
- Choose the best model to evaluate on the test dataset.
- Document takeways, key findings, conclusions, and next steps in the final report notebook.

### Business Goals:
- We want to be able to predict the values of single unit properties that the tax district assesses using the property data from those with a transaction during the "hot months" (in terms of real estate demand) of May-August, 2017.
- Build a Machine Learning regression model that outperforms the baseline model to make accurate predictions.
- Document my process so that it can be replicated, as well as read through like a report.

### Audience:
- The Zillow data science team.

### Deliverables:
- A report in the form of a presentation, verbal supported by slides.
    - The report/presentation slides should summarize your findings about the drivers of the single unit property values. This will come from the analysis you do during the exploration phase of the pipeline. In the report, you should have visualizations that support your main points.
    - The presentation should be no longer than 5 minutes.
- A github repository containing your work.
    - This repository should contain one clearly labeled final Jupyter Notebook that walks through the pipeline, but, if you wish, you may split your work among 2 notebooks, one for exploration and one for modeling. In exploration, you should perform your analysis including the use of at least two statistical tests along with visualizations documenting hypotheses and takeaways. In modeling, you should establish a baseline that you attempt to beat with various algorithms and/or hyperparameters. Evaluate your model by computing the metrics and comparing.
    - Make sure your notebook answers all the questions posed in the email from the Zillow data science team.
    - The repository should also contain the .py files necessary to reproduce your work, and your work must be reproducible by someone with their own env.py file.
    - As with every project you do, you should have an excellent README.md file documenting your project planning with instructions on how someone could clone and reproduce your project on their own machine. Include at least your goals for the project, a data dictionary, and key findings and takeaways. Your code should be well documented.
    
### Project Context:
- The Zillow data set came from the Codeup database.

### Data Dictionary:
|Target|Datatype|Definition|
|:-------|:-------|:----------|
|appraised_value|23937 non-null: int64|tax assessed value of property in dollars($)|

|Feature|Datatype|Description|
|:-------|:-------|:----------|
|parcel_id|int64|unique identifier for each home, set as index|
|bath|float|number of bathrooms|
|bed|int64|number of bedrooms|
|sqft_calc|int64|square feet of property|
|fips|int64|Federal Information Processing Standards, unique county code|
|yearbuilt|int64|year property was built|
|tax_amount|float|actual taxes on property in dollars and cents|
|age|int64|how old the property is in years|

### Initial Hypothesis:
- Hypothosis 1: We reject the null hypothesis.
    - alpha: 0.05
    - $H_O$: The age of the home has no impact on the appraised value, (they are independent variables.)
    - $H_a$: The age of the home has an impact on the appraised value, (they are dependent variables.)
- Hypothosis 2: We reject the null hypothesis.
    - alpha: 0.05
    - $H_O$: The mean appraised value of single unit properties with one bathroom is the same for those with more than one bathroom; (they are independent variables.)
    - $H_a$: The mean appraised value of single unit properties with one bathroom is less than those with more than one bathroom; (they are dependent variables.)
    
### Executive Summary:

## Stages of DS Pipeline
Plan -> Data Acquisition -> Data Prep -> Exploratory Analysis -> ML Models -> Delivery

### Planning
- [] Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- [] Acquire data from the Codeup Database and create a series of functions to automate this process. Save the functions in an acquire.py file to import into the Final Report Notebook.
- [] Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a series of functions to automate the process, store the functions in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtions.
- []  Clearly define two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- [] Establish a baseline accuracy and document well.
- [] Train three different regression models.
- [] Evaluate models on train and validate datasets.
- [] Choose the model with that performs the best and evaluate that single model on the test dataset.
- [] Add columns to the DataFrame to show the county and state of each property
- [] Document conclusions, takeaways, and next steps in the Final Report Notebook.

### Data Acquistion
- [] Store functions that are needed to acquire data from the zillow database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.
- [] The final function will return a pandas DataFrame.
- [] Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
- [] Complete some initial data summarization (`.info()`, `.describe()`, `.value_counts()`, `.nunique()`, ...).

### Data Prep
- []  Store functions needed to prepare the zillow data; make sure the module contains the necessary imports to run the code. The final function should do the following:
    - Split the data into train/validate/test.
    - Handle any missing values.
    - Handle erroneous data and/or outliers that need addressing.
    - Encode variables as needed.
    - Create any new features, if made for this project.
- []  Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.

### Exploratory Analysis
- [] Scale continuous data to get more accurate statistical testing
- [] Answer key questions, my hypotheses, and figure out the features that can be used in a regression model to best predict the target variable, appraised_value. 
- [] Run at least 2 statistical tests in data exploration. Document my hypotheses, set an alpha before running the tests, and document the findings well.
- [] Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). The goal is to identify features that are related to appraised_value (the target), identify any data integrity issues, and understand 'how the data works'. If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.
- [] Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.

### ML Models
- [] Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
- [] Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
- [] Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
- [] Feature Selection (after initial iteration through pipeline): Are there any variables that seem to provide limited to no additional information? If so, remove them.
- [] Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
- [] Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.

### Delivery
> - Introduce myself and my project goals at the very beginning of my slide presentation.
> - Provide an Executive Summary to highlight the 'one big thing.' 
> - Walk Zillow Data Science Team through the analysis I did to answer my questions and that lead to my findings. (Visualize relationships and Document takeaways.) 
> - Clearly call out the questions and answers I am analyzing as well as offer insights and recommendations based on my findings.

## How to Reproduce this Project
> - You will need your own env file with credentials for the database, along with these files to recreate my project:
    > - README.md
    > - acquire.py
    > - prepare.py
    > - explore.py
    > - run the final_report.ipynb notebook