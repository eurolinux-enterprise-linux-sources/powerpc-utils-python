%global debug_package %{nil}

Name:           powerpc-utils-python
Version:        1.2.1
Release:        7%{?dist}
Summary:        Python utilities for PowerPC platforms
Group:          System Environment/Base
License:        CPL
URL:            http://sourceforge.net/projects/powerpc-utils

Source0:        http://sourceforge.net/projects/powerpc-utils/files/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-devel
Requires:       pygtk2 >= 2.0


%description
Python based utilities for maintaining and servicing PowerPC systems.

%prep
%setup -q


%build
make


%install
make install DESTDIR=%{buildroot} FILES=""


%files
%attr(755,root,root) %{_bindir}/amsvis
%dir %{python_sitelib}/powerpcAMS
%{python_sitelib}/powerpcAMS/*.py
%{python_sitelib}/powerpcAMS/*.py[co]
%{python_sitelib}/powerpcAMS-%{version}-py*.egg-info
%{_mandir}/man1/amsvis.1*
%doc README COPYRIGHT


%changelog
* Tue Feb 11 2014 Jaromir Capik <jcapik@redhat.com> - 1.2.1-7
- ExclusiveArch was not much helpful - removing again
- Related: rhbz#1061054

* Tue Feb 11 2014 Jaromir Capik <jcapik@redhat.com> - 1.2.1-6
- Re-introducing ExclusiveArch
- Related: rhbz#1061054

* Mon Feb 10 2014 Jaromir Capik <jcapik@redhat.com> - 1.2.1-5
- Building as noarch (#1061054)
- Resolves: rhbz#1061054

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.2.1-4
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 29 2012 Lukas Nykryn <lnykryn@redhat.com> - 1.2.1-2
- use %%global instead of %%define

* Mon Jun 11 2012 Lukáš Nykrýn <lnykryn@redhat.com> - 1.2.1-1
- New package
