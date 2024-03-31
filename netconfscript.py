from ncclient import manager

a = manager.connect(host="192.168.45.131",port="830",username="admin",password="123",hostkey_verify=False)
config = """<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>loobpack0</name>
            <enabled>true</enabled>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip>192.0.0.1</ip>
                    <netmask>255.255.255.0</netmask>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</config>"""

response = a.edit_config(config, target="running")

#or capability in a.server_capabilities:
    #print(capability)
#config= a.get_config(source="running")
#print(config)