# AI-projects
this is repo for AI projects 

about implementation AI:
AI Pipeline
AI pipeline is the sequence of operations to be done to create an AI model to solve a specific problem

1- Data Gathering ( collecting data )
2- Data Preprocessing
3- Feature Engineering
4- Model Selection
5- Transformation / Fitting
6- Training
7- Testing
8- Deployment
9- Monitoring Performance
Step 1: Data Gathering:
Collecting all the data required to solve the problems
Where does this data come from ?
1- The Organization data itself ( employees performance, users behavior, market status, needs, shared data )
2- The new collected data ( the data Engineer must specify what data needed and why
3- Scapping ( getting the data ourselves from the web
4- Surveys ( forms might be filled to collect enough data

Step 2: Data Preprocessing/ Handling:
The collected data might be corrupted, missing rows, columns, formatted in a wrong way, in this step we filter the data to make sure it is ready to be fitted in the model

Step 3: Feature Engineering/ Selection:
After the data is filtered, the Data Scientist ( Analyist ) perform some statistical operation to filter only the important data from the whole data

Why this is an issue ?
This processes needs deep knowledge in the problem to select the best features.
Statistics may show that the important features are not the features that are logically important ( According to the problem field ) which could mean on of two things:

1- The data is not enough ( or even not right )
2- The statistics are not done proberly
Possible Solutions:
Redo the calculations
update the data itself
go with what the statsitics said
go with the logical features
What is the problem with theses possible solutions?
Time Consumption
Data Storage
Processing power
Overall confusion which may lead to uncountable mistakes and then get back to square zero
Step 4: Model Selection:
What parameters do we consider when selecting our model?
1- The problem Type:
Possible problem types : Classification - Regression - clustering - Generation
Also, if the problem is critical we may need to use the model that are more likely to perform better even if it's slower

2- Data type/ size:
Based on the data size we select the model that handel this amount of data in an easy way
if the data is small we might be able to try different models to select the one that has the best performance, otherwise it's Time Consuming

3- Time:
If we have a long time to get the best solution, we should consider giving more time to think about the model, and may even try some models and compare their accuracy.

If we don't have that amount of time, we choose the fastest most promising to give the best performance model ( this can be done because we know our data proberly so we know what is the best model for this kind of data.

Step 5: Fitting/ Transformation:
A model accepts data only in numeric values shaped as arrays or vectors (i.e. numpy arrays in python )
so before fitting the data we need to make sure it's the best representation of our data to be fitted into our model, that may include a regularization or normalization step.

Spliting the data
We have to split the data to be able to test the model later
Data is splitted into training data and test data
Then we fit the Training data

Step 6: Training:
Trainig process is basically ordering the model to start learning from this data.

We control this phase by specifying the training time, and some other arguments like ( patch size, epoches, random states , activation function ..etc.)

Step 7: Testing:
The most important phase, we want to check that our model performes as we hoped, we check the accuracy, check for overfitting and underfitting, and also check for which data were right and which were wrong

Testing is done on the test data ( sometimes on all data if some algorithms are applied )

Testing has two cases:

Accepted : when we have achieved the performance we hoped for
Failed : when the model doesn't perform well
Solution Sequence:
If our model fails the test, we do these operations in order:

1- Increase the training time ( Hyperparameter Tuining )
2- If step one failed, we try to change the model to a different one
3- If step two failed, we return to our data to perform reprocessing and analysis on it ( may cause to change its format or features )

This often happens due to :


1- Data, data in real life problems have a high ratio of randomness, misleading info, misunderstood concepts
2- Not enough time was set to data perprocessing and feature engineering
3- The problem is too complicated and need a long phase of model optimiztion
Step 8: Deployment : The process of actually using the model to solve new instances of the trained on problem
This is done by saving the model, model weights, uploading the model to a server ( could be local ) and then use it via an application request using the API

Step 9: Monitoring Peformance:
As the behavior of the data changes due to many reasons, the model should adapt to theses changes in data values and range, so we have to eight retrain it every now and then ( based on some conditions ) Or use transfer learning ( Automate the process )

