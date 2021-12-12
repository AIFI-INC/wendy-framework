#!/bin/bash
az group create -g ${RG} -l eastus
az deployment group create \
    --resource-group ${RG} \
    --template-file templates/arm/develop.json \
    --parameters "{\"siteName\": \"${SITENAME}\", \"imageName\": \"${IMAGENAME}\", \"administratorLogin\": \"${MYSQL_USERNAME}\", \"administratorLoginPassword\": \"${MYSQL_PASSWORD}\"}"
      