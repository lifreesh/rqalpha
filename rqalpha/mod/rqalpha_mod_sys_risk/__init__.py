# -*- coding: utf-8 -*-
#
# Copyright 2019 Ricequant, Inc
#
# * Commercial Usage: please contact public@ricequant.com
# * Non-Commercial Usage:
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.


import click
from rqalpha import cli

__config__ = {
    # 检查限价单价格是否合法
    "validate_price": True,
    # 检查标的证券是否可以交易
    "validate_is_trading": True,
    # 检查可用资金是否充足
    "validate_cash": True,
    # 检查股票可平仓位是否充足
    "validate_stock_position": True,
    # 检查期货可平仓位是否充足
    "validate_future_position": True,
    # 检查是否存在自成交的风险
    "validate_self_trade": False,
}


def load_mod():
    from .mod import RiskManagerMod
    return RiskManagerMod()


"""
注入 --short-stock option
可以通过 `rqalpha run --short-stock` 来开启允许股票卖空
"""
cli_prefix = "mod__sys_risk__"

cli.commands['run'].params.append(
    click.Option(
        ("--no-short-stock/--short-stock", "mod__sys_risk__validate_stock_position"),
        is_flag=True, default=True,
        help="[sys_risk] enable stock shorting"
    )
)


cli.commands["run"].params.append(
    click.Option(
        ("--cash-validation/--no-cash-validation", "mod__sys_risk__validate_cash"),
        is_flag=True, default=True,
        help="[sys_risk] enable cash validation"
    )
)
