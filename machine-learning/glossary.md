## [Imputation](https://www.wikiwand.com/en/Imputation_(statistics))
Filling in data with some of the missing values.
Can promote better results, but obviously results will also be tainted due to lack of real data for imputed entries.
#### Hot-Deck (Dangerous)
Sort the dataset by a column that has all its values, and then use the previous nonempty value in the dataset to fill in this one.

#### Cold-deck (Dangerous, Outdated)
Same as Hot-Deck, but with a different data-set.

#### Mean substitution (Simple, 
Given a column with missing values, populate all missing values in that column with the mean of the entries in the column that do exist.
##### Pros
- Simple
##### Cons
- Problematic for Multivariate Analysis b/c ignores correlation to other vars

#### Regression
Use other columns to predict what the imputed values should be through a regression. Has a problem in that it implies 
##### Pros
- Does not ignore other variables like Mean substitution
##### Cons
- Will give stronger apparent correlations between columns that were used for imputation.

