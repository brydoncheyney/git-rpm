%global __os_install_post %{nil}
%global _enable_debug_package 0
%global debug_package %{nil}

Name: git
Summary: Git core and tools
Version: 2.11.1
Release: 1
License: GPL
Group: Development/Tools
Source: https://github.com/git/git/archive/v2.11.1.tar.gz
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

%files
%defattr(-,root,root)
/usr/*
