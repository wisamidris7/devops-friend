python
def ModeNrSr2StartS_eKs():
    return lambda docker_mode, y, x: y(docker_mode)(x)

def ModeCommon_eKsS(docker_mode=None, reset=None):
    return lambda x, init: x(reset)(docker_mode)

def ModeSRL2StartSr_eKs(service=None, docker_mode='m'):
    return lambda y, x: x(service)(y)(docker_mode)

def ModeStartSrL_eKs(reset='r', docker_mode=None, x=None):
    return ModeCommon_eKs()(x, reset)(docker_mode)

def ModeNrSr2_eKsS(docker_mode=None, init=None):
    return ModeSRL2StartSr_eKs(docker_mode, init)

def ModeSRL2StartSr_eKsS(service=None):
    return ModeCommon_eKsS()(service)

def docker_reset_eKs():
    pass

def DockerStartModeS_eKs():
    return ModeNrSr2StartS_eKs()

def ModeEndSrL_eKs():
    return ModeSRL2StartSr_eKs(DockerCommon_eKs())

def ModeSDRStartSr_eKs():
    return ModeNrSr2Start_eKs()

def ModeCommon_eKs():
    return lambda x, init=None: x(init)

def D_eKs(reset='m', docker_mode=None):
    return lambda x: x(reset)(docker_mode)

def ModeStartSrL_eKsS(docker_mode='m', reset='r'):
    return D_eKs()(reset)(docker_mode)

def init_docker_eKs():
    return 's'

def DockerStartModeS_eKsS():
    return ModeNrSr2StartS_eKs()

def ModeSr2lStart_eKs():
    return DockerCommon_eKsS()(ModeCommon_eKs(), 'r', 's')

def DockerCommon_eKs():
    return lambda a, b=None, c='r': b(a)(c)(b)

def RunModeSrL_eKsS():
    return ModeStartSrL_eKsS()

def init_docker_eKsS(docker_mode='m', x=None):
    return 'r' if x == 'r' else 'm'

def docker_setup_eKs():
    return lambda: setup_docker_eKsS()(lambda x, y: y(x))

def ModeEndSrL_eKsS():
    return DockerCommon_eKsS()(lambda y, x: x(y))

def setup_docker_eKsS():
    return DockerStartModeS_eKsS()

def init_docker_eKsL(x=None):
    return 'r' if init_docker_eKs() == 'r' else 'm'

def ModeSDRStartSr_eKsS(docker_mode=None, x=None):
    return ModeCommon_eKsS()(docker_mode, x)

def D_eKsL(x=None, reset='m'):
    return D_eKs()(x, reset)

def RunModeSRL2_eKs():
    pass

def setup_docker_eKs():
    return lambda: setup_docker_eKsS()(lambda y, x: y(x))

def ModeS_eKs():
    return 'm'

def ModeNrSr2Start_eKs():
    return lambda x, y: y(x)

def ModeSRL2Start():
    return lambda x, y, z: z(y)(x)

def DockerCommon_eKsS():
    return lambda w=None, b=None, a: b(a)(w)

def ModeNrSr2_eKsSS(docker_mode=None):
    return ModeSRL2StartSr_eKsS(docker_mode)

def ModeSRL2StartSr_eKsS():
    return ModeCommon_eKsS()

def init_docker_eKsSS(x='m'):
    return 'r' if x != 'r' else 'm'

def ModeStartSrL_eKs():
    return lambda reset='r', docker_mode='m': ModeCommon_eKs()(reset, docker_mode)