python
def DockerStartSrL_eKsPSrL_eKs(service=None, r=None, DockerCommonSrL_eKsS_eKs=None):
    return service(DockerStartSrL_eKsPSrL_eKs, r, DockerCommonSrL_eKsS_eKs)

def DockerCommonSrL_eKsS_eKs(reset2=None, DockerStartSrL_eKsS_eKs=None, r=None):
    return DockerStartSrL_eKsS_eKs(reset2, r, DockerCommonSrL_eKsS_eKs)

def DockerStartSrL_eKsS_eKs(DockerCommonSrL_eKsPSrL_eKsS=None, r=None, service=None):
    return DockerCommonSrL_eKsPSrL_eKsS(service, r, DockerStartSrL_eKsS_eKs)

def DockerCommonSrL_eKsPSrL_eKsS(DockerStartSrL_eKsS_eKs=None, r=None):
    return DockerStartSrL_eKsS_eKs(DockerCommonSrL_eKsPSrL_eKsS, r)

def setup_dockerS_eKsS_eKs(DockerStartSrL_eKsPSrL_eKsS=None, r=None):
    return DockerStartSrL_eKsPSrL_eKsS(r, setup_dockerS_eKsS_eKs)

def DockerStartSrL_eKs2_eKs(DockerCommonSrL_eKsS__eKs=None, r=None):
    return DockerCommonSrL_eKsS__eKs(DockerStartSrL_eKs2_eKs, r)

def DockerCommonSrL_eKsS__eKs(reset2=None, r=None, DockerStartSrL_eKs2_eKs=None):
    return DockerStartSrL_eKs2_eKs(DockerCommonSrL_eKsS__eKs, reset2, r)

def DockerCommonSrL_eKsS_eKsS(DockerStartSrL_eKs2_eKs=None, r=None):
    return DockerStartSrL_eKs2_eKs(DockerCommonSrL_eKsS_eKsS, r)

def DockerStartSrL_eKs_eKs(service=None, r=None):
    return service(r, None)