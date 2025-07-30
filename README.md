# Mumbai House Price Prediction

A machine learning web application that predicts house prices in Mumbai based on various features like BHK, area, locality, region, type, status, and age.

## Features

- **Interactive Web Interface**: User-friendly Flask web application
- **Machine Learning Model**: Random Forest Regressor trained on Mumbai house price data
- **Real-time Predictions**: Get instant price predictions in Lakhs
- **Multiple Input Options**: Support for various property types, localities, and regions

## Technologies Used

- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, Random Forest Regressor
- **Data Processing**: Pandas, NumPy
- **Frontend**: HTML, CSS, Bootstrap-like styling

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Mumbai_House_Prediction_Price
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and go to `http://127.0.0.1:5000`

## Usage

1. Fill in the property details:
   - **BHK**: Number of bedrooms, hall, and kitchen
   - **Area**: Property area in square feet
   - **Type**: Apartment, Villa, Studio Apartment, etc.
   - **Status**: Ready to move or Under Construction
   - **Age**: New, Resale, or Unknown
   - **Locality**: Property location
   - **Region**: Property region

2. Click "Predict" to get the estimated price in Lakhs

## Model Details

- **Algorithm**: Random Forest Regressor
- **Features**: 327 engineered features including dummy variables for categorical data
- **Training Data**: Mumbai House Prices dataset
- **Performance**: R² score optimized for accuracy

## Project Structure

```
Mumbai_House_Prediction_Price/
├── app.py                 # Flask application
├── templates/
│   └── form.html         # Web interface
├── Mumbai_house_prediction.ipynb  # Jupyter notebook for model training
├── Mumbai House Prices.csv        # Dataset
├── model_filename.joblib          # Trained model
├── feature_names.joblib           # Feature names
├── requirements.txt               # Python dependencies
└── README.md                     # This file
```

## Data Preprocessing

The model includes sophisticated data preprocessing:
- Price conversion to Lakhs
- Locality simplification (rare localities grouped as 'Other')
- Region simplification (rare regions grouped as 'Other')
- One-hot encoding for categorical variables
- Duplicate removal

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE). 