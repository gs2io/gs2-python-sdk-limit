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


class UpdateLimitRequest(Gs2BasicRequest):

    class Constant(Gs2Limit):
        FUNCTION = "UpdateLimit"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(UpdateLimitRequest, self).__init__(params)
        if params is None:
            self.__limit_name = None
        else:
            self.set_limit_name(params['limitName'] if 'limitName' in params.keys() else None)
        if params is None:
            self.__description = None
        else:
            self.set_description(params['description'] if 'description' in params.keys() else None)

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
        :rtype: UpdateLimitRequest
        """
        self.set_limit_name(limit_name)
        return self

    def get_description(self):
        """
        説明文を取得
        :return: 説明文
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        """
        if not isinstance(description, unicode):
            raise TypeError(type(description))
        self.__description = description

    def with_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        :return: this
        :rtype: UpdateLimitRequest
        """
        self.set_description(description)
        return self
