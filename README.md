<h1 align="center">Timeseries Data API</h1>

## About

The Flask application provides API endpoint for grouping data and calculate average of values within the time period. Based on assumptions the result of the API also has a key called time which holds the time interval over which the data ais grouped. The API pulls the data from another REST API data provides JSON timeseries data a list of specific metrics id for a specific asset id.

The API also has pytest unit test cases to verify various test case scenarios

## API Documentation

There endpoint helps in grouping timeseries data over a period of time
<br>
<b> /asset_metrics/average </b>
<br>
Accepts a single JSON object with a key named "period". The period value is numeric and represents a value in minutes. The API returns the values in average grouping data over a period of time
<br

     - input : application/json
     - output : application/json

<br>

For better understanding please refer to the SwaggerHub link below

https://app.swaggerhub.com/apis/RjNayak/timeseries_data_api/1.0.0

## Technologies

The following technologies are used in this project:

- [Python](https://www.python.org/)
- [requests] (https://pypi.org/project/requests/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Pytest](https://docs.pytest.org/en/6.2.x/)
- [Docker](https://www.docker.com/)

## Requirements

Before starting you need to have [Python](https://www.python.org/) installed.

## Running

```bash
# Clone this project
$ git clone https://github.com/RjNayak/timeseries_data_api.git

# Access
$ cd timeseries_data_api

# Install dependencies
$ pip install -r requirements.txt

# Run the project
$ python app.py

# The server will initialize in the <http://localhost:5000>

# Test the endpoints
$ pytest test.py

# To run with docker
$ docker build -t timeseries_data_api:latest .
$ docker run -d -p 5000:5000 timeseries_data_api

```

<a href="#top">Back to top</a>
