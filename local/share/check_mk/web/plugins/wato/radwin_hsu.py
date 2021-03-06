#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
#
# Plugin for monitoring Radwin Base Station 5000 series
#
# Date: 2022-01-28
#
# Author: Wojciech Repiński
# email: wrepinski@gmail
#

from cmk.gui.i18n import _

from cmk.gui.valuespec import (
    Dictionary,
    Integer,
    Tuple,
    TextAscii,
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersOperatingSystem,
)

def _item_valuespec_radwin_hsu():
      return TextAscii(title=_("Radwin HSU"))

def _parameter_valuespec_radwin_hsu():
    return Transform(
        Dictionary(
            title=_('Radwin HSU  Signal Params'),
            elements=[
                ('rss_hbs', Tuple(
                    title=_('HBS Rx Signal'),
                    elements=[
                        Float(title=_('Warning at'), unit='dBm',
                              default_value='-65',
                              ),
                        Float(title=_('Critical at'), unit='dBm',
                              default_value='-70',
                              ),
                    ],)),
                ('rss_hsu', Tuple(
                    title=_('HSU Rx Signal'),
                    elements=[
                        Float(title=_('Warning at'), unit='dBm',
                              default_value='-65',
                              ),
                        Float(title=_('Critical at'), unit='dBm',
                              default_value='-70',
                              ),
                    ],)),
            ],
        ),
    )


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="radwin_hsu",
        group=RulespecGroupCheckParametersNetworking,
        match_type="dict",
        item_spec=_item_valuespec_radwin_hsu,
        parameter_valuespec=_parameter_valuespec_radwin_hsu,
        title=lambda: _("Radwin HSU"),
    )
)
