from flask import Blueprint

app_filter = Blueprint('app_filter', __name__)

from .report_filter import filter_result
from .report_filter import filter_testcase_class
from .report_filter import filter_testcase_result
from .report_filter import filter_group_latest_result
from .report_filter import filter_group_latest_time
from .interface_filter import str_json


# # 注册自定义过滤器
# env = app.jinja_env
# env.filters['filter_result'] = filter_result
# env.filters['filter_testcase_result'] = filter_testcase_result
# env.filters['filter_testcase_class'] = filter_testcase_class
# # env.filters["count_pass"] = count_pass
