from http import HTTPStatus

from flask import Blueprint, request, jsonify

from web.api.first_query.first_query_service import demonstrate_first_query_orm, demonstrate_first_query_native

first_query_orm = Blueprint("First demonstation query orm", __name__)
first_query_native = Blueprint("First demonstation query native", __name__)


@first_query_orm.post("/api/firstQuery/orm")
def update_complaint_orm() -> (dict, int):
    content = request.json
    user_login = content.get("userLogin", "")
    order_start_time = content.get("orderTime", "")
    complaint_time = content.get("complaintTime", "")
    status_to_update = content.get("statusToUpdate", "")

    if any(elem is None for elem in [user_login, order_start_time, complaint_time, status_to_update]):
        return {}, HTTPStatus.BAD_REQUEST

    demonstrate_first_query_orm(user_login, order_start_time, complaint_time, status_to_update)
    return jsonify({"result": "complated"})


@first_query_native.post("/api/firstQuery/native")
def update_complaint_native() -> (dict, int):
    content = request.json
    user_login = content.get("userLogin", "")
    order_start_time = content.get("orderTime", "")
    complaint_time = content.get("complaintTime", "")
    status_to_update = content.get("statusToUpdate", "")

    if any(elem is None for elem in [user_login, order_start_time, complaint_time, status_to_update]):
        return {}, HTTPStatus.BAD_REQUEST

    demonstrate_first_query_native(user_login, order_start_time, complaint_time, status_to_update)
    return jsonify({"result": "complated"})
