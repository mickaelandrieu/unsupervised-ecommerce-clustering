# E-commerce scoring from Olist Data

## How to get the dataset

You can download the dataset and its documentation on [Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce)

## Local installation

```bash
python -m venv dev
source dev/Scripts/activate
pip install -r requirements.txt
```

## Docker installation

### Build the image

```bash
docker build --tag app:1.0 .
```

## Train the model

1. Download the RAW data ;
2. Execute `src/clean.py` to create `cleaned_data.csv` ;
3. Execute `src/prepare_features.py` to create `training.pkl` ;
4. Execute `src/create_scoring.py` to create `training_folds.pkl` ;

## Quality tools

```bash
python -m isort src/
python -m black src/
python -m flake8 src/ --count --statistics
```

## LICENSE

This project is provided under the MIT license.
