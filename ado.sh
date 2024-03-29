#!/usr/bin/env bash

set -o pipefail -eux

declare -a args

command -v python

command -v pip3
pip3 --version
pip3 list --disable-pip-version-check

export PATH="${PWD}/bin:${PATH}"
export PYTHONIOENCODING="UTF-8"
export LC_ALL="en_US.utf-8"

#pip3 install virtualenv
#ls /usr/bin/
#ls /usr/bin/python3/
#ls /usr/bin/python3.6/
#virtualenv --python /usr/bin/python3.6/ansible-venv

#set +ux
#. ~/ansible-venv/bin/activate
#set -ux

pip3 install ansible=="2.9.0" --disable-pip-version-check

TEST_DIR="${HOME}/.ansible/ansible_collections/azure/azcollection"
mkdir -p "${TEST_DIR}"
cp -aT "${SHIPPABLE_BUILD_DIR}" "${TEST_DIR}"

pip3 install  -I -r "${TEST_DIR}/requirements-azure.txt"

timeout=60

cat <<EOF >> "${TEST_DIR}"/tests/integration/cloud-config-azure.ini
[default]
AZURE_CLIENT_ID:${AZURE_CLIENT_ID}
AZURE_SECRET:${AZURE_SECRET}
AZURE_SUBSCRIPTION_ID:${AZURE_SUBSCRIPTION_ID}
AZURE_TENANT:${AZURE_TENANT}
SHIPPABLE_BUILD_DIR: $(Build.Repository.LocalPath)
EOF

ansible-playbook delete_rg.yml -vvv
