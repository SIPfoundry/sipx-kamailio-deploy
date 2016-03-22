kamailio_TAG = 2016.02
kamailio_PACKAGE_REVISION = $(shell ./revision-gen $(kamailio_TAG))
kamailio_VER = 4.3.3
kamailio_RPM_DEFS = \
	--define "VERSION_NUMBER $(kamailio_VER)" \
	--define "BUILD_NUMBER $(kamailio_PACKAGE_REVISION)"
kamailio_TARBALL = kamailio-$(kamailio_VER)_src.tar.gz
kamailio_SPEC = kamailio.spec

PROJECTVER=2016.02-stage
REPOHOST = stage.sipfoundry.org
REPOUSER = stage
PACKAGE = kamailio
REPOPATH = /var/stage/www-root/sipxecs/${PROJECTVER}/externals/CentOS_6/x86_64/
RPMPATH = RPMBUILD/RPMS/x86_64/*.rpm
SSH_OPTIONS = -v -o UserKnownHostsFile=./.known_hosts -o StrictHostKeyChecking=no
SCP_PARAMS = ${RPMPATH} ${REPOUSER}@${REPOHOST}:${REPOPATH}
SSH_PASS = sshpass -p `cat .sshpass`
CREATEREPO_PARAMS = ${REPOUSER}@${REPOHOST} createrepo ${REPOPATH}
MKDIR_PARAMS = ${REPOUSER}@${REPOHOST} mkdir -p ${REPOPATH}


all: rpm

rpm-dir:
	@rm -rf RPMBUILD; \
	mkdir -p RPMBUILD/{BUILD,SOURCES,RPMS,SRPMS,SPECS};
	

dist: rpm-dir
	cd kamailio; \
	git archive --format=tar --prefix kamailio-$(kamailio_VER)/ HEAD | gzip > ../RPMBUILD/SOURCES/$(kamailio_TARBALL)

rpm: dist
	cp kamailio.init kamailio.default RPMBUILD/SOURCES/; \
	cp $(kamailio_SPEC) RPMBUILD/SPECS/; pwd > RPMBUILD/SPECS/.topdir; cd RPMBUILD/SPECS/; \
	rpmbuild -ba  --define "%_topdir `cat .topdir`/RPMBUILD" $(kamailio_RPM_DEFS) kamailio.spec

docker-build:
	docker pull sipfoundrydev/sipx-docker-base-libs; \
	docker run -t --rm --name sipx-${PACKAGE}-builder  -v `pwd`:/BUILD sipfoundrydev/sipx-docker-base-libs \
	/bin/sh -c "cd /BUILD && yum update -y && yum install -y mongo-c-driver-devel && make";


deploy:
	ssh ${SSH_OPTIONS} ${MKDIR_PARAMS}; \
	if [[ $$? -ne 0 ]]; then \
		exit 1; \
	fi; \
	scp ${SSH_OPTIONS} -r ${SCP_PARAMS}; \
	if [[ $$? -ne 0 ]]; then \
		exit 1; \
	fi; \
	ssh ${SSH_OPTIONS} ${CREATEREPO_PARAMS}; \
	if [[ $$? -ne 0 ]]; then \
		exit 1; \
	fi;
