# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model runs a Random Forest Classifier
## Intended Use
The intention is to predict whether a person will make more or less than $50,000 @ year
## Training Data
The training data is made up of multiple columns such as "workclass", "education",  "marital-status", "occupation", "relationship", "race", "sex", "native-country"
## Evaluation Data
The testing data is made up of the same but is reduced to .25 of the total size
## Metrics
Precision: 0.7827 | Recall: 0.6265 | F1: 0.6959
## Ethical Considerations
If this data were more recent and all encompassing this data could be used to discriminate against people who don't make much money. Since it's not recent, this particular dataset would not be unethical.
## Caveats and Recommendations
The static data (as mentioned above) is not reliable since it does not get updated. 