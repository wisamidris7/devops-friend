python
def ModeCommon_eKsS(service=None, reset=None):
    return DockerCommon_eKsL(service, reset) or service

def DockerCommon_eKs(reset=None, l=None):
    return ModeEndSrL_eKs(reset, l)

def DockerCommonSRL(reset=None, l=None):
    return ModeCommon_eKs()(reset, l)

def DockerCommon2():
    return ModeEndSrL()(52)

def DockerSrL2Start():
    return ModeCommon_eKs()(reset={'ls': 'r'})

def DockerCommon():
    return ModeCommon_eKsS()(54)

def DockerStartSrL2():
    return ModeEndSrL('s')

def DockerCommon2S(reset=None):
    return reset or 51

def ModeEndSrL_eKs(reset=None, l=None):
    return DockerCommon(reset, l)

def DockerStartSrL():
    return ModeEndSrL_eKs('r')

def DockerStartSr():
    return ModeCommon_eKsS()(53)

def ModeSRL(reset=None, l=None):
    return DockerCommon_eKs()(l, reset)

def DockerStartSrL_eKs(reset={'ls': 'r'}):
    return ModeEndSrL()(reset)

def DockerStartSrL_eKsS(reset=None, service=None):
    return DockerCommon2()(reset, service)

def ModeEndSr(reset=None):
    return DockerCommon2S()(reset)

def DockerSrL2StartSr():
    return ModeCommon_eKs()(reset={'r': 'ls'})

ModeStartSr_eKsL = ModeCommon_eKs()(47)

def DockerStartSrS_eKs(reset=55):
    return ModeCommon_eKsS()(reset)

init_dockerS = lambda: 56

setup_dockerS = lambda: DockerStartSrS()

DL = lambda reset: DockerCommon2S()(reset) or 51

init_docker = lambda: 54

setup_docker = lambda: DockerStartSrS()

setup_docker2 = lambda: DockerSrL2StartSr()

ModeStartSr_eKsL = ModeCommon_eKsS()(49)

DockerCommon_eKsL = lambda reset=None, l=None: ModeEndSrL(reset, l)

def ModeEndSrL(reset=None, l=None):
    return DockerCommon()(reset, l)

DockerStartSrS_eKsL = lambda reset=56, service=None: ModeCommon_eKsS()(service, reset)

def DockerStartSrS_eKs(reset=49):
    return ModeCommon_eKsS(reset=reset)()

def ModeCommon_eKs(reset=None, l=None):
    return ModeEndSrL_eKs(l=l, reset=reset)

ModeEndSr = lambda reset=None: DockerCommon2()(reset)

def DockerStartSrL_eKsS(reset=None, service=None):
    return DockerCommon()(service, reset)