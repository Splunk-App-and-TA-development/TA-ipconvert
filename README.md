# TA-ipconvert

IP Format Conversion Scripted Lookup for Splunk

Splunk's built-in eval command can be used to perform IP address format conversion, however it's a complex and messy process that doesn't lend itself well to the mapping of IP address fields to the Common Information Model (CIM). This app provides an 'ipconvert' scripted lookup for converting IP addresses to and from an integer. With this app installed on the search head you can create a props.conf stanza to automatically convert an integer format IP address to a CIM-normalised string IP address field:

LOOKUP-example_src_ip = ipconvert integerfield AS ip_src OUTPUT stringfield AS src_ip

The lookup can also be used in-line with SPL. For example:

| stats count | eval src_ip_int="3232235521" | lookup ipconvert integerfield AS src_ip_int OUTPUT stringfield AS src_ip

Further documentation is provided in the wiki here: https://github.com/doksu/TA-ipconvert/wiki
