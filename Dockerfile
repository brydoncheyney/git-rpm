FROM centos:6
RUN yum -y install epel-release
RUN yum -y install rpm-build rpmdevtools redhat-rpm-config rpmlint yum-utils
RUN yum -y groupinstall "Development Tools" --exclude=git subversion
RUN yum -y install openssl-devel curl-devel expat-devel perl-ExtUtils-MakeMaker
RUN yum -y install asciidoc xmlto

# Create RPM Build Environment
RUN rpmdev-setuptree

COPY ./build_rpm.sh /
RUN chmod +x ./build_rpm.sh
VOLUME /spec_src
ENTRYPOINT ["/build_rpm.sh"]
