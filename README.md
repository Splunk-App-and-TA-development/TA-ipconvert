# TA-ipconvert

IP Format Convertion Scripted Lookup for Splunk

Install this app on your search head to provide a scripted lookup for converting IP addresses to and from an integer.

For example: | stats count | eval src_ip_int="3232235521" | lookup ipconvert integerfield AS src_ip_int OUTPUT stringfield AS src_ip

Further documentation is provided in the wiki here: https://github.com/doksu/TA-ipconvert/wiki
