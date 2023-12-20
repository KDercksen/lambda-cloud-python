#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import environ

import requests

from lambda_client import BASE_URL


def list_instance_types():
    url = BASE_URL + "instance-types"
    r = requests.get(
        url, headers={"Authorization": "Bearer " + environ["LAMBDA_API_KEY"]}
    )
    return {"status_code": r.status_code, "content": r.json()}


def list_running_instances():
    url = BASE_URL + "instances"
    r = requests.get(
        url, headers={"Authorization": "Bearer " + environ["LAMBDA_API_KEY"]}
    )
    return {"status_code": r.status_code, "content": r.json()}


def list_instance_details(instance_id):
    url = BASE_URL + f"instances/{instance_id}"
    r = requests.get(
        url, headers={"Authorization": "Bearer " + environ["LAMBDA_API_KEY"]}
    )
    return {"status_code": r.status_code, "content": r.json()}


def launch_instance(
    instance_type,
    region_name,
    ssh_key_name,
    file_system_names=None,
    quantity=1,
    name=None,
):
    url = BASE_URL + "instance-operations/launch"
    payload = {
        "instance_type_name": instance_type,
        "region_name": region_name,
        "ssh_key_names": [ssh_key_name],
        "file_system_names": [] if file_system_names is None else file_system_names,
        "quantity": quantity,
        "name": name,
    }
    r = requests.post(
        url,
        headers={"Authorization": "Bearer " + environ["LAMBDA_API_KEY"]},
        json=payload,
    )
    return {"status_code": r.status_code, "content": r.json()}


def terminate_instance(instance_ids):
    url = BASE_URL + "instance-operations/terminate"
    if isinstance(instance_ids, str):
        instance_ids = [instance_ids]
    payload = {"instance_ids": instance_ids}
    r = requests.post(
        url,
        headers={"Authorization": "Bearer " + environ["LAMBDA_API_KEY"]},
        json=payload,
    )
    return {"status_code": r.status_code, "content": r.json()}


def restart_instance(instance_ids):
    url = BASE_URL + "instance-operations/restart"
    if isinstance(instance_ids, str):
        instance_ids = [instance_ids]
    payload = {"instance_ids": instance_ids}
    r = requests.post(
        url,
        headers={"Authorization": "Bearer " + environ["LAMBDA_API_KEY"]},
        json=payload,
    )
    return {"status_code": r.status_code, "content": r.json()}


def list_ssh_keys():
    url = BASE_URL + "ssh-keys"
    r = requests.get(
        url, headers={"Authorization": "Bearer " + environ["LAMBDA_API_KEY"]}
    )
    return {"status_code": r.status_code, "content": r.json()}


def add_ssh_key(name, public_key):
    url = BASE_URL + "ssh-keys"
    payload = {"name": name, "public_key": public_key}
    r = requests.post(
        url,
        headers={"Authorization": "Bearer " + environ["LAMBDA_API_KEY"]},
        json=payload,
    )
    return {"status_code": r.status_code, "content": r.json()}


def delete_ssh_key(key_id):
    url = BASE_URL + f"ssh-keys/{key_id}"
    r = requests.delete(
        url, headers={"Authorization": "Bearer " + environ["LAMBDA_API_KEY"]}
    )
    return {"status_code": r.status_code, "content": r.json()}


def list_file_systems():
    url = BASE_URL + "file-systems"
    r = requests.get(
        url, headers={"Authorization": "Bearer " + environ["LAMBDA_API_KEY"]}
    )
    return {"status_code": r.status_code, "content": r.json()}
