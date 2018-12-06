%bcond_without check
%global goipath     github.com/mdlayher/genetlink
%global commit      76fecce4c787fb8eaa21a8755f722d67c53038e1

Version:            0

%global common_description %{expand:
Package genetlink implements generic netlink interactions and data types.
}

%gometa

Name:    %{goname}
Release: 0.2%{?dist}
Summary: Generic netlink interactions and data types
License: MIT
URL:     %{gourl}
Source:  %{gosource}
Patch0:   0001-skip-arch-dependent-test-on-s390x.patch

BuildRequires: golang(github.com/mdlayher/netlink)
BuildRequires: golang(github.com/mdlayher/netlink/nlenc)
BuildRequires: golang(golang.org/x/net/bpf)
BuildRequires: golang(golang.org/x/sys/unix)

%if %{with check}
BuildRequires: golang(github.com/google/go-cmp/cmp)
BuildRequires: golang(github.com/mdlayher/netlink/nltest)
%endif

%description
%{common_description}

%package   devel
Summary:   %{summary}
BuildArch: noarch

%description devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%gosetup -q
%patch0 -p1
rm -rf vendor

%install
%goinstall

%check
%if %{with check}
  %gochecks
%endif

%files devel -f devel.file-list
%license LICENSE.md
%doc *\.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git76fecce
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 15 2018 Paul Gier <pgier@redhat.com> - 0-0.1.20180515git76fecc
- First package for Fedora
