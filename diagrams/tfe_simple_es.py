#!/usr/bin/env python3

from diagrams import Cluster, Diagram
from diagrams.aws.database import RDS
from diagrams.aws.network import Route53
from diagrams.aws.storage import S3
from diagrams.aws.compute import EC2

with Diagram("tfe_simple_es", show=False, direction="TB"):
    with Cluster("Cloud"):
        dns = Route53("dns")
        with Cluster("VPC"):

            dns >> EC2("TFE") >> [ S3("storage"), RDS("psql") ]