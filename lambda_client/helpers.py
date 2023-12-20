#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lambda_client import api


def list_available_instances():
    instance_types = api.list_instance_types()
    if instance_types["status_code"] != 200:
        print("Error: could not list instance types")
        return []

    results = []
    for name, metadata in instance_types["content"]["data"].items():
        if len(r := metadata["regions_with_capacity_available"]) > 0:
            results.append((name, [x["name"] for x in r]))
    return results
