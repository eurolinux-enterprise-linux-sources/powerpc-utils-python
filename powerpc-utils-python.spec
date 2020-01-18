%global debug_package %{nil}

Name:           powerpc-utils-python
Version:        1.2.1
Release:        3%{?dist}
Summary:        Python utilities for PowerPC platforms

Group:          System Environment/Base
License:        CPL
URL:            http://sourceforge.net/projects/powerpc-utils
Source0:        http://sourceforge.net/projects/powerpc-utils/files/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  python-devel
Requires:       pygtk2 >= 2.0

ExclusiveArch:  ppc ppc64

%description
Python based utilities for maintaining and servicing PowerPC systems.

%prep
%setup -q

%build
make 

%install
make install DESTDIR=%{buildroot} FILES=""

%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/amsvis
%dir %{python_sitelib}/powerpcAMS
%{python_sitelib}/powerpcAMS/*.py
%{python_sitelib}/powerpcAMS/*.py[co]
%{python_sitelib}/powerpcAMS-%{version}-py*.egg-info
%{_mandir}/man1/amsvis.1*
%doc README COPYRIGHT

%changelog
* Thu Nov 22 2012 Filip Kocina <fkocina@redhat.com> - 1.2.1-3
- %% doubled in the spec file

* Wed Aug 29 2012 Lukas Nykryn <lnykryn@redhat.com> - 1.2.1-2
- use %%global instead of %%define

* Mon Jun 11 2012 Lukáš Nykrýn <lnykryn@redhat.com> - 1.2.1-1
- New package

