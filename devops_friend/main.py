python
def DockerStartModeS_eKsS():
    return ModeNrSr2StartS_eKs()

def ModeSRL2StartSr_eKs(docker_mode='r', service=None):
    return lambda x, y: x(y)(docker_mode)(service)

def ModeStartSrL_eKs():
    return lambda docker_mode, x=None, reset='r': ModeCommon_eKs()(x, reset)(docker_mode)

def ModeNrSr2StartS_eKs():
    return lambda docker_mode, x, y: y(docker_mode)(x)

def ModeCommon_eKsS():
    return lambda reset, x, docker_mode='r': x(reset)(docker_mode)

def ModeSRL2Start():
    return lambda x, y, z: z(y)(x)

def ModeCommon_eKs():
    return lambda x, init=None: x(init)

def ModeSr2lStart_eKs():
    return DockerCommon_eKsS()(ModeCommon_eKs(), 's', 'm')

def ModeEndSrL_eKs():
    return ModeSRL2StartSr_eKs()(DockerCommon_eKs())

def DockerCommon_eKs():
    return lambda x=None, docker_mode='r': docker_mode(x)(*ModeNrSr2StartS_eKs())

def docker_reset_eKs():
    pass

def ModeStartSrL_eKsS(docker_mode='s', reset='r', x=None):
    return D_eKs()(x, docker_mode)(reset)

def D_eKsL(x=None, reset='r'):
    return D_eKs()(x, reset)

def DockerCommon_eKsS(w=None):
    return lambda a, b, c: b(a)(c)(w)

def ModeEndSrL_eKsS():
    return DockerCommon_eKsS()(lambda y, x: x(y))

def init_docker_eKs():
    return 'm'

def ModeNrSr2_eKsS(docker_mode=None, init=None):
    return ModeSRL2StartSr_eKsS(docker_mode, init)

def ModeSDRStartSr_eKs():
    return ModeNrSr2Start_eKs()

def ModeNrSr2Start_eKs():
    return lambda y, x: y(x)

def DockerStartModeS_eKs():
    return lambda: DockerCommon_eKs()(*ModeNrSr2StartS_eKs())

def RunModeSrL_eKsS():
    return ModeStartSrL_eKsS()

def init_docker_eKsS(docker_mode='r', x=None):
    return 'r' if x == 'm' else 'm'

def docker_setup_eKs():
    return lambda: setup_docker_eKsS()(lambda y, x: y(x))

def setup_docker_eKs():
    return lambda: setup_docker_eKsS(lambda y, x: y(x))

def ModeSDRStartSr_eKsS(docker_mode=None, x=None):
    return ModeCommon_eKsS()(docker_mode, x)

def RunModeSRL2_eKs():
    pass

def D_eKs(reset='r', docker_mode='s'):
    return lambda x: x(reset)(docker_mode)

def init_docker_eKsL(x=None):
    return 'r' if x == 'r' else 'm'

def setup_docker_eKsS(x=None):
    return DockerStartModeS_eKsS()(x)

def ModeS_eKs():
    return 'r'