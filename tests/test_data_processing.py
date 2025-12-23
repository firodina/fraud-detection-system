import pandas as pd
import pytest
from collections import Counter

# -----------------------------
# Utility
# -----------------------------


def check_for_nan(df, column):
    return df[column].isnull().any()

# -----------------------------
# Fixtures
# -----------------------------


@pytest.fixture
def fraud_test_data():
    return pd.read_csv("data/raw/Fraud_Data.csv")


@pytest.fixture
def creditcard_test_data():
    return pd.read_csv("data/raw/creditcard.csv")

# -----------------------------
# Fraud Data Tests (RAW)
# -----------------------------


def test_fraud_columns(fraud_test_data):
    expected_cols = [
        'user_id', 'signup_time', 'purchase_time',
        'purchase_value', 'device_id', 'source',
        'browser', 'sex', 'age', 'ip_address', 'class'
    ]
    for col in expected_cols:
        assert col in fraud_test_data.columns


def test_fraud_no_nan(fraud_test_data):
    for col in ['purchase_value', 'age']:
        assert not check_for_nan(fraud_test_data, col)


def test_fraud_class_distribution(fraud_test_data):
    assert set(fraud_test_data['class'].unique()).issubset({0, 1})


def test_fraud_shape(fraud_test_data):
    assert fraud_test_data.shape[0] > 0
    assert fraud_test_data.shape[1] > 0

# -----------------------------
# Credit Card Tests
# -----------------------------


def test_creditcard_columns(creditcard_test_data):
    assert 'Class' in creditcard_test_data.columns


def test_creditcard_no_nan(creditcard_test_data):
    for col in creditcard_test_data.columns:
        if col != 'Class':
            assert not check_for_nan(creditcard_test_data, col)


def test_creditcard_class_distribution(creditcard_test_data):
    assert set(creditcard_test_data['Class'].unique()).issubset({0, 1})


def test_creditcard_shape(creditcard_test_data):
    assert creditcard_test_data.shape[0] > 0
    assert creditcard_test_data.shape[1] > 0
