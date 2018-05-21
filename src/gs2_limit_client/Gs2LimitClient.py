# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client
from aws_sdk_for_serverless.common import url_encoder


class Gs2LimitClient(AbstractGs2Client):

    ENDPOINT = "limit"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2LimitClient, self).__init__(credential, region)

    def create_counter_master(self, request):
        """
        カウンターマスターを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_limit_client.control.CreateCounterMasterRequest.CreateCounterMasterRequest
        :return: 結果
        :rtype: gs2_limit_client.control.CreateCounterMasterResult.CreateCounterMasterResult
        """
        body = { 
            "name": request.get_name(),
            "max": request.get_max(),
            "resetType": request.get_reset_type(),
        }

        if request.get_reset_day_of_month() is not None:
            body["resetDayOfMonth"] = request.get_reset_day_of_month()
        if request.get_reset_day_of_week() is not None:
            body["resetDayOfWeek"] = request.get_reset_day_of_week()
        if request.get_reset_hour() is not None:
            body["resetHour"] = request.get_reset_hour()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_limit_client.control.CreateCounterMasterRequest import CreateCounterMasterRequest
        from gs2_limit_client.control.CreateCounterMasterResult import CreateCounterMasterResult
        return CreateCounterMasterResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/limit/" + str(("null" if request.get_limit_name() is None or request.get_limit_name() == "" else url_encoder.encode(request.get_limit_name()))) + "/master/counter",
            service=self.ENDPOINT,
            component=CreateCounterMasterRequest.Constant.MODULE,
            target_function=CreateCounterMasterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_counter_master(self, request):
        """
        カウンターマスターを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_limit_client.control.DeleteCounterMasterRequest.DeleteCounterMasterRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_limit_client.control.DeleteCounterMasterRequest import DeleteCounterMasterRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/limit/" + str(("null" if request.get_limit_name() is None or request.get_limit_name() == "" else url_encoder.encode(request.get_limit_name()))) + "/master/counter/" + str(("null" if request.get_counter_name() is None or request.get_counter_name() == "" else url_encoder.encode(request.get_counter_name()))) + "",
            service=self.ENDPOINT,
            component=DeleteCounterMasterRequest.Constant.MODULE,
            target_function=DeleteCounterMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_counter_master(self, request):
        """
        カウンターマスターの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_limit_client.control.DescribeCounterMasterRequest.DescribeCounterMasterRequest
        :return: 結果
        :rtype: gs2_limit_client.control.DescribeCounterMasterResult.DescribeCounterMasterResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_limit_client.control.DescribeCounterMasterRequest import DescribeCounterMasterRequest

        from gs2_limit_client.control.DescribeCounterMasterResult import DescribeCounterMasterResult
        return DescribeCounterMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/limit/" + str(("null" if request.get_limit_name() is None or request.get_limit_name() == "" else url_encoder.encode(request.get_limit_name()))) + "/master/counter",
            service=self.ENDPOINT,
            component=DescribeCounterMasterRequest.Constant.MODULE,
            target_function=DescribeCounterMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_counter_master(self, request):
        """
        カウンターマスターを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_limit_client.control.GetCounterMasterRequest.GetCounterMasterRequest
        :return: 結果
        :rtype: gs2_limit_client.control.GetCounterMasterResult.GetCounterMasterResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_limit_client.control.GetCounterMasterRequest import GetCounterMasterRequest

        from gs2_limit_client.control.GetCounterMasterResult import GetCounterMasterResult
        return GetCounterMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/limit/" + str(("null" if request.get_limit_name() is None or request.get_limit_name() == "" else url_encoder.encode(request.get_limit_name()))) + "/master/counter/" + str(("null" if request.get_counter_name() is None or request.get_counter_name() == "" else url_encoder.encode(request.get_counter_name()))) + "",
            service=self.ENDPOINT,
            component=GetCounterMasterRequest.Constant.MODULE,
            target_function=GetCounterMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_counter_master(self, request):
        """
        カウンターマスターを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_limit_client.control.UpdateCounterMasterRequest.UpdateCounterMasterRequest
        :return: 結果
        :rtype: gs2_limit_client.control.UpdateCounterMasterResult.UpdateCounterMasterResult
        """
        body = { 
            "max": request.get_max(),
            "resetType": request.get_reset_type(),
        }
        if request.get_reset_day_of_month() is not None:
            body["resetDayOfMonth"] = request.get_reset_day_of_month()
        if request.get_reset_day_of_week() is not None:
            body["resetDayOfWeek"] = request.get_reset_day_of_week()
        if request.get_reset_hour() is not None:
            body["resetHour"] = request.get_reset_hour()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_limit_client.control.UpdateCounterMasterRequest import UpdateCounterMasterRequest
        from gs2_limit_client.control.UpdateCounterMasterResult import UpdateCounterMasterResult
        return UpdateCounterMasterResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/limit/" + str(("null" if request.get_limit_name() is None or request.get_limit_name() == "" else url_encoder.encode(request.get_limit_name()))) + "/master/counter/" + str(("null" if request.get_counter_name() is None or request.get_counter_name() == "" else url_encoder.encode(request.get_counter_name()))) + "",
            service=self.ENDPOINT,
            component=UpdateCounterMasterRequest.Constant.MODULE,
            target_function=UpdateCounterMasterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_counter(self, request):
        """
        カウンターを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_limit_client.control.DeleteCounterRequest.DeleteCounterRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_limit_client.control.DeleteCounterRequest import DeleteCounterRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/limit/" + str(("null" if request.get_limit_name() is None or request.get_limit_name() == "" else url_encoder.encode(request.get_limit_name()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "/counter/" + str(("null" if request.get_counter_name() is None or request.get_counter_name() == "" else url_encoder.encode(request.get_counter_name()))) + "",
            service=self.ENDPOINT,
            component=DeleteCounterRequest.Constant.MODULE,
            target_function=DeleteCounterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_counter(self, request):
        """
        カウンターの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_limit_client.control.DescribeCounterRequest.DescribeCounterRequest
        :return: 結果
        :rtype: gs2_limit_client.control.DescribeCounterResult.DescribeCounterResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_limit_client.control.DescribeCounterRequest import DescribeCounterRequest

        from gs2_limit_client.control.DescribeCounterResult import DescribeCounterResult
        return DescribeCounterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/limit/" + str(("null" if request.get_limit_name() is None or request.get_limit_name() == "" else url_encoder.encode(request.get_limit_name()))) + "/counter",
            service=self.ENDPOINT,
            component=DescribeCounterRequest.Constant.MODULE,
            target_function=DescribeCounterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def describe_counter_by_user_id(self, request):
        """
        ユーザのカウンターの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_limit_client.control.DescribeCounterByUserIdRequest.DescribeCounterByUserIdRequest
        :return: 結果
        :rtype: gs2_limit_client.control.DescribeCounterByUserIdResult.DescribeCounterByUserIdResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_limit_client.control.DescribeCounterByUserIdRequest import DescribeCounterByUserIdRequest

        from gs2_limit_client.control.DescribeCounterByUserIdResult import DescribeCounterByUserIdResult
        return DescribeCounterByUserIdResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/limit/" + str(("null" if request.get_limit_name() is None or request.get_limit_name() == "" else url_encoder.encode(request.get_limit_name()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "/counter",
            service=self.ENDPOINT,
            component=DescribeCounterByUserIdRequest.Constant.MODULE,
            target_function=DescribeCounterByUserIdRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_counter(self, request):
        """
        カウンターを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_limit_client.control.GetCounterRequest.GetCounterRequest
        :return: 結果
        :rtype: gs2_limit_client.control.GetCounterResult.GetCounterResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_limit_client.control.GetCounterRequest import GetCounterRequest

        from gs2_limit_client.control.GetCounterResult import GetCounterResult
        return GetCounterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/limit/" + str(("null" if request.get_limit_name() is None or request.get_limit_name() == "" else url_encoder.encode(request.get_limit_name()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "/counter/" + str(("null" if request.get_counter_name() is None or request.get_counter_name() == "" else url_encoder.encode(request.get_counter_name()))) + "",
            service=self.ENDPOINT,
            component=GetCounterRequest.Constant.MODULE,
            target_function=GetCounterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_my_counter(self, request):
        """
        カウンターを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_limit_client.control.GetMyCounterRequest.GetMyCounterRequest
        :return: 結果
        :rtype: gs2_limit_client.control.GetMyCounterResult.GetMyCounterResult
        """
        query_strings = {
        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_limit_client.control.GetMyCounterRequest import GetMyCounterRequest

        from gs2_limit_client.control.GetMyCounterResult import GetMyCounterResult
        return GetMyCounterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/limit/" + str(("null" if request.get_limit_name() is None or request.get_limit_name() == "" else url_encoder.encode(request.get_limit_name()))) + "/counter/" + str(("null" if request.get_counter_name() is None or request.get_counter_name() == "" else url_encoder.encode(request.get_counter_name()))) + "",
            service=self.ENDPOINT,
            component=GetMyCounterRequest.Constant.MODULE,
            target_function=GetMyCounterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def up_counter(self, request):
        """
        カウンターを進めます<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_limit_client.control.UpCounterRequest.UpCounterRequest
        :return: 結果
        :rtype: gs2_limit_client.control.UpCounterResult.UpCounterResult
        """
        body = { 
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_limit_client.control.UpCounterRequest import UpCounterRequest
        from gs2_limit_client.control.UpCounterResult import UpCounterResult
        return UpCounterResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/limit/" + str(("null" if request.get_limit_name() is None or request.get_limit_name() == "" else url_encoder.encode(request.get_limit_name()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "/counter/" + str(("null" if request.get_counter_name() is None or request.get_counter_name() == "" else url_encoder.encode(request.get_counter_name()))) + "",
            service=self.ENDPOINT,
            component=UpCounterRequest.Constant.MODULE,
            target_function=UpCounterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def up_my_counter(self, request):
        """
        カウンターを進めます<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_limit_client.control.UpMyCounterRequest.UpMyCounterRequest
        :return: 結果
        :rtype: gs2_limit_client.control.UpMyCounterResult.UpMyCounterResult
        """
        body = { 
        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_limit_client.control.UpMyCounterRequest import UpMyCounterRequest
        from gs2_limit_client.control.UpMyCounterResult import UpMyCounterResult
        return UpMyCounterResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/limit/" + str(("null" if request.get_limit_name() is None or request.get_limit_name() == "" else url_encoder.encode(request.get_limit_name()))) + "/counter/" + str(("null" if request.get_counter_name() is None or request.get_counter_name() == "" else url_encoder.encode(request.get_counter_name()))) + "",
            service=self.ENDPOINT,
            component=UpMyCounterRequest.Constant.MODULE,
            target_function=UpMyCounterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def get_current_counter_master(self, request):
        """
        現在適用されている回数制限マスターを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_limit_client.control.GetCurrentCounterMasterRequest.GetCurrentCounterMasterRequest
        :return: 結果
        :rtype: gs2_limit_client.control.GetCurrentCounterMasterResult.GetCurrentCounterMasterResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_limit_client.control.GetCurrentCounterMasterRequest import GetCurrentCounterMasterRequest

        from gs2_limit_client.control.GetCurrentCounterMasterResult import GetCurrentCounterMasterResult
        return GetCurrentCounterMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/limit/" + str(("null" if request.get_limit_name() is None or request.get_limit_name() == "" else url_encoder.encode(request.get_limit_name()))) + "/counter/master",
            service=self.ENDPOINT,
            component=GetCurrentCounterMasterRequest.Constant.MODULE,
            target_function=GetCurrentCounterMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_current_counter_master(self, request):
        """
        回数制限マスターをインポートします<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_limit_client.control.UpdateCurrentCounterMasterRequest.UpdateCurrentCounterMasterRequest
        :return: 結果
        :rtype: gs2_limit_client.control.UpdateCurrentCounterMasterResult.UpdateCurrentCounterMasterResult
        """
        body = { 
            "settings": request.get_settings(),
        }

        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_limit_client.control.UpdateCurrentCounterMasterRequest import UpdateCurrentCounterMasterRequest
        from gs2_limit_client.control.UpdateCurrentCounterMasterResult import UpdateCurrentCounterMasterResult
        return UpdateCurrentCounterMasterResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/limit/" + str(("null" if request.get_limit_name() is None or request.get_limit_name() == "" else url_encoder.encode(request.get_limit_name()))) + "/counter/master",
            service=self.ENDPOINT,
            component=UpdateCurrentCounterMasterRequest.Constant.MODULE,
            target_function=UpdateCurrentCounterMasterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def create_limit(self, request):
        """
        回数制限を新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_limit_client.control.CreateLimitRequest.CreateLimitRequest
        :return: 結果
        :rtype: gs2_limit_client.control.CreateLimitResult.CreateLimitResult
        """
        body = { 
            "name": request.get_name(),
        }

        if request.get_description() is not None:
            body["description"] = request.get_description()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_limit_client.control.CreateLimitRequest import CreateLimitRequest
        from gs2_limit_client.control.CreateLimitResult import CreateLimitResult
        return CreateLimitResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/limit",
            service=self.ENDPOINT,
            component=CreateLimitRequest.Constant.MODULE,
            target_function=CreateLimitRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_limit(self, request):
        """
        回数制限を削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_limit_client.control.DeleteLimitRequest.DeleteLimitRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_limit_client.control.DeleteLimitRequest import DeleteLimitRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/limit/" + str(("null" if request.get_limit_name() is None or request.get_limit_name() == "" else url_encoder.encode(request.get_limit_name()))) + "",
            service=self.ENDPOINT,
            component=DeleteLimitRequest.Constant.MODULE,
            target_function=DeleteLimitRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_limit(self, request):
        """
        回数制限の一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_limit_client.control.DescribeLimitRequest.DescribeLimitRequest
        :return: 結果
        :rtype: gs2_limit_client.control.DescribeLimitResult.DescribeLimitResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_limit_client.control.DescribeLimitRequest import DescribeLimitRequest

        from gs2_limit_client.control.DescribeLimitResult import DescribeLimitResult
        return DescribeLimitResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/limit",
            service=self.ENDPOINT,
            component=DescribeLimitRequest.Constant.MODULE,
            target_function=DescribeLimitRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_limit(self, request):
        """
        回数制限を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_limit_client.control.GetLimitRequest.GetLimitRequest
        :return: 結果
        :rtype: gs2_limit_client.control.GetLimitResult.GetLimitResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_limit_client.control.GetLimitRequest import GetLimitRequest

        from gs2_limit_client.control.GetLimitResult import GetLimitResult
        return GetLimitResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/limit/" + str(("null" if request.get_limit_name() is None or request.get_limit_name() == "" else url_encoder.encode(request.get_limit_name()))) + "",
            service=self.ENDPOINT,
            component=GetLimitRequest.Constant.MODULE,
            target_function=GetLimitRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_limit_status(self, request):
        """
        回数制限の状態を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_limit_client.control.GetLimitStatusRequest.GetLimitStatusRequest
        :return: 結果
        :rtype: gs2_limit_client.control.GetLimitStatusResult.GetLimitStatusResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_limit_client.control.GetLimitStatusRequest import GetLimitStatusRequest

        from gs2_limit_client.control.GetLimitStatusResult import GetLimitStatusResult
        return GetLimitStatusResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/limit/" + str(("null" if request.get_limit_name() is None or request.get_limit_name() == "" else url_encoder.encode(request.get_limit_name()))) + "/status",
            service=self.ENDPOINT,
            component=GetLimitStatusRequest.Constant.MODULE,
            target_function=GetLimitStatusRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_limit(self, request):
        """
        回数制限を更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_limit_client.control.UpdateLimitRequest.UpdateLimitRequest
        :return: 結果
        :rtype: gs2_limit_client.control.UpdateLimitResult.UpdateLimitResult
        """
        body = { 
        }
        if request.get_description() is not None:
            body["description"] = request.get_description()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_limit_client.control.UpdateLimitRequest import UpdateLimitRequest
        from gs2_limit_client.control.UpdateLimitResult import UpdateLimitResult
        return UpdateLimitResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/limit/" + str(("null" if request.get_limit_name() is None or request.get_limit_name() == "" else url_encoder.encode(request.get_limit_name()))) + "",
            service=self.ENDPOINT,
            component=UpdateLimitRequest.Constant.MODULE,
            target_function=UpdateLimitRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def export_master(self, request):
        """
        カウンターマスターをエクスポートします<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_limit_client.control.ExportMasterRequest.ExportMasterRequest
        :return: 結果
        :rtype: gs2_limit_client.control.ExportMasterResult.ExportMasterResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_limit_client.control.ExportMasterRequest import ExportMasterRequest

        from gs2_limit_client.control.ExportMasterResult import ExportMasterResult
        return ExportMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/limit/" + str(("null" if request.get_limit_name() is None or request.get_limit_name() == "" else url_encoder.encode(request.get_limit_name()))) + "/master",
            service=self.ENDPOINT,
            component=ExportMasterRequest.Constant.MODULE,
            target_function=ExportMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))
