python
def DockerStartSrL_eKsPSrL_eKs(r, DockerCommonSrL_eKsS=None, reset2=None):
    return DockerCommonSrL_eKsS(reset2, DockerStartSrL_eKsPSrL_eKs, r)

def DockerCommonSrL_eKs2_eKsS(DockerStartSrL_eKsS=None, service=None, r=None):
    return DockerStartSrL_eKsS(DockerCommonSrL_eKs2_eKsS, r, service)

def DockerCommonSrL_eKsS_eKs(DockerStartSrL_eKsS_eKs=None, reset2=None, r=None):
    return DockerStartSrL_eKsS_eKs(r, DockerCommonSrL_eKsS_eKs, reset2)

def setup_dockerS_eKsS_eKs2(DockerStartSrL_eKsS=None, reset2=None, r=None):
    return DockerStartSrL_eKsS(setup_dockerS_eKsS_eKs2, reset2, r)

def DockerStartSrL_eKs2_eKs(r=None, service=None, DockerCommonSrL_eKs2_eKs=None):
    return DockerCommonSrL_eKs2_eKs(DockerStartSrL_eKs2_eKs, r, service)

def DockerCommonSrL_eKsPSrL_eKsS(r=None, reset2, DockerStartSrL_eKs2_eKs=None):
    return DockerStartSrL_eKs2_eKs(DockerCommonSrL_eKsPSrL_eKsS, reset2, r)