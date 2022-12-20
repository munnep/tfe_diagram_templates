#!/usr/bin/env python3

from diagrams import Cluster, Diagram
from diagrams.aws.database import RDS
from diagrams.aws.network import Route53
from diagrams.aws.storage import S3
from diagrams.aws.compute import EC2
from diagrams.aws.storage import ElasticBlockStoreEBSVolume
from diagrams.aws.storage import ElasticBlockStoreEBSSnapshot

with Diagram("tfe_simple_md", show=False, direction="TB"):
    with Cluster("Cloud"):
        dns = Route53("dns")
        with Cluster("VPC"):
            (
                dns
                >> EC2("TFE")
                >> ElasticBlockStoreEBSVolume("Disk")
                >> [
                    S3("storage"),
                    RDS("psql"),
                    ElasticBlockStoreEBSSnapshot("DiskSnapshot"),
                ]
            )
