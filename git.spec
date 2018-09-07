%global __os_install_post %{nil}
%global _enable_debug_package 0
%global debug_package %{nil}

# CentOS 7 would force ".el7.centos", we want to avoid that.
%if 0%{?rhel} == 7
  %define dist .el7
%endif

%define version 2.18.0

Name: git
Summary: Git core and tools
Version: %{version}
Release: 1%{?dist}
License: GPL
Group: Development/Tools
Source: https://github.com/git/git/archive/v%{version}.tar.gz
URL: http://git-scm.com/
Distribution: RHEL6
Vendor: Red Hat

%description
fast, scalable, distributed revision control system Git is popular version
control system designed to handle very large projects with speed and
efficiency; it is used for many high profile open source projects, most notably
the Linux kernel.

Git falls in the category of distributed source code management tools.  Every
Git working directory is a full-fledged repository with full revision tracking
capabilities, not dependent on network access or a central server.

This package provides the git main components with minimal dependencies.
Additional functionality, e.g. a graphical user interface and revision tree
visualizer, tools for interoperating with other VCS's, or a web interface, is
provided as separate git* packages.

%prep
%autosetup

%build
make configure
%configure --prefix=/usr
make all man

%install
make install install-man DESTDIR=%{buildroot}
%{__rm} -rf %{buildroot}%{_datadir}/locale/*

%files
%defattr(-,root,root)
%doc %{_mandir}/man1/*.1*
%doc %{_mandir}/man3/*.3*
%doc %{_mandir}/man5/*.5*
%doc %{_mandir}/man7/*.7*
%{_bindir}/git*
%{_libexecdir}/git-core/
%{_datadir}/git-core/
%{_datadir}/git-gui/
%{_datadir}/gitk/
%{_datadir}/gitweb
%{_datadir}/perl5/FromCPAN
%{_datadir}/perl5/Git.pm
%{_datadir}/perl5/Git
