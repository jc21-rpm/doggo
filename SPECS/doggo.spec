%define debug_package %{nil}

Name:           doggo
Version:        1.1.5
Release:        1%{?dist}
Summary:        Command-line DNS Client for Humans. Written in Golang
Group:          Applications/System
License:        GPL3
URL:            https://doggo.mrkaran.dev/
Source:         https://github.com/mr-karan/%{name}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  golang

%description
doggo is a modern command-line DNS client (like dig) written in Golang. It outputs
information in a neat concise manner and supports protocols like DoH, DoT, DoQ, and
DNSCrypt as well.

%prep
%setup -q -n %{name}-%{version}

%build
make build-cli

%install
install -Dm0755 %{_builddir}/%{name}-%{version}/bin/%{name}.bin %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Wed Feb 5 2026 Jamie Curnow <jc@jc21.com> 1.1.5-1
- https://github.com/mr-karan/doggo/releases/tag/v1.1.5

* Fri Feb 6 2026 Jamie Curnow <jc@jc21.com> 1.1.4-1
- https://github.com/mr-karan/doggo/releases/tag/v1.1.4
