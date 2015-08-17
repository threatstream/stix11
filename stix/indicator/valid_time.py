# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from stix.common import DateTimeWithPrecision
import stix.bindings.indicator as indicator_binding
from stix.base import ElementField

class ValidTime(stix.Entity):
    _namespace = "http://stix.mitre.org/Indicator-2"
    _binding = indicator_binding
    _binding_class = _binding.ValidTimeType
    
    start_time = ElementField("Start_Time", DateTimeWithPrecision)
    end_time = ElementField("End_Time", DateTimeWithPrecision)
    
    def __init__(self, start_time=None, end_time=None):
        self._fields = {}
        self.start_time = start_time
        self.end_time = end_time

