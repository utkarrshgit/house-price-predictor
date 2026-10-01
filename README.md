# California House Price Predictor

A machine learning project that predicts the median house value of a California geographic area using demographic and housing-related features.

## Project Overview

The goal of this project is to build a regression model that predicts median house values based on characteristics such as median income, house age, number of rooms, population, occupancy, and geographic location.

The project covers the complete machine learning workflow:

- Data exploration
- Exploratory Data Analysis (EDA)
- Feature and target selection
- Train/test splitting
- Model training
- Model evaluation
- Cross-validation
- Hyperparameter tuning
- Feature importance
- Model serialization
- Prediction on new data
- Streamlit web application

---

## Dataset

The project uses the California Housing dataset provided by `scikit-learn`.

- **Observations:** 20,640
- **Input Features:** 8

### Features

| Feature | Description |
|---|---|
| `MedInc` | Median income in block group |
| `HouseAge` | Median house age in block group |
| `AveRooms` | Average number of rooms per household |
| `AveBedrms` | Average number of bedrooms per household |
| `Population` | Block group population |
| `AveOccup` | Average number of household members |
| `Latitude` | Block group latitude |
| `Longitude` | Block group longitude |

### Target

- **`MedHouseVal`**: Median house value for California districts, expressed in hundreds of thousands of dollars ($100,000s).

Examples:
- `2.0` → $200,000
- `3.5` → $350,000

---

## Models & Evaluation

Several regression models were evaluated:

### 1. Linear Regression
- **Test R²:** 0.576

### 2. Decision Tree
- Tested across varying maximum depths to evaluate underfitting and overfitting.
- Best test performance occurred around depths 8–10:
  - **Test R²:** 0.678–0.682

### 3. Random Forest (Baseline)
- **Test R²:** 0.804
- **5-Fold CV Mean R²:** 0.805

---

## Hyperparameter Tuning

`GridSearchCV` with 5-fold cross-validation was used to optimize the Random Forest regressor.

### Best Parameters
- `n_estimators`: 200
- `max_depth`: None
- `min_samples_split`: 2
- `min_samples_leaf`: 2

**Best Cross-Validation R²:** 0.805

---

## Final Model Performance

Performance metrics for the tuned Random Forest on the test set:

| Metric | Model Output | Dollar Equivalent |
|---|---|---|
| **R²** | 0.806 | — |
| **MAE** | 0.326 | ≈ $32,605 |
| **RMSE** | 0.504 | ≈ $50,401 |

---

## Feature Importance

The Random Forest model identified **`MedInc`** (Median Income) as the most influential feature by a wide margin. 

Other key contributors include:
- `AveOccup`
- `Latitude`
- `Longitude`
- `HouseAge`
- `AveRooms`

> **Note:** Feature importance reflects utility during tree splitting and does not imply direct causal relationships.

---

## Project Structure

```text
house-price-predictor/
│
├── data/
├── notebooks/
│   └── house_price_prediction.ipynb
├── models/
│   └── house_price_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd house-price-predictor

2. **Create and activate a virtual environment:**
   ```bash
    python3 -m venv .venv
    source .venv/bin/activate # On Windows: .venv\Scripts\activate

3. **Install dependencies:**
   ```bash
    pip install -r requirements.txt

4. **Run the Streamlit application:**
    ```bash
    streamlit run app.py

## Limitations

- **Aggregated Data:** Predicts the median value of a geographic block group rather than individual property market values.
- **Target Value Cap:** Target values are capped at $500,000 ($5.0), reducing accuracy for high-end luxury properties.
- **Intended Use:** Designed as an educational machine learning demonstration rather than a production-grade appraisal tool.

## Technologies Used

- **Language:** Python
- **Data Manipulation:** NumPy, Pandas
- **Machine Learning:** Scikit-learn, Joblib
- **Visualization:** Matplotlib, Seaborn
- **Interactive UI:** Streamlit
- **Environment:** Jupyter Notebook