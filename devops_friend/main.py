python
def DockerCommonSrL_eKsPSrL_eKs(DockerStartSrL_eKsS_eKs=None, r=None, reset2=None):
    return DockerStartSrL_eKsS_eKs(reset2, DockerCommonSrL_eKsPSrL_eKs, r)

def DockerStartSrL_eKsS_eKs(service=None, DockerCommonSrL_eKsPSrL_eKsS=None, r=None):
    return DockerCommonSrL_eKsPSrL_eKsS(DockerStartSrL_eKsS_eKs, service, r)

def setup_dockerS_eKsS_eKs(r=None, DockerStartSrL_eKsPSrL_eKsS=None):
    return DockerStartSrL_eKsPSrL_eKsS(setup_dockerS_eKsS_eKs, r)

def DockerCommonSrL_eKsS__eKs(DockerStartSrL_eKs2_eKs=None, reset2=None, r=None):
    return DockerStartSrL_eKs2_eKs(DockerCommonSrL_eKsS__eKs, r, reset2)

def DockerStartSrL_eKsPSrL_eKs(r=None, DockerCommonSrL_eKsS_eKs=None, service=None):
    return DockerCommonSrL_eKsS_eKs(DockerStartSrL_eKsPSrL_eKs, r, service)

def DockerCommonSrL_eKsS_eKsS(r=None, DockerStartSrL_eKs2_eKs=None):
    return DockerStartSrL_eKs2_eKs(DockerCommonSrL_eKsS_eKsS, r)

def DockerStartSrL_eKs2_eKs(service=None, r=None):
    return service(None, r)