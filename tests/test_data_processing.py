import pandas as pd
import pytest
import numpy as np

# -----------------------------
# Utility function
# -----------------------------


def check_for_nan(df, column):
    """Return True if column has any NaN values."""
    return df[column].isnull().any()

# -----------------------------
# Fixtures
# -----------------------------


@pytest.fixture
def fraud_test_data():
    """Fixture to load the fraud test dataset."""
    return pd.read_csv('../data/raw/Fraud_Data.csv')


@pytest.fixture
def creditcard_test_data():
    """Fixture to load the credit card test dataset."""
    return pd.read_csv('../data/raw/creditcard.csv')

# -----------------------------
# Fraud Data Tests
# -----------------------------


def test_fraud_columns(fraud_test_data):
    """Check that expected columns exist in the fraud test data."""
    expected_cols = ['purchase_value', 'age', 'hour_of_day', 'day_of_week',
                     'time_since_signup', 'transactions_per_user', 'class']
    for col in expected_cols:
        assert col in fraud_test_data.columns


def test_fraud_no_nan(fraud_test_data):
    """Check that there are no NaN values in critical numeric columns."""
    numeric_cols = ['purchase_value', 'age', 'hour_of_day', 'day_of_week',
                    'time_since_signup', 'transactions_per_user']
    for col in numeric_cols:
        assert check_for_nan(fraud_test_data, col) is False


def test_fraud_class_distribution(fraud_test_data):
    """Check that 'class' column contains only 0 and 1."""
    unique_values = set(fraud_test_data['class'].unique())
    assert unique_values.issubset({0, 1})

# -----------------------------
# Credit Card Data Tests
# -----------------------------


def test_creditcard_columns(creditcard_test_data):
    """Check that expected columns exist in the credit card test data."""
    assert 'Class' in creditcard_test_data.columns


def test_creditcard_no_nan(creditcard_test_data):
    """Check that numeric columns have no NaN values."""
    numeric_cols = [
        col for col in creditcard_test_data.columns if col != 'Class']
    for col in numeric_cols:
        assert check_for_nan(creditcard_test_data, col) is False


def test_creditcard_class_distribution(creditcard_test_data):
    """Check that 'Class' column contains only 0 and 1."""
    unique_values = set(creditcard_test_data['Class'].unique())
    assert unique_values.issubset({0, 1})

# -----------------------------
# Optional: Quick Shape Checks
# -----------------------------


def test_fraud_shape(fraud_test_data):
    """Ensure fraud test data has rows and columns."""
    assert fraud_test_data.shape[0] > 0
    assert fraud_test_data.shape[1] > 0


def test_creditcard_shape(creditcard_test_data):
    """Ensure credit card test data has rows and columns."""
    assert creditcard_test_data.shape[0] > 0
    assert creditcard_test_data.shape[1] > 0
