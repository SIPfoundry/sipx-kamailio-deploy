%define _sharedir %{_prefix}/share

%define version %{VERSION_NUMBER}
%define release %{BUILD_NUMBER}

Summary:      Kamailio, very fast, reliable and flexible SIP Server
Name:         kamailio
Version:	%{version}
Release:	%{release}
License:      GPL
Group:        Productivity/Telephony/SIP/Servers
Source0:      http://www.kamailio.org/pub/kamailio/%{version}/%{name}-%{version}_src.tar.gz
%if 0%{?suse_version}
Source1:      kamailio.init.suse
%else
Source1:      kamailio.init
%endif
Source2:      kamailio.default
URL:          http://www.kamailio.org/
Vendor:       kamailio.org
BuildRoot:    %{_tmppath}/%{name}-%{version}-buildroot
Conflicts:	  kamailio-auth-ephemeral < %version, kamailio-bdb < %version
Conflicts:	  kamailio-carrierroute < %version, kamailio-cnxcc < %version, kamailio-cpl < %version
Conflicts:	  kamailio-dnssec < %version, kamailio-erlang < %version, kamailio-ev < %version,
Conflicts:	  kamailio-geoip < %version, kamailio-gzcompress < %version, kamailio-ims < %version
Conflicts:	  kamailio-java < %version, kamailio-jansson < %version, kamailio-json < %version
Conflicts:	  kamailio-kazoo < %version
Conflicts:	  kamailio-ldap < %version, kamailio-lua < %version
Conflicts:	  kamailio-memcached < %version,kamailio-mongodb < %version, kamailio-mysql < %version
Conflicts:	  kamailio-outbound < %version, kamailio-perl < %version
Conflicts:	  kamailio-postgresql < %version, kamailio-presence < %version
Conflicts:	  kamailio-purple < %version, kamailio-python < %version
Conflicts:	  kamailio-radius < % version, kamailio-redis < %version
Conflicts:	  kamailio-regex < %version, kamailio-sctp < %version
Conflicts:	  kamailio-snmpstats < %version, kamailio-sqlite < %version
Conflicts:	  kamailio-tls < %version, kamailio-unixodbc < %version
Conflicts:	  kamailio-utils < %version, kamailio-uuid < %version, kamailio-websocket < %version
Conflicts:	  kamailio-xml < %version, kamailio-xmpp < %version
BuildRequires:  make gcc flex bison pcre-devel

%if 0%{?centos_version} || 0%{?fedora} || 0%{?rhel_version}
BuildRequires:  which
BuildRequires:  redhat-rpm-config
%endif

%if 0%{?suse_version}
PreReq:       %insserv_prereq %fillup_prereq
BuildRequires:  pkg-config
%endif

BuildRequires:  openssl
BuildRequires:  perl
%if 0%{?fedora}
BuildRequires:  perl-devel
BuildRequires:  perl-ExtUtils-Embed
%endif
BuildRequires:  python redhat-rpm-config

%description
Kamailio is a very fast, reliable and flexible SIP (RFC3261)
proxy server. Written entirely in C, Kamailio can handle thousands calls
per second even on low performance hardware. A C Shell like scripting
language provides full control over the server's behaviour. It's modular
architecture allows only required functionality to be loaded.
Among available features: IPv4, IPv6, digest authentication, accounting,
CPL scripts, instant messaging, MySQL, Postgres and UNIXODBC support,
NoSQL backends Redis, Cassandra, Redis, Memcached,
radius authentication, record routing, SMS gateway, ENUM, UDP, TCP,
TLS and SCTP, transaction and dialog module, OSP, statistics support,
registrar and user location, SNMP, SIMPLE Presence, Lua, Perl, Python, Java
and Mono programming interfaces, WebSocket support for WebRTC, IMS extensions,
embedded XCAP server and MSRP relay, DNSSEC, gzip compression.

# list of flags to enable extra packages
%define _with_bdb 0
%define _with_carrierroute 0
%define _with_cnxcc 0
%define _with_dnssec 0
%define _with_erlang 0
%define _with_ev 0
%define _with_geoip 0
%define _with_java 0
%define _with_json 0
%define _with_jansson 0
%define _with_ldap 0
%define _with_lua 0
%define _with_kazoo 0
%define _with_memcached 0
%define _with_mi_xmlrpc 0
%define _with_mongodb 0
%define _with_mono 0
%define _with_perl 0
%define _with_purple 0
%define _with_radius 0
%define _with_redis 0
%define _with_sctp 0
%define _with_snmp 0
%define _with_sqlite 0
%define _with_websocket 0
%define _with_uuid 0

# define flags to enable extra packages
%define _with_bdb 1
%define _with_carrierroute 1
%define _with_ev 1
%define _with_ldap 1
%define _with_sctp 1
%define _with_snmp 1
%define _with_uuid 1
%define _with_mongodb 1

# groups of distros
%if 0%{?centos_version} || 0%{?rhel_version}  || 0%{?fedora}
%define _with_ev 0
%endif

#centos
%if 0%{?centos_version}
%define _with_cnxcc 0
%endif

%if 0%{?centos_version} < 600
%define _with_uuid 0
%endif

%if 0%{?centos_version} >= 600
%define _with_sqlite 1
%define _with_websocket 1
%endif

%if 0%{?centos_version} >= 700
%define _with_bdb 0
%define _with_jansson 1
%endif

#fedora
%if 0%{?fedora}
%define _with_cnxcc 1
%define _with_dnssec 1
%define _with_jansson 1
%define _with_json 1
%define _with_mono 0
%define _with_perl 1
%define _with_radius 1
%define _with_sqlite 1
%endif

%if 0%{?fedora} > 17
%define _with_bdb 0
%define _with_erlang 1
%endif

# opensuse
%if 0%{?suse_version} > 1100
%define _with_radius 1
%define _with_lua 1
%define _with_perl 1
%define _with_sqlite 1
%endif
%if 0%{?suse_version} > 1200
%define _with_bdb 0
%define _with_mono 0
%define _with_websocket 1
%endif

%if 0%{?suse_version} > 1210
%define _with_lua 0
%endif

%if 0%{?suse_version} >= 1310
%define _with_ldap 0
%endif

# redhat
%if 0%{?rhel_version} >= 600
%define _with_sctp 0
%endif

%if 0%{?rhel_version} >= 700
%define _with_bdb 0
%endif


%package	auth-ephemeral
Summary:	Functions for authentication using ephemeral credentials
Group:		System Environment/Daemons
Requires:	openssl, kamailio = %version
BuildRequires:	openssl-devel

%description auth-ephemeral
Functions for authentication using ephemeral credentials.


%if 0%{_with_bdb}
%package  bdb
Summary:  Berkeley connectivity for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: db4, kamailio = %version
BuildRequires: db4-devel

%description bdb
Berkeley database connectivity for Kamailio.
%endif


%if 0%{_with_carrierroute}
%package  carrierroute
Summary:  Carrier routing module for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: kamailio = %version

%description carrierroute
Carrier routing, balancing, and blacklisting for Kamailio.
%endif


%if 0%{_with_cnxcc}
%package  cnxcc
Summary:  Prepaid and call control module for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: hiredis, libevent, kamailio = %version
BuildRequires: hiredis-devel libevent-devel

%description cnxcc
Prepaid and call control module for Kamailio.
%endif


%package  cpl
Summary:  CPL interpreter for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: libxml2, kamailio = %version
BuildRequires:  libxml2-devel

%description cpl
CPL (Call Processing Language) interpreter engine for Kamailio.


%if 0%{_with_dnssec}
%package	dnssec
Summary:	DNSSEC support for Kamailio
Group:		System Environment/Daemons
Requires:	dnssec-tools-libs, kamailio = %version
BuildRequires:	dnssec-tools-libs-devel

%description	dnssec
DNSSEC support for Kamailio.
%endif


%if 0%{_with_erlang}
%package	erlang
Summary:	Erlang node connector for Kamailio
Group:		System Environment/Daemons
Requires:	erlang, erlang-erl_interface, kamailio = %version
BuildRequires:	erlang, erlang-erl_interface

%description	erlang
Erlang module - erlang node connector for Kamailio.
%endif

%if 0%{_with_ev}
%package	ev
Summary:	EVAPI extension using libev support for Kamailio
Group:		System Environment/Daemons
Requires:	libev, kamailio = %version
BuildRequires:	libev-devel

%description	ev
EVAPI - event driven API over TCP for Kamailio.
%endif


%if 0%{_with_geoip}
%package  geoip
Summary:  GeoIP extensions for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: kamailio = %version
BuildRequires: libGeoIP-devel

%description geoip
Max Mind GeoIP real-time query support for Kamailio.
%endif


%package	gzcompress
Summary:	Compressed body (SIP and HTTP) handling for Kamailio
Group:		System Environment/Daemons
Requires:	zlib, kamailio = %version
BuildRequires:	zlib-devel

%description	gzcompress
Compressed body (SIP and HTTP) handling for Kamailio.


%if 0%{_with_java}
%package	java
Summary:	Java extensions for Kamailio.
Group:		System Environment/Daemons
Requires:	libgcj, java-1.6.0-openjdk, kamailio = %version
BuildRequires:	libgcj-devel, java-1.6.0-openjdk-devel, ant

%description	java
Java extensions for Kamailio.
%endif


%package  ims
Summary:  IMS extensions for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: libxml2, kamailio = %version
BuildRequires: libxml2-devel

%description ims
IMS extensions for Kamailio.


%if 0%{_with_jansson}
%package  jansson
Summary:  JSON parser and JSONRPC modules for Kamailio using libjansson
Group:    Productivity/Telephony/SIP/Servers
Requires: jansson, libevent, kamailio = %version
BuildRequires: jansson-devel, libevent-devel

%description jansson
JSON parser and JSONRPC modules for Kamailio using libjansson.
%endif


%if 0%{_with_json}
%package  json
Summary:  JSON parser and JSONRPC modules for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: kamailio = %version
BuildRequires: json-c-devel libevent-devel

%description json
JSON parser and JSONRPC modules for Kamailio.
%endif


%if 0%{_with_kazoo}
%package	kazoo
Summary:	Kazoo middle layer connector support for Kamailio
Group:		System Environment/Daemons
Requires:	libuuid, kamailio = %version
BuildRequires:	librabbitmq-devel, json-c-devel, libuuid-devel

%description	kazoo
Kazoo module for Kamailio.
%endif


%if 0%{_with_ldap}
%package  ldap
Summary:  LDAP modules for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: kamailio = %version
%if 0%{?suse_version} > 1100
Requires:      openldap2
BuildRequires: openldap2-devel
%else
Requires:      openldap
BuildRequires: openldap-devel
%endif

%description ldap
LDAP search interface, DB APIv2 and h350 for Kamailio.
%endif


%if 0%{_with_lua}
%package  lua
Summary:  Lua embedded interpreter for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: lua, kamailio = %version
BuildRequires: lua-devel

%description lua
Lua embedded interpreter for Kamailio.
%endif


%if 0%{_with_memcached}
%package  memcached
Summary:  Memcache distributed hash table for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: libmemcached, kamailio = %version
BuildRequires:  libmemcached-devel

%description memcached
Memcache distributed hash table for Kamailio.
%endif


%if 0%{_with_mi_xmlrpc}
%package  mi_xmlrpc
Summary:  XMLRPC support for management interface of Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: kamailio = %version
BuildRequires:  libxml2-devel xmlrpc-c-devel

%description mi_xmlrpc
XMLRPC support for management interface of Kamailio.
%endif


%if 0%{_with_mongodb}
%package	mongodb
Summary:	MongoDB connectors for Kamailio
Group:		System Environment/Daemons
Requires:	libmongoc, kamailio = %version
BuildRequires:	libmongoc-devel

%description	mongodb
MongoDB modules for Kamailio.
%endif


%if 0%{_with_mono}
%package  mono
Summary:  Embedded interpreter for managed code using Mono project
Group:    Productivity/Telephony/SIP/Servers
Requires:      mono-core, kamailio = %version
BuildRequires: mono-devel

%description mono
Embedded interpreter for managed code (C#, IronJava, F#, ...) using Mono project.
%endif


%package  mysql
Summary:  MySQL connectivity for the Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: mysql-libs, kamailio = %version
BuildRequires:  mysql-devel zlib-devel

%description mysql
MySQL database connectivity for Kamailio.


%package  outbound
Summary:  Outbound (RFC 5626) support for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: openssl, kamailio = %version
BuildRequires: openssl-devel

%description outbound
RFC 5626, "Managing Client-Initiated Connections in the Session Initiation
Protocol (SIP)" support for Kamailio.


%if 0%{_with_perl}
%package  perl
Summary:  Perl embedded interpreter and virtual database driver for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: perl
Requires: kamailio = %version

%description perl
Perl embedded interpreter and virtual database driver for Kamailio.
%endif


%package  presence
Summary:  SIP SIMPLE presence server and user agent support for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: libxml2, libcurl, kamailio = %version
BuildRequires:  libxml2-devel, curl-devel

%description presence
SIP Presence (and RLS, XCAP, etc) support for Kamailio.


%package  postgres
Summary:  Postgres connectivity for the Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: postgresql-libs, kamailio = %version
BuildRequires:  postgresql-devel

%description postgres
PostgreSQL database connectivity for Kamailio.


%if 0%{_with_purple}
%package  purple
Summary:  Multi-protocol IM and presence gateway module
Group:    Productivity/Telephony/SIP/Servers
%if 0%{?fedora}
Requires: glib, libpurple, libxml2, kamailio = %version, kamailio-presence = %version
BuildRequires: glib-devel, libpurple-devel, libxml2-devel
%else
Requires: glib2, libpurple, libxml2, kamailio = %version, kamailio-presence = %version
BuildRequires: glib2-devel, libpurple-devel, libxml2-devel
%endif

%description purple
Multi-protocol IM and presence gateway module.
%endif


%package  python
Summary:  Python embedded interpreter for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: python kamailio = %version redhat-rpm-config
BuildRequires: python-devel

%description python
Python embedded interpreter for Kamailio.


%if 0%{_with_radius}
%package  radius
Summary:  Radius AAA API for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: kamailio = %version
%if 0%{?suse_version} > 1100
BuildRequires:  freeradius-client-devel
%else
Requires: radiusclient-ng
BuildRequires:  radiusclient-ng-devel
%endif

%description radius
Radius AAA API for Kamailio.
%endif


%if 0%{_with_redis}
%package  redis
Summary:  REDIS NoSQL database connector for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: hiredis, kamailio = %version
BuildRequires: hiredis-devel

%description redis
REDIS NoSQL database connector for Kamailio.
%endif


%if 0%{_with_sctp}
%package	sctp
Summary:	SCTP transport for Kamailio
Group:		System Environment/Daemons
Requires:	lksctp-tools, kamailio = %version
BuildRequires:	lksctp-tools-devel

%description	sctp
SCTP transport for Kamailio.
%endif


%if 0%{_with_snmp}
%package  snmpstats
Summary:  SNMP AgentX subagent module for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: net-snmp-utils, kamailio = %version
%if 0%{?fedora}
Requires:      net-snmp-agent-libs
%else
Requires:      net-snmp-libs
%endif
BuildRequires:  net-snmp-devel
%if 0%{?suse_version} > 1100
BuildRequires:  libsensors4-devel
%else
BuildRequires:  lm_sensors-devel
%endif

%description snmpstats
SNMP management interface (scalar statistics) for Kamailio.
%endif


%if 0%{_with_sqlite}
%package  sqlite
Summary:  SQLite connectivity for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: sqlite, kamailio = %version
BuildRequires: sqlite-devel

%description sqlite
SQLite database connectivity for Kamailio.
%endif


%package  tls
Summary:  TLS transport protocol for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: openssl, kamailio = %version
BuildRequires:  openssl-devel

%description tls
TLS transport protocol and auth identity for Kamailio.


%package  unixodbc
Summary:  UnixODBC connectivity for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: unixODBC, kamailio = %version
BuildRequires:  unixODBC-devel

%description unixodbc
UnixODBC database connectivity for Kamailio.


%package  utils
Summary:  Utils for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: libcurl, libxml2, kamailio = %version
BuildRequires: curl-devel, libxml2-devel

%description utils
Non-SIP utitility functions for Kamailio.


%if 0%{_with_uuid}
%package	uuid
Summary:	uuid generator for Kamailio
Group:		System Environment/Daemons
Requires:	libuuid, kamailio = %version
BuildRequires:	libuuid-devel

%description	uuid
UUID module for Kamailio.
%endif


%if 0%{_with_websocket}
%package  websocket
Summary:  WebSocket transport for Kamailio
Group:    Productivity/Telephony/SIP/Servers
%if 0%{?suse_version} > 1020
Requires: libunistring, kamailio = %version
%else
%if 0%{?centos_version} >= 600
Requires: libunistring, kamailio = %version
%else
Requires: libunistring0, kamailio = %version
%endif
%endif
BuildRequires:  libunistring-devel

%description websocket
WebSocket transport for Kamailio.
%endif


%package  xml
Summary:  XML modules for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: libxml2, kamailio = %version
BuildRequires: libxml2-devel

%description xml
XML modules (xmlrpc, xmlops, xhttp_pi) for Kamailio.


%package  xmpp
Summary:  SIP to XMPP message and presence translation support for Kamailio
Group:    Productivity/Telephony/SIP/Servers
Requires: kamailio = %version
%if 0%{?suse_version} > 1020
BuildRequires:  libexpat-devel
%else
BuildRequires:  expat-devel
%endif

%description xmpp
SIP/XMPP IM and presence gateway for Kamailio.



%prep
%setup -n %{name}-%{version}

%build
%if 0%{?suse_version} > 1100
export FREERADIUS=1
%endif
make cfg \
		prefix=/usr \
		basedir=%{buildroot} \
		cfg_prefix=%{buildroot} \
		cfg_target=/%{_sysconfdir}/kamailio/ \
		modules_dirs="modules" 
make
make every-module skip_modules="malloc_test print print_lib" \
		group_include="kstandard"
make every-module group_include="kautheph"
%if 0%{_with_bdb}
make every-module group_include="kberkeley"
%endif
%if 0%{_with_carrierroute}
make every-module group_include="kcarrierroute"
%endif
%if 0%{_with_cnxcc}
make every-module group_include="kcnxcc"
%endif
%if 0%{_with_dnssec}
make every-module group_include="kdnssec"
%endif
%if 0%{_with_erlang}
make every-module group_include="kerlang"
%endif
%if 0%{_with_ev}
make every-module group_include="kev"
%endif
make every-module group_include="kcpl"
%if 0%{_with_geoip}
make every-module group_include="kgeoip"
%endif
make every-module group_include="kgzcompress"
make every-module group_include="kims"
%if 0%{_with_java}
make every-module group_include="kjava"
%endif
%if 0%{_with_jansson}
make every-module group_include="kjansson"
%endif
%if 0%{_with_json}
make every-module group_include="kjson"
%endif
%if 0%{_with_kazoo}
make every-module group_include="kkazoo"
%endif
%if 0%{_with_ldap}
make every-module group_include="kldap"
%endif
%if 0%{_with_lua}
make every-module group_include="klua"
%endif
%if 0%{_with_memcached}
make every-module group_include="kmemcached"
%endif
%if 0%{_with_mongodb}
make every-module group_include="kmongodb"
%endif
%if 0%{_with_mono}
make every-module group_include="kmono"
%endif
make every-module group_include="kmysql"
make every-module group_include="koutbound"
%if 0%{_with_perl}
make every-module group_include="kperl"
%endif
make every-module group_include="kpostgres"
make every-module group_include="kpresence"
%if 0%{_with_purple}
make every-module group_include="kpurple"
%endif
make every-module group_include="kpython"
%if 0%{_with_radius}
%if 0%{?suse_version} > 1100
make every-module FREERADIUS=1 group_include="kradius"
%else
make every-module group_include="kradius"
%endif
%endif
%if 0%{_with_redis}
make every-module group_include="kredis"
%endif
%if 0%{_with_sctp}
make every-module group_include="ksctp"
%endif
%if 0%{_with_snmp}
make every-module group_include="ksnmpstats"
%endif
%if 0%{_with_sqlite}
make every-module group_include="ksqlite"
%endif
make every-module group_include="ktls"
make every-module group_include="kunixodbc"
make every-module group_include="kutils"
%if 0%{_with_uuid}
make every-module group_include="kuuid"
%endif
%if 0%{_with_websocket}
make every-module group_include="kwebsocket"
%endif
make every-module group_include="kxmpp"
make every-module group_include="kxml"


%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"

make install skip_modules="malloc_test print print_lib" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
make install-modules-all skip_modules="malloc_test print print_lib" \
		group_include="kstandard" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/

make install-modules-all group_include="kautheph" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%if 0%{_with_bdb}
make install-modules-all group_include="kberkeley" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
%if 0%{_with_carrierroute}
make install-modules-all group_include="kcarrierroute" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
%if 0%{_with_cnxcc}
make install-modules-all group_include="kcnxcc" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
make install-modules-all group_include="kcpl" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%if 0%{_with_dnssec}
make install-modules-all group_include="kdnssec" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
%if 0%{_with_erlang}
make install-modules-all group_include="kerlang" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
%if 0%{_with_ev}
make install-modules-all group_include="kev" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
%if 0%{_with_geoip}
make install-modules-all group_include="kgeoip" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
make install-modules-all group_include="kgzcompress" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
make install-modules-all group_include="kims" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%if 0%{_with_java}
make install-modules-all group_include="kjava" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
%if 0%{_with_jansson}
make install-modules-all group_include="kjansson" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
%if 0%{_with_json}
make install-modules-all group_include="kjson" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
%if 0%{_with_ldap}
make install-modules-all group_include="kldap" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
%if 0%{_with_lua}
make install-modules-all group_include="klua" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
%if 0%{_with_kazoo}
make install-modules-all group_include="kkazoo" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
%if 0%{_with_memcached}
make install-modules-all group_include="kmemcached" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
%if 0%{_with_mongodb}
make install-modules-all group_include="kmongodb" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
%if 0%{_with_mono}
make install-modules-all group_include="kmono" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
make install-modules-all group_include="kmysql" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
make install-modules-all group_include="koutbound" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%if 0%{_with_perl}
make install-modules-all group_include="kperl" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
make install-modules-all group_include="kpostgres" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
make install-modules-all group_include="kpresence" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%if 0%{_with_purple}
make install-modules-all group_include="kpurple"
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
make install-modules-all group_include="kpython" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%if 0%{_with_radius}
%if 0%{?suse_version} > 1100
make install-modules-all FREERADIUS=1 group_include="kradius" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%else
make install-modules-all group_include="kradius" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
%endif
%if 0%{_with_redis}
make install-modules-all group_include="kredis" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
%if 0%{_with_sctp}
make install-modules-all group_include="ksctp" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
%if 0%{_with_snmp}
make install-modules-all group_include="ksnmpstats" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
%if 0%{_with_sqlite}
make install-modules-all group_include="ksqlite" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
make install-modules-all group_include="ktls" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
make install-modules-all group_include="kunixodbc" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
make install-modules-all group_include="kutils" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%if 0%{_with_uuid}
make install-modules-all group_include="kuuid" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
%if 0%{_with_websocket}
make install-modules-all group_include="kwebsocket" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
%endif
make install-modules-all group_include="kxml" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/
make install-modules-all group_include="kxmpp" \
		doc_prefix=%{buildroot} doc_dir=%{_docdir}/%{name}/


install -m755 -D %{SOURCE1} %{buildroot}/%{_initrddir}/%{name}

install -m644 -D %{SOURCE2} %{buildroot}/%{_sysconfdir}/default/kamailio


%pre
/usr/sbin/groupadd -r kamailio 2> /dev/null || :
/usr/sbin/useradd -r -g kamailio -s /bin/false -c "Kamailio daemon" \
                  -d %{_var}/run/kamailio kamailio 2> /dev/null || :


%clean
rm -rf "$RPM_BUILD_ROOT"

%post
%if 0%{?suse_version}
%else
/sbin/chkconfig --add kamailio
%endif

%preun
%if 0%{?suse_version}
%stop_on_removal %{name}
%else
if [ $1 = 0 ]; then
    /sbin/service kamailio stop > /dev/null 2>&1
    /sbin/chkconfig --del kamailio
fi
%endif
                
 
%postun
%if 0%{?suse_version}
%restart_on_update %{name}
%{insserv_cleanup}
%endif


%files
%defattr(-,root,root)
%dir %{_docdir}/kamailio
%doc %{_docdir}/kamailio/AUTHORS
%doc %{_docdir}/kamailio/NEWS
%doc %{_docdir}/kamailio/INSTALL
%doc %{_docdir}/kamailio/README
%doc %{_docdir}/kamailio/README-MODULES

%dir %{_docdir}/kamailio/modules
%doc %{_docdir}/kamailio/modules/README.acc
%doc %{_docdir}/kamailio/modules/README.alias_db
%doc %{_docdir}/kamailio/modules/README.async
%doc %{_docdir}/kamailio/modules/README.auth
%doc %{_docdir}/kamailio/modules/README.auth_db
%doc %{_docdir}/kamailio/modules/README.auth_diameter
%doc %{_docdir}/kamailio/modules/README.auth_xkeys
%doc %{_docdir}/kamailio/modules/README.avp
%doc %{_docdir}/kamailio/modules/README.avpops
%doc %{_docdir}/kamailio/modules/README.benchmark
%doc %{_docdir}/kamailio/modules/README.blst
%doc %{_docdir}/kamailio/modules/README.call_control
%doc %{_docdir}/kamailio/modules/README.cfg_db
%doc %{_docdir}/kamailio/modules/README.cfg_rpc
%doc %{_docdir}/kamailio/modules/README.cfgutils
%doc %{_docdir}/kamailio/modules/README.corex
%doc %{_docdir}/kamailio/modules/README.counters
%doc %{_docdir}/kamailio/modules/README.ctl
%doc %{_docdir}/kamailio/modules/README.db_cluster
%doc %{_docdir}/kamailio/modules/README.db_flatstore
%doc %{_docdir}/kamailio/modules/README.db_text
%doc %{_docdir}/kamailio/modules/README.db2_ops
%doc %{_docdir}/kamailio/modules/README.debugger
%doc %{_docdir}/kamailio/modules/README.dialog
%doc %{_docdir}/kamailio/modules/README.dialplan
%doc %{_docdir}/kamailio/modules/README.dispatcher
%doc %{_docdir}/kamailio/modules/README.diversion
%doc %{_docdir}/kamailio/modules/README.dmq
%doc %{_docdir}/kamailio/modules/README.dmq_usrloc
%doc %{_docdir}/kamailio/modules/README.domain
%doc %{_docdir}/kamailio/modules/README.domainpolicy
%doc %{_docdir}/kamailio/modules/README.drouting
%doc %{_docdir}/kamailio/modules/README.enum
%doc %{_docdir}/kamailio/modules/README.exec
%doc %{_docdir}/kamailio/modules/README.group
%doc %{_docdir}/kamailio/modules/README.htable
%doc %{_docdir}/kamailio/modules/README.imc
%doc %{_docdir}/kamailio/modules/README.ipops
%doc %{_docdir}/kamailio/modules/README.jsonrpc-s
%doc %{_docdir}/kamailio/modules/README.kex
%doc %{_docdir}/kamailio/modules/README.lcr
%doc %{_docdir}/kamailio/modules/README.mangler
%doc %{_docdir}/kamailio/modules/README.matrix
%doc %{_docdir}/kamailio/modules/README.maxfwd
%doc %{_docdir}/kamailio/modules/README.mediaproxy
%doc %{_docdir}/kamailio/modules/README.mi_datagram
%doc %{_docdir}/kamailio/modules/README.mi_fifo
%doc %{_docdir}/kamailio/modules/README.mi_rpc
%doc %{_docdir}/kamailio/modules/README.mohqueue
%doc %{_docdir}/kamailio/modules/README.mqueue
%doc %{_docdir}/kamailio/modules/README.msilo
%doc %{_docdir}/kamailio/modules/README.msrp
%doc %{_docdir}/kamailio/modules/README.mtree
%doc %{_docdir}/kamailio/modules/README.nat_traversal
%doc %{_docdir}/kamailio/modules/README.nathelper
%doc %{_docdir}/kamailio/modules/README.nosip
%doc %{_docdir}/kamailio/modules/README.p_usrloc
%doc %{_docdir}/kamailio/modules/README.path
%doc %{_docdir}/kamailio/modules/README.pdb
%doc %{_docdir}/kamailio/modules/README.pdt
%doc %{_docdir}/kamailio/modules/README.permissions
%doc %{_docdir}/kamailio/modules/README.pike
%doc %{_docdir}/kamailio/modules/README.pipelimit
%doc %{_docdir}/kamailio/modules/README.prefix_route
%doc %{_docdir}/kamailio/modules/README.pv
%doc %{_docdir}/kamailio/modules/README.qos
%doc %{_docdir}/kamailio/modules/README.ratelimit
%doc %{_docdir}/kamailio/modules/README.regex
%doc %{_docdir}/kamailio/modules/README.registrar
%doc %{_docdir}/kamailio/modules/README.rr
%doc %{_docdir}/kamailio/modules/README.rtimer
%doc %{_docdir}/kamailio/modules/README.rtjson
%doc %{_docdir}/kamailio/modules/README.rtpproxy
%doc %{_docdir}/kamailio/modules/README.rtpengine
%doc %{_docdir}/kamailio/modules/README.sanity
%doc %{_docdir}/kamailio/modules/README.sca
%doc %{_docdir}/kamailio/modules/README.seas
%doc %{_docdir}/kamailio/modules/README.sdpops
%doc %{_docdir}/kamailio/modules/README.sipcapture
%doc %{_docdir}/kamailio/modules/README.sipt
%doc %{_docdir}/kamailio/modules/README.siptrace
%doc %{_docdir}/kamailio/modules/README.siputils
%doc %{_docdir}/kamailio/modules/README.speeddial
%doc %{_docdir}/kamailio/modules/README.sl
%doc %{_docdir}/kamailio/modules/README.sms
%doc %{_docdir}/kamailio/modules/README.sqlops
%doc %{_docdir}/kamailio/modules/README.sst
%doc %{_docdir}/kamailio/modules/README.statistics
%doc %{_docdir}/kamailio/modules/README.statsd
%doc %{_docdir}/kamailio/modules/README.stun
%doc %{_docdir}/kamailio/modules/README.tcpops
%doc %{_docdir}/kamailio/modules/README.textops
%doc %{_docdir}/kamailio/modules/README.textopsx
%doc %{_docdir}/kamailio/modules/README.timer
%doc %{_docdir}/kamailio/modules/README.tm
%doc %{_docdir}/kamailio/modules/README.tmrec
%doc %{_docdir}/kamailio/modules/README.tmx
%doc %{_docdir}/kamailio/modules/README.topoh
%doc %{_docdir}/kamailio/modules/README.tsilo
%doc %{_docdir}/kamailio/modules/README.uac
%doc %{_docdir}/kamailio/modules/README.uac_redirect
%doc %{_docdir}/kamailio/modules/README.uid_auth_db
%doc %{_docdir}/kamailio/modules/README.uid_avp_db
%doc %{_docdir}/kamailio/modules/README.uid_domain
%doc %{_docdir}/kamailio/modules/README.uid_gflags
%doc %{_docdir}/kamailio/modules/README.uid_uri_db
%doc %{_docdir}/kamailio/modules/README.uri_db
%doc %{_docdir}/kamailio/modules/README.userblacklist
%doc %{_docdir}/kamailio/modules/README.usrloc
%doc %{_docdir}/kamailio/modules/README.xhttp
%doc %{_docdir}/kamailio/modules/README.xhttp_rpc
%doc %{_docdir}/kamailio/modules/README.xlog
%doc %{_docdir}/kamailio/modules/README.xprint

%dir %{_sysconfdir}/kamailio
%config(noreplace) %{_sysconfdir}/kamailio/*
%config %{_initrddir}/*
%config %{_sysconfdir}/default/*

%dir %{_libdir}/kamailio
%{_libdir}/kamailio/libbinrpc.so
%{_libdir}/kamailio/libbinrpc.so.0
%{_libdir}/kamailio/libbinrpc.so.0.1
%{_libdir}/kamailio/libkcore.so
%{_libdir}/kamailio/libkcore.so.1
%{_libdir}/kamailio/libkcore.so.1.0
%{_libdir}/kamailio/libkmi.so
%{_libdir}/kamailio/libkmi.so.1
%{_libdir}/kamailio/libkmi.so.1.0
%{_libdir}/kamailio/libsrdb1.so
%{_libdir}/kamailio/libsrdb1.so.1
%{_libdir}/kamailio/libsrdb1.so.1.0
%{_libdir}/kamailio/libsrdb2.so
%{_libdir}/kamailio/libsrdb2.so.1
%{_libdir}/kamailio/libsrdb2.so.1.0
%{_libdir}/kamailio/libsrutils.so
%{_libdir}/kamailio/libsrutils.so.1
%{_libdir}/kamailio/libsrutils.so.1.0
%{_libdir}/kamailio/libtrie.so
%{_libdir}/kamailio/libtrie.so.1
%{_libdir}/kamailio/libtrie.so.1.0

%dir %{_libdir}/kamailio/modules
%{_libdir}/kamailio/modules/acc.so
%{_libdir}/kamailio/modules/alias_db.so
%{_libdir}/kamailio/modules/async.so
%{_libdir}/kamailio/modules/auth.so
%{_libdir}/kamailio/modules/auth_db.so
%{_libdir}/kamailio/modules/auth_diameter.so
%{_libdir}/kamailio/modules/auth_xkeys.so
%{_libdir}/kamailio/modules/avp.so
%{_libdir}/kamailio/modules/avpops.so
%{_libdir}/kamailio/modules/benchmark.so
%{_libdir}/kamailio/modules/blst.so
%{_libdir}/kamailio/modules/call_control.so
%{_libdir}/kamailio/modules/cfg_db.so
%{_libdir}/kamailio/modules/cfg_rpc.so
%{_libdir}/kamailio/modules/cfgutils.so
%{_libdir}/kamailio/modules/corex.so
%{_libdir}/kamailio/modules/counters.so
%{_libdir}/kamailio/modules/ctl.so
%{_libdir}/kamailio/modules/db_cluster.so
%{_libdir}/kamailio/modules/db_flatstore.so
%{_libdir}/kamailio/modules/db_text.so
%{_libdir}/kamailio/modules/db2_ops.so
%{_libdir}/kamailio/modules/debugger.so
%{_libdir}/kamailio/modules/dialog.so
%{_libdir}/kamailio/modules/dialplan.so
%{_libdir}/kamailio/modules/dispatcher.so
%{_libdir}/kamailio/modules/diversion.so
%{_libdir}/kamailio/modules/dmq.so
%{_libdir}/kamailio/modules/dmq_usrloc.so
%{_libdir}/kamailio/modules/domain.so
%{_libdir}/kamailio/modules/domainpolicy.so
%{_libdir}/kamailio/modules/drouting.so
%{_libdir}/kamailio/modules/enum.so
%{_libdir}/kamailio/modules/exec.so
%{_libdir}/kamailio/modules/group.so
%{_libdir}/kamailio/modules/htable.so
%{_libdir}/kamailio/modules/imc.so
%{_libdir}/kamailio/modules/ipops.so
%{_libdir}/kamailio/modules/jsonrpc-s.so
%{_libdir}/kamailio/modules/kex.so
%{_libdir}/kamailio/modules/lcr.so
%{_libdir}/kamailio/modules/mangler.so
%{_libdir}/kamailio/modules/matrix.so
%{_libdir}/kamailio/modules/maxfwd.so
%{_libdir}/kamailio/modules/mediaproxy.so
%{_libdir}/kamailio/modules/mi_datagram.so
%{_libdir}/kamailio/modules/mi_fifo.so
%{_libdir}/kamailio/modules/mi_rpc.so
%{_libdir}/kamailio/modules/mohqueue.so
%{_libdir}/kamailio/modules/mqueue.so
%{_libdir}/kamailio/modules/msilo.so
%{_libdir}/kamailio/modules/msrp.so
%{_libdir}/kamailio/modules/mtree.so
%{_libdir}/kamailio/modules/nat_traversal.so
%{_libdir}/kamailio/modules/nathelper.so
%{_libdir}/kamailio/modules/nosip.so
%{_libdir}/kamailio/modules/p_usrloc.so
%{_libdir}/kamailio/modules/path.so
%{_libdir}/kamailio/modules/pdb.so
%{_libdir}/kamailio/modules/pdt.so
%{_libdir}/kamailio/modules/permissions.so
%{_libdir}/kamailio/modules/pike.so
%{_libdir}/kamailio/modules/pipelimit.so
%{_libdir}/kamailio/modules/prefix_route.so
%{_libdir}/kamailio/modules/pv.so
%{_libdir}/kamailio/modules/qos.so
%{_libdir}/kamailio/modules/ratelimit.so
%{_libdir}/kamailio/modules/regex.so
%{_libdir}/kamailio/modules/registrar.so
%{_libdir}/kamailio/modules/rr.so
%{_libdir}/kamailio/modules/rtimer.so
%{_libdir}/kamailio/modules/rtjson.so
%{_libdir}/kamailio/modules/rtpproxy.so
%{_libdir}/kamailio/modules/rtpengine.so
%{_libdir}/kamailio/modules/sanity.so
%{_libdir}/kamailio/modules/sca.so
%{_libdir}/kamailio/modules/seas.so
%{_libdir}/kamailio/modules/sdpops.so
%{_libdir}/kamailio/modules/sipcapture.so
%{_libdir}/kamailio/modules/sipt.so
%{_libdir}/kamailio/modules/siptrace.so
%{_libdir}/kamailio/modules/siputils.so
%{_libdir}/kamailio/modules/speeddial.so
%{_libdir}/kamailio/modules/sl.so
%{_libdir}/kamailio/modules/sms.so
%{_libdir}/kamailio/modules/sqlops.so
%{_libdir}/kamailio/modules/sst.so
%{_libdir}/kamailio/modules/statistics.so
%{_libdir}/kamailio/modules/statsd.so
%{_libdir}/kamailio/modules/stun.so
%{_libdir}/kamailio/modules/tcpops.so
%{_libdir}/kamailio/modules/textops.so
%{_libdir}/kamailio/modules/textopsx.so
%{_libdir}/kamailio/modules/timer.so
%{_libdir}/kamailio/modules/tm.so
%{_libdir}/kamailio/modules/tmrec.so
%{_libdir}/kamailio/modules/tmx.so
%{_libdir}/kamailio/modules/topoh.so
%{_libdir}/kamailio/modules/tsilo.so
%{_libdir}/kamailio/modules/uac.so
%{_libdir}/kamailio/modules/uac_redirect.so
%{_libdir}/kamailio/modules/uid_auth_db.so
%{_libdir}/kamailio/modules/uid_avp_db.so
%{_libdir}/kamailio/modules/uid_domain.so
%{_libdir}/kamailio/modules/uid_gflags.so
%{_libdir}/kamailio/modules/uid_uri_db.so
%{_libdir}/kamailio/modules/uri_db.so
%{_libdir}/kamailio/modules/userblacklist.so
%{_libdir}/kamailio/modules/usrloc.so
%{_libdir}/kamailio/modules/xhttp.so
%{_libdir}/kamailio/modules/xhttp_rpc.so
%{_libdir}/kamailio/modules/xlog.so
%{_libdir}/kamailio/modules/xprint.so


%{_sbindir}/kamailio
%{_sbindir}/kamctl
%{_sbindir}/kamdbctl
%{_sbindir}/kamcmd
%dir %{_libdir}/kamailio/kamctl
%dir %{_libdir}/kamailio/kamctl/dbtextdb
%if 0%{?suse_version}
%{_libdir}/kamailio/kamctl/dbtextdb/dbtextdb.py
%else
%{_libdir}/kamailio/kamctl/dbtextdb/dbtextdb.py
%{_libdir}/kamailio/kamctl/dbtextdb/dbtextdb.pyc
%{_libdir}/kamailio/kamctl/dbtextdb/dbtextdb.pyo
%endif
%{_libdir}/kamailio/kamctl/kamctl.base
%{_libdir}/kamailio/kamctl/kamctl.ctlbase
%{_libdir}/kamailio/kamctl/kamctl.dbtext
%{_libdir}/kamailio/kamctl/kamctl.fifo
%{_libdir}/kamailio/kamctl/kamctl.ser
%{_libdir}/kamailio/kamctl/kamctl.ser_mi
%{_libdir}/kamailio/kamctl/kamctl.sqlbase
%{_libdir}/kamailio/kamctl/kamctl.unixsock
%{_libdir}/kamailio/kamctl/kamdbctl.base
%{_libdir}/kamailio/kamctl/kamdbctl.dbtext

%{_mandir}/man5/*
%{_mandir}/man8/*

%dir %{_sharedir}/kamailio
%dir %{_sharedir}/kamailio/dbtext
%dir %{_sharedir}/kamailio/dbtext/kamailio
%{_sharedir}/kamailio/dbtext/kamailio/*


%files		auth-ephemeral
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.auth_ephemeral
%{_libdir}/kamailio/modules/auth_ephemeral.so


%if 0%{_with_bdb}
%files bdb
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.db_berkeley
%{_sbindir}/kambdb_recover
%{_libdir}/kamailio/modules/db_berkeley.so
%{_libdir}/kamailio/kamctl/kamctl.db_berkeley
%{_libdir}/kamailio/kamctl/kamdbctl.db_berkeley
%dir %{_datadir}/kamailio/db_berkeley
%{_datadir}/kamailio/db_berkeley/*
%endif


%if 0%{_with_carrierroute}
%files carrierroute
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.carrierroute
%{_libdir}/kamailio/modules/carrierroute.so
%endif


%if 0%{_with_cnxcc}
%files cnxcc
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.cnxcc
%{_libdir}/kamailio/modules/cnxcc.so
%endif


%files cpl
%defattr(-,root,root)
%{_docdir}/kamailio/modules/README.cpl-c
%{_libdir}/kamailio/modules/cpl-c.so


%if 0%{_with_dnssec}
%files		dnssec
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.dnssec
%{_libdir}/kamailio/modules/dnssec.so
%endif


%if 0%{_with_erlang}
%files		erlang
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.erlang
%{_libdir}/kamailio/modules/erlang.so
%endif


%if 0%{_with_ev}
%files		ev
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.evapi
%{_libdir}/kamailio/modules/evapi.so
%endif


%if 0%{_with_geoip}
%files geoip
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.geoip
%{_libdir}/kamailio/modules/geoip.so
%endif


%files		gzcompress
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.gzcompress
%{_libdir}/kamailio/modules/gzcompress.so


%files ims
%defattr(-,root,root)
%{_libdir}/kamailio/libkamailio_ims.so
%{_libdir}/kamailio/libkamailio_ims.so.0
%{_libdir}/kamailio/libkamailio_ims.so.0.1

%doc %{_docdir}/kamailio/modules/README.cdp
%{_libdir}/kamailio/modules/cdp.so
%doc %{_docdir}/kamailio/modules/README.cdp_avp
%{_libdir}/kamailio/modules/cdp_avp.so
%doc %{_docdir}/kamailio/modules/README.dialog_ng
%{_libdir}/kamailio/modules/dialog_ng.so
%doc %{_docdir}/kamailio/modules/README.ims_auth
%{_libdir}/kamailio/modules/ims_auth.so
%doc %{_docdir}/kamailio/modules/README.ims_charging
%{_libdir}/kamailio/modules/ims_charging.so
%doc %{_docdir}/kamailio/modules/README.ims_icscf
%{_libdir}/kamailio/modules/ims_icscf.so
%doc %{_docdir}/kamailio/modules/README.ims_isc
%{_libdir}/kamailio/modules/ims_isc.so
%doc %{_docdir}/kamailio/modules/README.ims_qos
%{_libdir}/kamailio/modules/ims_qos.so
#%doc %{_docdir}/kamailio/modules/README.ims_registrar_pcscf
%{_libdir}/kamailio/modules/ims_registrar_pcscf.so
#%doc %{_docdir}/kamailio/modules/README.ims_registrar_scscf
%{_libdir}/kamailio/modules/ims_registrar_scscf.so
%doc %{_docdir}/kamailio/modules/README.ims_usrloc_pcscf
%{_libdir}/kamailio/modules/ims_usrloc_pcscf.so
#%doc %{_docdir}/kamailio/modules/README.ims_usrloc_scscf
%{_libdir}/kamailio/modules/ims_usrloc_scscf.so


%if 0%{_with_java}
%files		java
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.app_java
%{_libdir}/kamailio/modules/app_java.so
%dir %{_libdir}/kamailio/java
%{_libdir}/kamailio/java/Kamailio.class
%{_libdir}/kamailio/java/kamailio.jar
%endif


%if 0%{_with_jansson}
%files jansson
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.jansson
%doc %{_docdir}/kamailio/modules/README.janssonrpc-c
%{_libdir}/kamailio/modules/jansson.so
%{_libdir}/kamailio/modules/janssonrpc-c.so
%endif


%if 0%{_with_json}
%files json
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.json
%doc %{_docdir}/kamailio/modules/README.jsonrpc-c
%{_libdir}/kamailio/modules/json.so
%{_libdir}/kamailio/modules/jsonrpc-c.so
%endif


%if 0%{_with_kazoo}
%files		kazoo
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.kazoo
%{_libdir}/kamailio/modules/kazoo.so
%endif


%if 0%{_with_ldap}
%files ldap
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.db2_ldap
%doc %{_docdir}/kamailio/modules/README.h350
%doc %{_docdir}/kamailio/modules/README.ldap
%{_libdir}/kamailio/modules/db2_ldap.so
%{_libdir}/kamailio/modules/h350.so
%{_libdir}/kamailio/modules/ldap.so
%endif


%if 0%{_with_lua}
%files lua
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.app_lua
%{_libdir}/kamailio/modules/app_lua.so
%endif


%if 0%{_with_memcached}
%files memcached
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.memcached
%{_libdir}/kamailio/modules/memcached.so
%endif


%if 0%{_with_mongodb}
%files		mongodb
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.db_mongodb
%doc %{_docdir}/kamailio/modules/README.ndb_mongodb
%{_libdir}/kamailio/modules/db_mongodb.so
%{_libdir}/kamailio/modules/ndb_mongodb.so
%endif


%if 0%{_with_mi_xmlrpc}
%files mi_xmlrpc
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.mi_xmlrpc
%{_libdir}/kamailio/modules/mi_xmlrpc.so
%endif


%if 0%{_with_mono}
%files mono
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.app_mono
%{_libdir}/kamailio/modules/app_mono.so
%endif


%files mysql
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.db_mysql
%{_libdir}/kamailio/modules/db_mysql.so
%{_libdir}/kamailio/kamctl/kamctl.mysql
%{_libdir}/kamailio/kamctl/kamdbctl.mysql
%dir %{_sharedir}/kamailio/mysql
%{_sharedir}/kamailio/mysql/*


%files outbound
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.outbound
%{_libdir}/kamailio/modules/outbound.so


%if 0%{_with_perl}
%files perl
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.app_perl
%doc %{_docdir}/kamailio/modules/README.db_perlvdb
%{_libdir}/kamailio/modules/app_perl.so
%{_libdir}/kamailio/modules/db_perlvdb.so
%dir %{_libdir}/kamailio/perl
%{_libdir}/kamailio/perl/Kamailio.pm
%dir %{_libdir}/kamailio/perl/Kamailio
%{_libdir}/kamailio/perl/Kamailio/Constants.pm
%{_libdir}/kamailio/perl/Kamailio/Message.pm
%{_libdir}/kamailio/perl/Kamailio/VDB.pm
%dir %{_libdir}/kamailio/perl/Kamailio/LDAPUtils
%{_libdir}/kamailio/perl/Kamailio/LDAPUtils/LDAPConf.pm
%{_libdir}/kamailio/perl/Kamailio/LDAPUtils/LDAPConnection.pm
%dir %{_libdir}/kamailio/perl/Kamailio/Utils
%{_libdir}/kamailio/perl/Kamailio/Utils/Debug.pm
%{_libdir}/kamailio/perl/Kamailio/Utils/PhoneNumbers.pm
%dir %{_libdir}/kamailio/perl/Kamailio/VDB
%{_libdir}/kamailio/perl/Kamailio/VDB/Column.pm
%{_libdir}/kamailio/perl/Kamailio/VDB/Pair.pm
%{_libdir}/kamailio/perl/Kamailio/VDB/ReqCond.pm
%{_libdir}/kamailio/perl/Kamailio/VDB/Result.pm
%{_libdir}/kamailio/perl/Kamailio/VDB/VTab.pm
%{_libdir}/kamailio/perl/Kamailio/VDB/Value.pm
%dir %{_libdir}/kamailio/perl/Kamailio/VDB/Adapter
%{_libdir}/kamailio/perl/Kamailio/VDB/Adapter/AccountingSIPtrace.pm
%{_libdir}/kamailio/perl/Kamailio/VDB/Adapter/Alias.pm
%{_libdir}/kamailio/perl/Kamailio/VDB/Adapter/Auth.pm
%{_libdir}/kamailio/perl/Kamailio/VDB/Adapter/Describe.pm
%{_libdir}/kamailio/perl/Kamailio/VDB/Adapter/Speeddial.pm
%{_libdir}/kamailio/perl/Kamailio/VDB/Adapter/TableVersions.pm
%endif


%files postgres
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.db_postgres
%{_libdir}/kamailio/modules/db_postgres.so
%{_libdir}/kamailio/kamctl/kamctl.pgsql
%{_libdir}/kamailio/kamctl/kamdbctl.pgsql
%dir %{_sharedir}/kamailio/postgres
%{_sharedir}/kamailio/postgres/*


%files presence
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.presence
%doc %{_docdir}/kamailio/modules/README.presence_conference
%doc %{_docdir}/kamailio/modules/README.presence_dialoginfo
%doc %{_docdir}/kamailio/modules/README.presence_mwi
%doc %{_docdir}/kamailio/modules/README.presence_profile
%doc %{_docdir}/kamailio/modules/README.presence_reginfo
%doc %{_docdir}/kamailio/modules/README.presence_xml
%doc %{_docdir}/kamailio/modules/README.pua
%doc %{_docdir}/kamailio/modules/README.pua_bla
%doc %{_docdir}/kamailio/modules/README.pua_dialoginfo
%doc %{_docdir}/kamailio/modules/README.pua_mi
%doc %{_docdir}/kamailio/modules/README.pua_reginfo
%doc %{_docdir}/kamailio/modules/README.pua_usrloc
%doc %{_docdir}/kamailio/modules/README.pua_xmpp
%doc %{_docdir}/kamailio/modules/README.rls
%doc %{_docdir}/kamailio/modules/README.xcap_client
%doc %{_docdir}/kamailio/modules/README.xcap_server
%{_libdir}/kamailio/modules/presence.so
%{_libdir}/kamailio/modules/presence_conference.so
%{_libdir}/kamailio/modules/presence_dialoginfo.so
%{_libdir}/kamailio/modules/presence_mwi.so
%{_libdir}/kamailio/modules/presence_profile.so
%{_libdir}/kamailio/modules/presence_reginfo.so
%{_libdir}/kamailio/modules/presence_xml.so
%{_libdir}/kamailio/modules/pua.so
%{_libdir}/kamailio/modules/pua_bla.so
%{_libdir}/kamailio/modules/pua_dialoginfo.so
%{_libdir}/kamailio/modules/pua_mi.so
%{_libdir}/kamailio/modules/pua_reginfo.so
%{_libdir}/kamailio/modules/pua_usrloc.so
%{_libdir}/kamailio/modules/pua_xmpp.so
%{_libdir}/kamailio/modules/rls.so
%{_libdir}/kamailio/modules/xcap_client.so
%{_libdir}/kamailio/modules/xcap_server.so


%if 0%{_with_purple}
%files purple
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.purple
%{_libdir}/kamailio/modules/purple.so
%endif


%files python
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.app_python
%{_libdir}/kamailio/modules/app_python.so


%if 0%{_with_radius}
%files radius
%defattr(-,root,root)
%{_docdir}/kamailio/modules/README.acc_radius
%{_docdir}/kamailio/modules/README.auth_radius
%{_docdir}/kamailio/modules/README.misc_radius
%{_docdir}/kamailio/modules/README.peering
%{_libdir}/kamailio/modules/acc_radius.so
%{_libdir}/kamailio/modules/auth_radius.so
%{_libdir}/kamailio/modules/misc_radius.so
%{_libdir}/kamailio/modules/peering.so
%endif


%if 0%{_with_sctp}
%files		sctp
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.sctp
%{_libdir}/kamailio/modules/sctp.so
%endif


%if 0%{_with_snmp}
%files snmpstats
%defattr(-,root,root)
%{_docdir}/kamailio/modules/README.snmpstats
%{_libdir}/kamailio/modules/snmpstats.so
%dir %{_sharedir}/snmp
%dir %{_sharedir}/snmp/mibs
%{_sharedir}/snmp/mibs/*
%endif


%if 0%{_with_sqlite}
%files sqlite
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.db_sqlite
%{_libdir}/kamailio/modules/db_sqlite.so
%{_libdir}/kamailio/kamctl/kamctl.sqlite
%{_libdir}/kamailio/kamctl/kamdbctl.sqlite
%dir %{_sharedir}/kamailio/db_sqlite
%{_sharedir}/kamailio/db_sqlite/*
%endif


%files tls
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.auth_identity
%doc %{_docdir}/kamailio/modules/README.tls
%{_libdir}/kamailio/modules/auth_identity.so
%{_libdir}/kamailio/modules/tls.so


%files unixodbc
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.db_unixodbc
%{_libdir}/kamailio/modules/db_unixodbc.so


%files utils
%defattr(-,root,root)
%{_docdir}/kamailio/modules/README.utils
%{_libdir}/kamailio/modules/utils.so


%if 0%{_with_uuid}
%files		uuid
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.uuid
%{_libdir}/kamailio/modules/uuid.so
%endif


%if 0%{_with_websocket}
%files websocket
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.websocket
%{_libdir}/kamailio/modules/websocket.so
%endif


%files xml
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.xhttp_pi
%{_libdir}/kamailio/modules/xhttp_pi.so
%dir %{_datadir}/kamailio/xhttp_pi
%{_datadir}/kamailio/xhttp_pi/*
%doc %{_docdir}/kamailio/modules/README.xmlops
%{_libdir}/kamailio/modules/xmlops.so
%doc %{_docdir}/kamailio/modules/README.xmlrpc
%{_libdir}/kamailio/modules/xmlrpc.so


%files xmpp
%defattr(-,root,root)
%doc %{_docdir}/kamailio/modules/README.xmpp
%{_libdir}/kamailio/modules/xmpp.so


%changelog
* Thu Jun  4 2015 miconda@gmail.com
- Update for release series 4.3.x
* Thu Oct 16 2014 miconda@gmail.com
- Update for release series 4.2.x
* Mon Dec  2 2013 miconda@gmail.com
- Update for release series 4.1.x
* Mon Mar 11 2013 miconda@gmail.com
- Update for release series 4.0.x
* Sun Feb 17 2013 jengelh@inai.de
- Avoid useless indirection with %%name, %%ver and %%rel
- Kill Packager tag, this ought not to be used (inconveniences
  secondary builders) and is overwritten in OBS anyway
- Remove redundant clean sections
* Sun Feb 17 2013 jengelh@inai.de
- Changelog ought to be in .changes, not .spec
- Remove old tarballs
* Mon Jun 18 2012 miconda@gmail.com
- Update for release series 3.3.x
* Wed Sep 21 2011 miconda@gmail.com
- Update for OpenSUSE Build System (3.1.5)
* Sat Mar 19 2011 miconda@gmail.com
- Update for OpenSUSE Build System (3.1.2)
* Mon Oct  4 2010 osas@voipembedded.com
- Update for kamailio 3.1 (3.1.0)
* Tue Mar 23 2010 osas@voipembedded.com
- First version of the spec file for kamailio 3.0
