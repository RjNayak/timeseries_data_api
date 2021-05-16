
from routes.request_handler import configure_handler
from flask import Flask, request, Response
import requests
import json


def test_data_service_availibility():
    r = requests.get(url='https://reference.intellisense.io/test.dataprovider')
    assert r is not None


def test_api_for_valid_input():
    app = Flask(__name__)
    configure_handler(app)
    client = app.test_client()
    url = 'http://localhost:5000/data_transformation/timeseries/v1.0/asset_metrics/average'

    mock_request_headers = {
        'Content-Type': 'application/json'
    }

    mock_request_data = json.dumps({"period": 10})

    response = client.post(url, data=mock_request_data,
                           headers=mock_request_headers)

    assert response.status_code == 200


def test_api_for_text_input():
    app = Flask(__name__)
    configure_handler(app)
    client = app.test_client()
    url = 'http://localhost:5000/data_transformation/timeseries/v1.0/asset_metrics/average'

    mock_request_headers = {
        'Content-Type': 'application/json'
    }

    mock_request_data = json.dumps({"period": 'abcdef'})

    response = client.post(url, data=mock_request_data,
                           headers=mock_request_headers)

    response_dict = json.loads(response.data)
    assert response.status_code == 400 and "error" in response_dict


def test_api_for_alphanumeric_input():
    app = Flask(__name__)
    configure_handler(app)
    client = app.test_client()
    url = 'http://localhost:5000/data_transformation/timeseries/v1.0/asset_metrics/average'

    mock_request_headers = {
        'Content-Type': 'application/json'
    }

    mock_request_data = json.dumps({"period": '123abcd'})

    response = client.post(url, data=mock_request_data,
                           headers=mock_request_headers)

    response_dict = json.loads(response.data)
    assert response.status_code == 400 and "error" in response_dict


def test_api_for_charnumber_input():
    app = Flask(__name__)
    configure_handler(app)
    client = app.test_client()
    url = 'http://localhost:5000/data_transformation/timeseries/v1.0/asset_metrics/average'

    mock_request_headers = {
        'Content-Type': 'application/json'
    }

    mock_request_data = json.dumps({"period": ''})

    response = client.post(url, data=mock_request_data,
                           headers=mock_request_headers)

    response_dict = json.loads(response.data)
    assert response.status_code == 400 and "error" in response_dict


def test_api_for_blank_input():
    app = Flask(__name__)
    configure_handler(app)
    client = app.test_client()
    url = 'http://localhost:5000/data_transformation/timeseries/v1.0/asset_metrics/average'

    mock_request_headers = {
        'Content-Type': 'application/json'
    }

    mock_request_data = json.dumps({"period": ''})

    response = client.post(url, data=mock_request_data,
                           headers=mock_request_headers)

    response_dict = json.loads(response.data)
    assert response.status_code == 400 and "error" in response_dict


def test_api_for_valid_out():
    app = Flask(__name__)
    configure_handler(app)
    client = app.test_client()
    url = 'http://localhost:5000/data_transformation/timeseries/v1.0/asset_metrics/average'

    mock_request_headers = {
        'Content-Type': 'application/json'
    }

    mock_request_data = json.dumps({"period": 60})

    response = client.post(url, data=mock_request_data,
                           headers=mock_request_headers)

    response_dict = json.loads(response.data)
    for key, val in response_dict.items():
        if type(val) is dict:
            for keys, values in val.items():
                assert len(values) == 3
