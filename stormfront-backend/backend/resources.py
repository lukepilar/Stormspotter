"""Contains all node lables and relationship type mappings"""
# NODE_LABELS

AADAPP_NODE_LABEL = "AADApplication"
AADGROUP_NODE_LABEL = "AADGroup"
AADOBJECT_NODE_LABEL = "AADObject"
AADSPN_NODE_LABEL = "AADServicePrincipal"
AADUSER_NODE_LABEL = "AADUser"
AVAILABILITYSET_NODE_LABEL = "AvailabilitySet"
BACKENDPOOL_NODE_LABEL = "Pool"
CERTIFICATE_NODE_LABEL = "Certificate"
DISK_NODE_LABEL = "Disk"
ENDPOINT_NODE_LABEL = "Endpoint"
GENERIC_NODE_LABEL = "AzureResource"
HOSTEDSERVICEROLE_NODE_LABEL = "HostedServiceRole"
HOSTEDSERVICE_NODE_LABEL = "HostedService"
IPCONFIG_NODE_LABEL = "IpConfiguration"
KEYVAULT_NODE_LABEL = "KeyVault"
LOADBALANCER_NODE_LABEL = "LoadBalancer"
NETWORKINTERFACE_NODE_LABEL = "NetworkInterface"
NSG_NODE_LABEL = "NetworkSecurityGroup"
PUBLIC_IP_NODE_LABEL = "PublicIp"
RESOURCEGROUP_NODE_LABEL = "ResourceGroup"
RULE_NODE_LABEL = "Rule"
SERVERFARM_NODE_LABEL = "ServerFarm"
SERVICEBUSNAMESPACE_NODE_LABEL = "ServiceBusNamespace"
SERVICEFABRIC_NODE_LABEL = "ServiceFabric"
SQLDATABASE_NODE_LABEL = "SQLDatabase"
SQLSERVER_NODE_LABEL = "SQLServer"
STORAGEACCOUNT_NODE_LABEL = "StorageAccount"
SUBSCRIPTION_NODE_LABEL = "Subscription"
TENANT_NODE_LABEL = "Tenant"
VIRTUALMACHINE_NODE_LABEL = "VirtualMachine"
VIRTUALNETWORK_NODE_LABEL = "VirtualNetwork"
VMSS_NODE_LABEL = "VMSS"
WEBSITE_NODE_LABEL = "WebSite"

# RELATIONSHIP TYPES
APP_TO_SPN = "Instantiates"
ASSET_TO_CERT = "CanExtractCert"
ASSET_TO_ENDPOINT_OR_IP = "Exposes"
ASSET_TO_HSROLE = "ServerRole"
ASSET_TO_MANAGED = "Manages"
ASSET_TO_VNET = "ConnectedTo"
ATTACHED_TO_ASSET = "Attached"
CERT_TO_ASSET = "Admin"
DEFAULT_REL = "Contains"
IPCONFIG_TO_NIC = "HasConfig"
NIC_TO_NSG = "Uses"
OWNER = "Owner"
SUB_TO_ASSET = "Hosts"
USER_TO_GROUP = "MemberOf"
HAS_PERMISSIONS = "Permissions"
HAS_RBAC = "HasRbac"
