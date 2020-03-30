# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix111.mixbox import entities, fields

import stix111.cybox.bindings.dns_query_object as dns_query_binding
from stix111.cybox.common import DateTime, ObjectProperties, String, HexBinary
from stix111.cybox.objects.uri_object import URI
from stix111.cybox.objects.dns_record_object import DNSRecord


class DNSResourceRecords(entities.EntityList):
    _binding = dns_query_binding
    _binding_class = dns_query_binding.DNSResourceRecordsType
    _namespace = "http://cybox.mitre.org/objects#DNSQueryObject-2"
    resource_record = fields.TypedField("Resource_Record", DNSRecord, multiple=True)


class DNSQuestion(entities.Entity):
    _namespace = "http://cybox.mitre.org/objects#DNSQueryObject-2"
    _binding = dns_query_binding
    _binding_class = dns_query_binding.DNSQuestionType

    qname = fields.TypedField("QName", URI)
    qtype = fields.TypedField("QType", String)
    qclass = fields.TypedField("QClass", String)


class DNSQuery(ObjectProperties):
    _binding = dns_query_binding
    _binding_class = dns_query_binding.DNSQueryObjectType
    _namespace = "http://cybox.mitre.org/objects#DNSQueryObject-2"
    _XSI_NS = "DNSQueryObj"
    _XSI_TYPE = "DNSQueryObjectType"

    successful = fields.TypedField("successful")
    transaction_id = fields.TypedField("Transaction_ID", HexBinary)
    question = fields.TypedField("Question", DNSQuestion)
    answer_resource_records = fields.TypedField("Answer_Resource_Records", DNSResourceRecords)
    authority_resource_records = fields.TypedField("Authority_Resource_Records", DNSResourceRecords)
    additional_records = fields.TypedField("Additional_Records", DNSResourceRecords)
    date_ran = fields.TypedField("Date_Ran", DateTime)
    service_used = fields.TypedField("Service_Used", String)