%define Product PloneLanguageTool
%define product plonelanguagetool
%define name    zope-%{Product}
%define version 2.0.1
%define release %mkrel 1

%define zope_minver	2.7
%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	PloneLanguageTool allows to set the available languages in a Plone site
License:	GPL
Group:		System/Servers
URL:		http://plone.org/products/%{product}
Source:		http://plone.org/products/%{product}/releases/%{version}/%{Product}-%{version}.tar.gz
Requires:	zope >= %{zope_minver}
Requires:	zope-Plone >= 2.0.5
BuildArch:	noarch

%description
PloneLanguageTool allows you to set the available languages in your Plone
site, select various fallback mechanisms, and control the use of flags
for language selection and translations.


%prep
%setup -c -q

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
