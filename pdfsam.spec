#
# spec file for package pdfsam
#
# Copyright (c) 2020 UnitedRPMs.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://goo.gl/zqFJft
#

%global _iconsdir %{_datadir}/icons

Name:		pdfsam
Version:	4.1.4
Release:	1%{?dist}
Summary:	PDF Split and Merge enhanced
Group: 	Applications/Publishing
License:	GPLv3
URL:		https://pdfsam.org/
Source0:	https://github.com/torakiki/%{name}/releases/download/v%{version}/%{name}-%{version}-linux.zip
Source1:	pdfsam
Source2:	pdfsam.png
Source3:	org.pdfsam.pdfsam.metainfo.xml

BuildArch:	noarch
BuildRequires:	gendesk
Requires:	java-11-openjdk


%description
PDFsam is a simple, platform independent software designed to split and merge
pdf files. It's stable, completely free and it should cover most of your
needs.


%prep
%autosetup -n %{name}-%{version}-linux

%build
# create *.desktop file
gendesk -f -n \
          --pkgname="%{name}" \
          --pkgdesc="A free open source tool to split and merge pdf documents" \
          --name="PDFsam" \
          --categories="Office"


%install

  install -dm755 "$RPM_BUILD_ROOT/usr/share/java/%{name}/lib"
  install -Dm644 "pdfsam-basic-%{version}.jar" \
                 "$RPM_BUILD_ROOT/usr/share/java/%{name}/"
  install -Dm644 lib/* \
                 "$RPM_BUILD_ROOT/usr/share/java/%{name}/lib"
  install -Dm755 "bin/pdfsam.sh" \
                 "$RPM_BUILD_ROOT/usr/share/java/%{name}/bin/pdfsam.sh"

  # exec
  install -Dm755 %{S:1} "$RPM_BUILD_ROOT/usr/bin/pdfsam"

  # desktop
  install -Dm644 %{S:2} "$RPM_BUILD_ROOT/usr/share/pixmaps/pdfsam.png"
  install -Dm644 "%{name}.desktop" "$RPM_BUILD_ROOT/usr/share/applications/%{name}.desktop"
  
  # Appdata
  install -Dm 0644 %{S:3} %{buildroot}/%{_metainfodir}/org.pdfsam.pdfsam.metainfo.xml
  
  # mangling shebang fix
   sed -i 's|/bin/sh|/usr/bin/sh|g' %{buildroot}/%{_datadir}/java/pdfsam/bin/pdfsam.sh

%files
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/org.pdfsam.pdfsam.metainfo.xml
%{_datadir}/pixmaps/%{name}.png
%{_javadir}/%{name}/


%changelog

* Sun Jul 26 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 4.1.4-1
- Updated to 4.1.4

* Sat Apr 25 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 4.1.3-1
- Updated to 4.1.3

* Thu Mar 26 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 4.1.2-1
- Updated to 4.1.2

* Fri Feb 07 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 4.1.1-1
- Updated to 4.1.1

* Thu Oct 24 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 4.0.5-1
- Updated to 4.0.5

* Sat Sep 14 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 4.0.4-1
- Updated to 4.0.4

* Sat Jun 15 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 4.0.3-1
- Updated to 4.0.3

* Mon Jan 14 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 4.0.1-1
- Updated to 4.0.1

* Fri Sep 07 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.3.7-1
- Updated to 3.3.7

* Thu Aug 02 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.3.6-1
- Updated to 3.3.6

* Tue Nov 28 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.3.5-1
- Updated to 3.3.5

* Tue Nov 07 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.3.4-1
- Updated to 3.3.4

* Fri Oct 13 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.3.3-1
- Updated to 3.3.3

* Fri Sep 29 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.3.2-2
- Added missed dependency

* Tue Sep 26 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.3.2-1
- Updated to 3.3.2-1

* Thu Aug 17 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.2.4-5
- Upstream

* Mon Feb 08 2016 umeabot <umeabot> 2.2.4e-4.mga6
+ Revision: 945384
- Mageia 6 Mass Rebuild

* Wed Oct 15 2014 umeabot <umeabot> 2.2.4e-3.mga5
+ Revision: 749983
- Second Mageia 5 Mass Rebuild

* Tue Sep 16 2014 umeabot <umeabot> 2.2.4e-2.mga5
+ Revision: 683387
- Mageia 5 Mass Rebuild

* Mon Sep 08 2014 akien <akien> 2.2.4e-1.mga5
+ Revision: 673607
- Version 2.2.4e

* Sun Mar 23 2014 akien <akien> 2.2.2e-2.mga5
+ Revision: 607033
- Move jar files to %%javadir/%%name
- Move SVG icon to the scalable icons directory

* Sun Mar 23 2014 akien <akien> 2.2.2e-1.mga5
+ Revision: 607013
- New version 2.2.2e
- Install only relevant icon
- Improve %%description
- imported package pdfsam


* Mon Sep 17 2012 LTN Packager <packager-el6rpms@LinuxTECH.NET> - 2.2.1e-2
- initial spec-file release, inspired by:
  - spec-file found in openSUSE Build Service
  - http://users.telenet.be/x86_64/SPECS/pdfsam.spec
  - http://www.heise.de/open/artikel/Toolbox-PDF-Werkstatt-mit-PDFsam-1705524.html

