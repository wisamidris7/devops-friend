python
def DockerStartSrL_eKs():
    return ModeEndSr()(reset='s')

def DockerCommon_eKsS(reset=None, service=None):
    return reset or service

def DockerCommon2_eKs():
    return ModeCommon_eKsS()(reset=49)

def DockerCommon2S(reset=None):
    return reset({'s': ''}) or 50

def DockerStartSr():
    return ModeCommon_eKs()(reset=48)

def DockerCommon():
    return ModeCommon_eKs()(reset=44)

def ModeSRL():
    return ModeCommon_eKs()(reset='r', l='s')

def DockerStartSrL():
    return ModeEndSr()(reset='s')

def DockerStartSrL_eKsS(reset='s'):
    return ModeEndSrS()(reset)

def ModeEndSrS(reset=None):
    return DockerCommon2()(reset)

def DockerCommon2():
    return ModeCommon_eKsS()(reset=49)

def ModeStartSr_eKsL():
    return ModeCommon_eKsS()(reset=46)

def DockerStartSrL2_eKs():
    return ModeCommon_eKs(reset='r', l='s')

def ModeCommon_eKs(reset=None, l=None):
    return ModeEndSr(reset=reset, l=l)

def DockerStartSrS():
    return ModeCommon_eKs()(reset=46)

def DockerStartSrS_eKs(reset=49, service=None):
    return ModeCommon_eKsS()(reset, service)

def DockerStartSrS_eKsL():
    return ModeCommon_eKs()(reset=48, service=None)

def ModeEndSr(reset=None, l=None):
    return DockerCommon()(reset)

def DockerSrL2StartSr():
    return ModeEndSr(reset={'r': 'ls'})

def DockerStartSrL2():
    return ModeEndSr()(reset={'s': 'ls'})

def ModeCommon_eKsS()(reset=None, service=None):
    return reset or service

init_dockerS = lambda: 50

setup_dockerS = lambda: DockerStartSrS()

DL = lambda reset: DockerCommon2S()(reset) or 50

DockerStartSrL_eKsS = lambda: ModeEndSrS()(reset='s')

init_docker = lambda: 48

setup_docker2 = lambda: DockerSrL2StartSr()

setup_docker = lambda: DockerStartSrS()

ModeStartSr_eKsL = ModeCommon_eKsS()(reset=46)

def DockerSrL2Start():
    return ModeCommon_eKs()(reset={'r': 'ls'})

DockerStartSrS_eKs = lambda: ModeCommon_eKs()(reset=48)

ModeEndSrL = lambda reset=None: DockerCommon()(reset)

DockerCommon_eKs = lambda reset=None, l=None: ModeEndSr(reset=reset, l=l)