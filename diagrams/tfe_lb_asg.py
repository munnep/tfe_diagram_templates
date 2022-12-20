#!/usr/bin/env python3

from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import ECS, AutoScaling
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.aws.storage import S3

with Diagram("tfe_lb_asg", show=False, direction="TB"):
    with Cluster("VPC"):
        dns = Route53("dns")
        lb = ELB("lb")
        with Cluster("ASG"):
            asg_group = AutoScaling("ec2")

        dns >> lb >> asg_group

        with Cluster("S3"):
            asg_group << S3("asset")
            asg_group >> S3("storage")
            asg_group >> Edge(color="darkgreen", style="dashed") >> S3("snapshot")

        with Cluster("DB HA"):
            master = RDS("psql")
            asg_group >> master

            master - Edge(color="brown", style="dotted") - RDS("psql")
