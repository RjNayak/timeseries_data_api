
from validator.validations import validate_input
from flask import request, Response
import json
import requests


def get_average(lst):
    if len(lst) > 0:
        return sum(lst) / len(lst)


def get_cleaned_list(val):
    return [i for i in val if i]


def get_timeframes(timelist, period):
    time_frames = []
    for k in range(0, len(timelist), period):
        time_frames.append(timelist[k])
    return time_frames[1:]


def get_timeseries_data():
    r = requests.get(url='https://reference.intellisense.io/test.dataprovider')
    json_data = r.json()
    return json_data


def configure_handler(app):

    @app.route("/data_transformation/timeseries/v1.0/asset_metrics/average", methods=["POST"])
    def transform_data():

        response_object = {}
        response_code = 200

        # capture data from the POST request
        period_value = request.get_json()["period"]

        if validate_input(period_value):

            # prepare the outer json structure
            out_json = {}
            # prepare the inner json object
            inner_object = {}

            # get timeseries data fromo wrapper function
            timeseries_data = get_timeseries_data()

            for asset_id, value in timeseries_data.items():
                if type(value) is dict:
                    for key, val in value.items():
                        if key != 'time':
                            cleaned_lst = get_cleaned_list(val)
                            out = [get_average(cleaned_lst[k:k+period_value])
                                   for k in range(0, len(cleaned_lst), period_value)]
                            inner_object[key] = out
                        else:
                            time_frame_data = get_timeframes(val, period_value)
                            inner_object['time'] = time_frame_data
                out_json[asset_id] = inner_object

            response_object = json.dumps(out_json, indent=4)

        else:
            response_object = json.dumps({"error": "invalid input"}, indent=4)
            response_code = 400

        return Response(response_object, response_code, mimetype='application/json')
