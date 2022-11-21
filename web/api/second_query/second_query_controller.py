from http import HTTPStatus

from flask import Blueprint, request, jsonify

from web.api.second_query.second_query_service import demonstrate_second_query_orm, demonstrate_second_query_native

second_query_orm = Blueprint("Second demonstation query orm", __name__)
second_query_native = Blueprint("Second demonstation query native", __name__)


@second_query_orm.post("/api/secondQuery/orm")
def show_users_with_positive_complaint_orm() -> (dict, int):
    content = request.json
    num_of_seats = content.get("numOfSeats", "")
    start_date = content.get("startDate", "")
    end_date = content.get("endDate", "")

    if any(elem is None for elem in [num_of_seats, start_date, end_date]):
        return {}, HTTPStatus.BAD_REQUEST

    results = demonstrate_second_query_orm(num_of_seats, start_date, end_date)
    return jsonify({"result": results})


@second_query_native.post("/api/secondQuery/native")
def show_users_with_positive_complaint_native() -> (dict, int):
    content = request.json
    num_of_seats = content.get("numOfSeats", "")
    start_date = content.get("startDate", "")
    end_date = content.get("endDate", "")

    if any(elem is None for elem in [num_of_seats, start_date, end_date]):
        return {}, HTTPStatus.BAD_REQUEST

    results = demonstrate_second_query_native(num_of_seats, start_date, end_date)
    return jsonify({"result": results})
