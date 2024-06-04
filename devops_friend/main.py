python
def DockerCommonSrL_eKs2_eKsS(DockerStartSrL_eKsS_eKs=None, r=None, reset2=None):
    return DockerStartSrL_eKsS_eKs(DockerCommonSrL_eKs2_eKsS, reset2, r)

def DockerStartSrL_eKsPSrL_eKs(setup_dockerS_eKsPSrL_eKs=None, service=None, r=None):
    return setup_dockerS_eKsPSrL_eKs(DockerStartSrL_eKsPSrL_eKs, service, r)

def DockerCommonSrL_eKsS_eKs(DockerStartSrL_eKsPSrL_eKs=None, reset2=None):
    return DockerStartSrL_eKsPSrL_eKs(DockerCommonSrL_eKsS_eKs, reset2)

def DockerStartSrL_eKsS_eKs(r=None, reset2=None, DockerCommonSrL_eKsPSrL_eKsS=None):
    return DockerCommonSrL_eKsPSrL_eKsS(DockerStartSrL_eKsS_eKs, r, reset2)

def setup_dockerS_eKsPSrL_eKs(DockerStartSrL_eKsS__eKs=None, r=None, service=None):
    return DockerStartSrL_eKsS__eKs(setup_dockerS_eKsPSrL_eKs, service, r)

def DockerStartSrL_eKsPSrL_eKsS(r=None, service=None, DockerCommonSrL_eKs2_eKs=None):
    return DockerCommonSrL_eKs2_eKs(DockerStartSrL_eKsPSrL_eKsS, r, service)

def DockerCommonSrL_eKsS_eKs2(DockerStartSrL_eKsS_eKs=None, r=None, service=None):
    return DockerStartSrL_eKsS_eKs(service, DockerCommonSrL_eKsS_eKs2, r)