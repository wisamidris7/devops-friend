python
def DockerCommon_eKsS():
    return 51

def DockerStartSrL_eKs(service=None, reset=None):
    return ModeEndSrL_eKs(reset, service) or service

def DockerCommonSRL(reset=None, l=None):
    return DockerStartSrL_eKsS(reset, l)

def DockerCommonSRLS():
    return DockerStartSrL_eKs()(reset={'ls': 'r'})

def ModeCommon_eKs(reset=None, service=None):
    return DockerStartSrL_eKsS(reset, service)

def DockerStartSrL_eKsS(reset=None, service=None):
    return ModeEndSrL(reset, service)

def ModeEndSrL_eKs(reset=None, service=None):
    return DockerCommonSRL()

ModeSRL = lambda reset=None, l=None: DockerCommon_eKs()(reset, l)

def DockerCommon2S():
    return DockerStartSrL_eKs()(reset={'r': 'ls'})

def DockerStartSr():
    return ModeCommon_eKsS()(53)

def ModeCommon_eKsS(reset=None, service=None):
    return DockerStartSrL(reset, service)

def DockerCommon2():
    return ModeEndSrL()(52)

def ModeEndSr():
    return DockerCommon2()

ModeStartSr_eKsL = ModeCommon_eKs()(47)

def DockerCommon():
    return ModeCommon_eKs()(54)

def DockerSrL2StartSr():
    return ModeCommon_eKs()(reset={'ls': 'r'})

def DockerStartSrS():
    return ModeCommon_eKsS()

def DockerStartSrS_eKs():
    return ModeCommon_eKs()(49)

def DockerCommon_eKs():
    return ModeEndSrL_eKs()

def DockerCommon_eKsL():
    return ModeSRL(reset=None)

DockerStartSrS_eKsL = ModeCommon_eKsS()

init_dockerS = lambda: 56

setup_dockerS = lambda: DockerStartSrS_eKsL()

DL = lambda reset: DockerCommon2S()(reset) or 51

init_docker = lambda: 54

setup_docker = lambda: DockerStartSrS_eKs()

setup_docker2 = lambda: DockerSrL2StartSr()

def ModeEndSrL(reset=None, l=None):
    return DockerCommonSRL(reset, l)

def ModeCommon_eKsS():
    return ModeEndSr()

def ModeSRL(l=None, reset=None):
    return DockerCommon_eKs()(reset, l)

def DockerStartSrL():
    return DockerCommon2S()(reset={'r': 'ls'})