#!/bin/bash
set -e
set -x

echo "%define version 1.0.0" > dependency.spec
cat package/similar.spec >> dependency.spec
yum-builddep dependency.spec
/bin/rm dependency.spec