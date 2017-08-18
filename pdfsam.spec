%global _iconsdir %{_datadir}/icons

Name:		pdfsam
Version:	2.2.4
Release:	5%{?dist}
Summary:	PDF Split and Merge enhanced
Group: 		Applications/Publishing
License:	GPLv2
URL:		http://www.pdfsam.org
Source0:	http://sourceforge.net/projects/pdfsam/files/pdfsam-enhanced/%{version}e/pdfsam-%{version}e-out-src.zip
Source1:	https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

BuildArch:	noarch
BuildRequires:	ant
BuildRequires:	dos2unix
BuildRequires:	java-1.8.0-openjdk-devel
BuildRequires:	javapackages-tools
Requires:	java >= 1.7.0
Requires:	javapackages-tools


%description
PDFsam is a simple, platform independent software designed to split and merge
pdf files. It's stable, completely free and it should cover most of your
needs.


%prep
%setup -q -c %{name}-%{version}e
# extract all individual source zip files
for FILE in *.zip; do
    unzip -q -o $FILE ; rm -f $FILE
done
# fix line endings
for FILE in pdfsam-maine/doc/licenses/*/*.txt; do
    dos2unix -k -o $FILE
done
dos2unix -k -o pdfsam-maine/doc/enhanced/readme.txt
dos2unix -k -o pdfsam-maine/doc/enhanced/changelog-enhanced.txt


%build
cd pdfsam-maine/ant/
%ant -Dpdfsam.deploy.dir="%{_javadir}/%{name}" \
     -Dworkspace.dir="../" \
     -Dbuild.dir="../build"


%install
# create start script
cat << EOF > %{name}.sh
#!/bin/bash
cd %{_javadir}/%{name}
java -jar %{_javadir}/%{name}/%{name}.jar
cd -
EOF
install -D -m 755 %{name}.sh %{buildroot}%{_bindir}/%{name}

# create application dir and populate it
install -d -m 755 %{buildroot}%{_javadir}/%{name}
for i in ext lib plugins pdfsam-%{version}e.jar pdfsam-config.xml; do
    cp -rf build/pdfsam-maine/release/dist/pdfsam-enhanced/$i %{buildroot}%{_javadir}/%{name}/
done
ln -s pdfsam-%{version}e.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar

# menu entry and icon #
install -D -m 644 build/pdfsam-maine/release/dist/pdfsam-enhanced/doc/icons/pdfsam_enhanced.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -D -m 644 build/pdfsam-maine/release/dist/pdfsam-enhanced/doc/icons/pdfsam_enhanced.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg

# License
cp -f %{S:1} GPL-2.0.txt

install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=PDFsam
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Office;Java;Viewer;TextTools;
EOF

%files
%doc build/pdfsam-maine/release/dist/pdfsam-enhanced/doc/{changelog-enhanced.txt,pdfsam-1.5.0e-tutorial.pdf,readme.txt}
%license GPL-2.0.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_javadir}/%{name}/


%changelog

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

