#!/usr/bin/env bash

set -e

SPEC_FILE_NAME=$1

cd /root/rpmbuild

# copy spec file into generic location
cp /spec_src/${SPEC_FILE_NAME} /root/rpmbuild/SPECS/build.spec

# lint the spec file
rpmlint --verbose SPECS/build.spec

# fetch sources
spectool -g -R SPECS/build.spec

# install build dependencies
yum-builddep -y SPECS/build.spec

# build the binary package
rpmbuild -bb SPECS/build.spec

cp -aR RPMS /spec_src
