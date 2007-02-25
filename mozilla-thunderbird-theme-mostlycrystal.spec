%define		_realname	mostlycrystal
%define		_fver	%(echo %{version} | tr -d .)
Summary:	Mostly Crystal is a theme for Thunderbird
Name:		mozilla-thunderbird-theme-mostlycrystal
Version:	1.5.0.23
Release:	0.1
License:	?
Group:		Themes
Source0:	http://www.tom-cat.com/mozilla/downloads/mostlycrystal_tb_15.jar
# Source0-md5:	3f46349ec17a4cb793a28ca7b2e4c01a
URL:		http://www.tom-cat.com/mozilla/
Requires(post,postun):	textutils
Requires:	mozilla-thunderbird >= 1.5
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_extensiondir	%{_libdir}/mozilla-thunderbird/extensions/\{%{_uuid}\}
%define		_uuid			1b6c444d-7472-43e4-95f4-6b28eb7946a3

%description
Mostly Crystal is a theme for Thunderbird 1.5 "mostly" from the
colorful Crystal SVG (for Linux) icon set designed by Everaldo and
includes icons in their original form plus custom-edited composites of
the originals.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_extensiondir}
cp -a . $RPM_BUILD_ROOT%{_extensiondir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_extensiondir}
