%global _iconsdir %{_datadir}/icons

Name:		pdfsam
Version:	3.3.2
Release:	2%{?dist}
Summary:	PDF Split and Merge enhanced
Group: 		Applications/Publishing
License:	GPLv3
URL:		http://www.pdfsam.org/
Source0:	https://github.com/torakiki/pdfsam/releases/download/v%{version}/pdfsam-%{version}-bin.zip
Source1:	pdfsam
Source2:	pdfsam.png

BuildArch:	noarch
BuildRequires:	gendesk
Requires:	java >= 1.8.0
Requires:	java-1.8.0-openjdk-openjfx
Requires:	javapackages-tools


%description
PDFsam is a simple, platform independent software designed to split and merge
pdf files. It's stable, completely free and it should cover most of your
needs.


%prep
%autosetup -n %{name}-%{version}

%build
# create *.desktop file
gendesk -f -n \
          --pkgname="%{name}" \
          --pkgdesc="A free open source tool to split and merge pdf documents" \
          --name="PDFsam" \
          --categories="Office"


%install
  install -dm755 "$RPM_BUILD_ROOT/%{_javadir}/%{name}/modules"
  install -Dm644 "pdfsam-community-%{version}.jar" \
                 "$RPM_BUILD_ROOT/%{_javadir}/%{name}/"
  install -Dm755 "bin/pdfsam.sh" \
                 "$RPM_BUILD_ROOT/%{_javadir}/%{name}/bin/pdfsam.sh"
  install -Dm755 "etc/logback.xml" \
                 "$RPM_BUILD_ROOT/%{_javadir}/%{name}/etc/logback.xml"
  install -Dm755 "resources/splash.gif" \
                 "$RPM_BUILD_ROOT/%{_javadir}/%{name}/resources/splash.gif"

  # exec
  install -Dm755 %{S:1} "$RPM_BUILD_ROOT/usr/bin/pdfsam"

  # desktop
  install -Dm644 %{S:2} "$RPM_BUILD_ROOT/usr/share/pixmaps/pdfsam.png"
  install -Dm644 "%{name}.desktop" "$RPM_BUILD_ROOT/usr/share/applications/%{name}.desktop"

%files
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_javadir}/%{name}/


%changelog

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

