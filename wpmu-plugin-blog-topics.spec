%define		plugin	blog-topics
Summary:	WordPressMU Blog Topics Plugin
Name:		wpmu-plugin-%{plugin}
Version:	1.0
Release:	0.4
License:	GPL v2+
Group:		Applications/Publishing
Source0:	http://downloads.wordpress.org/plugin/blog-topics.zip
# Source0-md5:	3bb901ee63ce4c623e33b55c9f6b504b
URL:		http://wordpress.org/extend/plugins/blog-topics/
Patch0:		current_topic.patch
Patch1:		localization.patch
Patch2:		utf8.patch
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	wpmu >= 2.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		wp_root		%{_datadir}/wpmu
%define		wp_content	%{wp_root}/wp-content
%define		pluginsdir	%{wp_content}/mu-plugins

%description
This plugin creates site-wide topics. Each blog can be identified as
belonging to a single topic. Blog owners can select a topic for their
blog at creation time, and through a menu under settings. Blog owners
can also choose whether or not to include their content in any
site-wide aggregated content via the Blog Topics Settings menu.

%prep
%setup -qn %{plugin}
%undos readme.txt *.php
%patch0 -p1
%patch1 -p1
%patch2 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{wp_content},%{pluginsdir}}
cp -a cets_blogtopics.php cets_blog_topics $RPM_BUILD_ROOT%{pluginsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%{pluginsdir}/*.php
%{pluginsdir}/cets_blog_topics
