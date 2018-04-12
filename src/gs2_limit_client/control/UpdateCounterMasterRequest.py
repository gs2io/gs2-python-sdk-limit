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

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_limit_client.Gs2Limit import Gs2Limit


class UpdateCounterMasterRequest(Gs2BasicRequest):

    class Constant(Gs2Limit):
        FUNCTION = "UpdateCounterMaster"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(UpdateCounterMasterRequest, self).__init__(params)
        if params is None:
            self.__limit_name = None
        else:
            self.set_limit_name(params['limitName'] if 'limitName' in params.keys() else None)
        if params is None:
            self.__counter_name = None
        else:
            self.set_counter_name(params['counterName'] if 'counterName' in params.keys() else None)
        if params is None:
            self.__max = None
        else:
            self.set_max(params['max'] if 'max' in params.keys() else None)
        if params is None:
            self.__reset_type = None
        else:
            self.set_reset_type(params['resetType'] if 'resetType' in params.keys() else None)
        if params is None:
            self.__reset_day_of_month = None
        else:
            self.set_reset_day_of_month(params['resetDayOfMonth'] if 'resetDayOfMonth' in params.keys() else None)
        if params is None:
            self.__reset_day_of_week = None
        else:
            self.set_reset_day_of_week(params['resetDayOfWeek'] if 'resetDayOfWeek' in params.keys() else None)
        if params is None:
            self.__reset_hour = None
        else:
            self.set_reset_hour(params['resetHour'] if 'resetHour' in params.keys() else None)

    def get_limit_name(self):
        """
        回数制限の名前を指定します。を取得
        :return: 回数制限の名前を指定します。
        :rtype: unicode
        """
        return self.__limit_name

    def set_limit_name(self, limit_name):
        """
        回数制限の名前を指定します。を設定
        :param limit_name: 回数制限の名前を指定します。
        :type limit_name: unicode
        """
        if not isinstance(limit_name, unicode):
            raise TypeError(type(limit_name))
        self.__limit_name = limit_name

    def with_limit_name(self, limit_name):
        """
        回数制限の名前を指定します。を設定
        :param limit_name: 回数制限の名前を指定します。
        :type limit_name: unicode
        :return: this
        :rtype: UpdateCounterMasterRequest
        """
        self.set_limit_name(limit_name)
        return self

    def get_counter_name(self):
        """
        カウンター名を指定します。を取得
        :return: カウンター名を指定します。
        :rtype: unicode
        """
        return self.__counter_name

    def set_counter_name(self, counter_name):
        """
        カウンター名を指定します。を設定
        :param counter_name: カウンター名を指定します。
        :type counter_name: unicode
        """
        if not isinstance(counter_name, unicode):
            raise TypeError(type(counter_name))
        self.__counter_name = counter_name

    def with_counter_name(self, counter_name):
        """
        カウンター名を指定します。を設定
        :param counter_name: カウンター名を指定します。
        :type counter_name: unicode
        :return: this
        :rtype: UpdateCounterMasterRequest
        """
        self.set_counter_name(counter_name)
        return self

    def get_max(self):
        """
        カウンターの最大値を取得
        :return: カウンターの最大値
        :rtype: int
        """
        return self.__max

    def set_max(self, max):
        """
        カウンターの最大値を設定
        :param max: カウンターの最大値
        :type max: int
        """
        if not isinstance(max, int):
            raise TypeError(type(max))
        self.__max = max

    def with_max(self, max):
        """
        カウンターの最大値を設定
        :param max: カウンターの最大値
        :type max: int
        :return: this
        :rtype: UpdateCounterMasterRequest
        """
        self.set_max(max)
        return self

    def get_reset_type(self):
        """
        リセット周期を取得
        :return: リセット周期
        :rtype: unicode
        """
        return self.__reset_type

    def set_reset_type(self, reset_type):
        """
        リセット周期を設定
        :param reset_type: リセット周期
        :type reset_type: unicode
        """
        if not isinstance(reset_type, unicode):
            raise TypeError(type(reset_type))
        self.__reset_type = reset_type

    def with_reset_type(self, reset_type):
        """
        リセット周期を設定
        :param reset_type: リセット周期
        :type reset_type: unicode
        :return: this
        :rtype: UpdateCounterMasterRequest
        """
        self.set_reset_type(reset_type)
        return self

    def get_reset_day_of_month(self):
        """
        期間内の取得量をリセットする日にちを取得
        :return: 期間内の取得量をリセットする日にち
        :rtype: int
        """
        return self.__reset_day_of_month

    def set_reset_day_of_month(self, reset_day_of_month):
        """
        期間内の取得量をリセットする日にちを設定
        :param reset_day_of_month: 期間内の取得量をリセットする日にち
        :type reset_day_of_month: int
        """
        if not isinstance(reset_day_of_month, int):
            raise TypeError(type(reset_day_of_month))
        self.__reset_day_of_month = reset_day_of_month

    def with_reset_day_of_month(self, reset_day_of_month):
        """
        期間内の取得量をリセットする日にちを設定
        :param reset_day_of_month: 期間内の取得量をリセットする日にち
        :type reset_day_of_month: int
        :return: this
        :rtype: UpdateCounterMasterRequest
        """
        self.set_reset_day_of_month(reset_day_of_month)
        return self

    def get_reset_day_of_week(self):
        """
        期間内の取得量をリセットする曜日を取得
        :return: 期間内の取得量をリセットする曜日
        :rtype: unicode
        """
        return self.__reset_day_of_week

    def set_reset_day_of_week(self, reset_day_of_week):
        """
        期間内の取得量をリセットする曜日を設定
        :param reset_day_of_week: 期間内の取得量をリセットする曜日
        :type reset_day_of_week: unicode
        """
        if not isinstance(reset_day_of_week, unicode):
            raise TypeError(type(reset_day_of_week))
        self.__reset_day_of_week = reset_day_of_week

    def with_reset_day_of_week(self, reset_day_of_week):
        """
        期間内の取得量をリセットする曜日を設定
        :param reset_day_of_week: 期間内の取得量をリセットする曜日
        :type reset_day_of_week: unicode
        :return: this
        :rtype: UpdateCounterMasterRequest
        """
        self.set_reset_day_of_week(reset_day_of_week)
        return self

    def get_reset_hour(self):
        """
        期間内の取得量をリセットする時を取得
        :return: 期間内の取得量をリセットする時
        :rtype: int
        """
        return self.__reset_hour

    def set_reset_hour(self, reset_hour):
        """
        期間内の取得量をリセットする時を設定
        :param reset_hour: 期間内の取得量をリセットする時
        :type reset_hour: int
        """
        if not isinstance(reset_hour, int):
            raise TypeError(type(reset_hour))
        self.__reset_hour = reset_hour

    def with_reset_hour(self, reset_hour):
        """
        期間内の取得量をリセットする時を設定
        :param reset_hour: 期間内の取得量をリセットする時
        :type reset_hour: int
        :return: this
        :rtype: UpdateCounterMasterRequest
        """
        self.set_reset_hour(reset_hour)
        return self
