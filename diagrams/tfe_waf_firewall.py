from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.network import ElasticLoadBalancing
from diagrams.onprem.compute import Server
from diagrams.aws.storage import SimpleStorageServiceS3Bucket
from diagrams.aws.database import RDSPostgresqlInstance
from diagrams.aws.general import GenericFirewall
from diagrams.onprem.network import Haproxy 


# Variables
title = "Client connection to TFE"
outformat = "png"
filename = "tfe_waf_firewall"
direction = "TB"


with Diagram(
    name=title,
    direction=direction,
    filename=filename,
    outformat=outformat,
) as diag:
    # Non Clustered
    user = Server("user")

    bucket_tfe = SimpleStorageServiceS3Bucket("TFE bucket")
    ec2_tfe_server = EC2("TFE_server")
    postgresql = RDSPostgresqlInstance("RDS Instance")
    firewall = GenericFirewall("Firewall/WAF")
    loadbalancer = ElasticLoadBalancing("loadbalancer")
    proxy = Haproxy("Proxy server")
 
    user >> proxy >> firewall >> loadbalancer >> ec2_tfe_server >> [postgresql,
                       bucket_tfe]

diag