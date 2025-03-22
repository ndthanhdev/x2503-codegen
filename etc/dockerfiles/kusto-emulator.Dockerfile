FROM mcr.microsoft.com/azuredataexplorer/kustainer-linux:latest


ENV PUID=1000
ENV PGID=1000

# install shadow-utils
RUN tdnf install -y shadow-utils

# add user abc and group abc
RUN groupadd -g 1000 abc && useradd -u 1000 -g abc abc

# add root to abc group
RUN usermod -aG abc root

# chmod /kusto
RUN chmod -R 777 /kusto

USER abc