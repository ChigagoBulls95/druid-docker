#!/bin/bash

ip addr | grep 'eth0' | awk '{print $2}' | cut -f1  -d'/' | tail -1