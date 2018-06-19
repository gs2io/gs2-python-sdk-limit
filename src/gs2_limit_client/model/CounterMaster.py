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


class CounterMaster(object):

    def __init__(self, params=None):
        if params is None:
            self.__counter_master_id = None
            self.__name = None
            self.__max = None
            self.__reset_type = None
            self.__reset_day_of_month = None
            self.__reset_day_of_week = None
            self.__reset_hour = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_counter_master_id(params['counterMasterId'] if 'counterMasterId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_max(params['max'] if 'max' in params.keys() else None)
            self.set_reset_type(params['resetType'] if 'resetType' in params.keys() else None)
            self.set_reset_day_of_month(params['resetDayOfMonth'] if 'resetDayOfMonth' in params.keys() else None)
            self.set_reset_day_of_week(params['resetDayOfWeek'] if 'resetDayOfWeek' in params.keys() else None)
            self.set_reset_hour(params['resetHour'] if 'resetHour' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)

    def get_counter_master_id(self):
        """
        カウンターマスターGRNを取得
        :return: カウンターマスターGRN
        :rtype: unicode
        """
        return self.__counter_master_id

    def set_counter_master_id(self, counter_master_id):
        """
        カウンターマスターGRNを設定
        :param counter_master_id: カウンターマスターGRN
        :type counter_master_id: unicode
        """
        self.__counter_master_id = counter_master_id

    def get_name(self):
        """
        カウンターマスター名を取得
        :return: カウンターマスター名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        カウンターマスター名を設定
        :param name: カウンターマスター名
        :type name: unicode
        """
        self.__name = name

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
        self.__max = max

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
        self.__reset_type = reset_type

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
        self.__reset_day_of_month = reset_day_of_month

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
        self.__reset_day_of_week = reset_day_of_week

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
        self.__reset_hour = reset_hour

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

    def get_update_at(self):
        """
        最終更新日時(エポック秒)を取得
        :return: 最終更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        最終更新日時(エポック秒)を設定
        :param update_at: 最終更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(CounterMaster, self).__getitem__(key)

    def to_dict(self):
        return {
            "counterMasterId": self.__counter_master_id,
            "name": self.__name,
            "max": self.__max,
            "resetType": self.__reset_type,
            "resetDayOfMonth": self.__reset_day_of_month,
            "resetDayOfWeek": self.__reset_day_of_week,
            "resetHour": self.__reset_hour,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }
