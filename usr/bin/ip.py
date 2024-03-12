#!/usr/bin/env python3
# Script by Yono Irenk (Kartolo)
# Keluarga EDY
# Youtube Aryo Brokolly

from argparse import ArgumentParser
from huawei_lte_api.Connection import Connection
from huawei_lte_api.Client import Client

parser = ArgumentParser()
parser.add_argument('url', type=str)
parser.add_argument('--username', type=str)
parser.add_argument('--password', type=str)
args = parser.parse_args()

with Connection(args.url, username=args.username, password=args.password) as connection:
    client = Client(connection)
    wan_ip_address = client.device.information()['WanIPAddress']
    print(f'IP: {wan_ip_address}')
