# Hourly Energy Consumption forecast

This project use to forecasting energy consumption in megawatt hourly

## Install

This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [seaborn](https://seaborn.pydata.org/)
- [xgboost](https://imbalanced-learn.org/stable/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [streamlit](https://streamlit.io/)


## Usage

first, you can clone this git repository

```
git clone https://github.com/HillalXD/Hourly-Energy-Consumption.git
```

then navigate your command to this directory

```
cd Hourly-Energy-Consumption
```

after that run `app.py` to use streamlit app

```
streamlit run app.py
```


## Code 
- Template code is provided in the `xgboost.ipynb` notebook file.
- `PJME_hourly.csv` is provide data source for training model
- `app.py` is streamlit web application to user input features for model predicting 

## Dataset features

for doing prediction you need to input this features:

| features  | explanation  | 
| :-------- | :------- | 
| hour | specific hour for energy forecast |
| day  | specific day in number (monthly) |
| month | month in number |
| year   | specific year for energy forecast |




