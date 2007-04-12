%define product		PloneLanguageTool
%define ver		1.5
%define rel		1

%define zope_minver	2.7

%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python


Summary:	PloneLanguageTool allows to set the available languages in a Plone site
Name:		zope-%{product}
Version:	%{ver}
Release:	%mkrel %{rel}
License:	GPL
Group:		System/Servers
Source:		http://plone.org/products/plonelanguagetool/releases/%{version}/PloneLanguageTool-%{version}.tar.bz2
URL:		http://plone.org/products/plonelanguagetool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
Requires:	zope >= %{zope_minver}
Requires:	plone >= 2.0.5

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
%defattr(-, root, root, 0755)
%{software_home}/Products/*




