%define		srcname		guava
%include	/usr/lib/rpm/macros.java
Summary:	Google Core Libraries for Java
Name:		java-%{srcname}
Version:	15.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Java
Source0:	http://search.maven.org/remotecontent?filepath=com/google/guava/guava/%{version}/%{srcname}-%{version}.jar
# Source0-md5:	2c10bb2ca3ac8b55b0e77e54a7eb3744
URL:		http://code.google.com/p/guava-libraries
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Guava is a suite of core and expanded libraries that include utility
classes, Google's collections, io classes, and much much more. This
project is a complete packaging of all the Guava libraries into a
single jar. Individual portions of Guava can be used by downloading
the appropriate module and its dependencies.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Documentation

%description javadoc
API documentation for %{name}.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
cp -p %{SOURCE0} $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/guava-%{version}.jar
%{_javadir}/guava.jar
