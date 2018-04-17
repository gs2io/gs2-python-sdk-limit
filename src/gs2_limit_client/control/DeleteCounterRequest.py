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


class DeleteCounterRequest(Gs2BasicRequest):

    class Constant(Gs2Limit):
        FUNCTION = "DeleteCounter"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(DeleteCounterRequest, self).__init__(params)
        if params is None:
            self.__limit_name = None
        else:
            self.set_limit_name(params['limitName'] if 'limitName' in params.keys() else None)
        if params is None:
            self.__user_id = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
        if params is None:
            self.__counter_name = None
        else:
            self.set_counter_name(params['counterName'] if 'counterName' in params.keys() else None)

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
        if limit_name and not (isinstance(limit_name, str) or isinstance(limit_name, unicode)):
            raise TypeError(type(limit_name))
        self.__limit_name = limit_name

    def with_limit_name(self, limit_name):
        """
        回数制限の名前を指定します。を設定
        :param limit_name: 回数制限の名前を指定します。
        :type limit_name: unicode
        :return: this
        :rtype: DeleteCounterRequest
        """
        self.set_limit_name(limit_name)
        return self

    def get_user_id(self):
        """
        ユーザIDを指定します。を取得
        :return: ユーザIDを指定します。
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        ユーザIDを指定します。を設定
        :param user_id: ユーザIDを指定します。
        :type user_id: unicode
        """
        if user_id and not (isinstance(user_id, str) or isinstance(user_id, unicode)):
            raise TypeError(type(user_id))
        self.__user_id = user_id

    def with_user_id(self, user_id):
        """
        ユーザIDを指定します。を設定
        :param user_id: ユーザIDを指定します。
        :type user_id: unicode
        :return: this
        :rtype: DeleteCounterRequest
        """
        self.set_user_id(user_id)
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
        if counter_name and not (isinstance(counter_name, str) or isinstance(counter_name, unicode)):
            raise TypeError(type(counter_name))
        self.__counter_name = counter_name

    def with_counter_name(self, counter_name):
        """
        カウンター名を指定します。を設定
        :param counter_name: カウンター名を指定します。
        :type counter_name: unicode
        :return: this
        :rtype: DeleteCounterRequest
        """
        self.set_counter_name(counter_name)
        return self
