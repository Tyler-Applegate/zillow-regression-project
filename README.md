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

