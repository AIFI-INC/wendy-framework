#!/bin/bash
az group create -g ${RG} -l eastus
az deployment group create \
    --resource-group ${RG} \
    --template-file templates/arm/wendy.json \
    --parameters templates/arm/wendy.parameters.json
      