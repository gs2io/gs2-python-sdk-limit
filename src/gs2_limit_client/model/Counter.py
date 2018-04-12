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


class Counter(object):

    def __init__(self, params=None):
        if params is None:
            self.__user_id = None
            self.__counter_name = None
            self.__count = None
            self.__next_reset_at = None
            self.__count_at = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
            self.set_counter_name(params['counterName'] if 'counterName' in params.keys() else None)
            self.set_count(params['count'] if 'count' in params.keys() else None)
            self.set_next_reset_at(params['nextResetAt'] if 'nextResetAt' in params.keys() else None)
            self.set_count_at(params['countAt'] if 'countAt' in params.keys() else None)

    def get_user_id(self):
        """
        ユーザIDを取得
        :return: ユーザID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        ユーザIDを設定
        :param user_id: ユーザID
        :type user_id: unicode
        """
        self.__user_id = user_id

    def get_counter_name(self):
        """
        カウンター名を取得
        :return: カウンター名
        :rtype: unicode
        """
        return self.__counter_name

    def set_counter_name(self, counter_name):
        """
        カウンター名を設定
        :param counter_name: カウンター名
        :type counter_name: unicode
        """
        self.__counter_name = counter_name

    def get_count(self):
        """
        カウント値を取得
        :return: カウント値
        :rtype: int
        """
        return self.__count

    def set_count(self, count):
        """
        カウント値を設定
        :param count: カウント値
        :type count: int
        """
        self.__count = count

    def get_next_reset_at(self):
        """
        次回リセット日時(エポック秒)を取得
        :return: 次回リセット日時(エポック秒)
        :rtype: int
        """
        return self.__next_reset_at

    def set_next_reset_at(self, next_reset_at):
        """
        次回リセット日時(エポック秒)を設定
        :param next_reset_at: 次回リセット日時(エポック秒)
        :type next_reset_at: int
        """
        self.__next_reset_at = next_reset_at

    def get_count_at(self):
        """
        最後にカウンターを進めた時間(エポック秒)を取得
        :return: 最後にカウンターを進めた時間(エポック秒)
        :rtype: int
        """
        return self.__count_at

    def set_count_at(self, count_at):
        """
        最後にカウンターを進めた時間(エポック秒)を設定
        :param count_at: 最後にカウンターを進めた時間(エポック秒)
        :type count_at: int
        """
        self.__count_at = count_at

    def to_dict(self):
        return {
            "userId": self.__user_id,
            "counterName": self.__counter_name,
            "count": self.__count,
            "nextResetAt": self.__next_reset_at,
            "countAt": self.__count_at,
        }
