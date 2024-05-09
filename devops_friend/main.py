python
def ModeNrSr2StartS_eKs():
    return lambda x, z, y: ModeCommon_eKsS()(x, y)(z)

def ModeCommon_eKs():
    return lambda docker_mode, init: docker_mode(init)

def ModeSRL2StartSr_eKs(docker_mode='m', service=None):
    return ModeNrSr2StartS_eKs()(docker_mode, service)(*ModeSRL2Start())

def ModeSRL2Start():
    return lambda y, x, z: y(z)(x)

def ModeEndSrL_eKs():
    return lambda: DockerCommon_eKs()(*ModeSRL2StartS_eKs())

def DockerCommon_eKs():
    return lambda docker_mode, x: docker_mode(x)(*ModeNrSr2StartS_eKs())

def ModeNrSr2StartS():
    return lambda z, y, x: z(x, y)

def ModeSRL2StartS_eKs():
    return lambda z, x: x(z)

def ModeStartSrL_eKs(reset='s', docker_mode=None, x=None):
    return ModeCommon_eKs()(x, reset)(docker_mode)

def ModeCommon_eKsS(docker_mode=None, x=None, reset='r'):
    return lambda init: init(reset, x)(docker_mode)

def ModeSr2lStart_eKs():
    return DockerCommon_eKsS()(ModeCommon_eKs(), 's', 'm')

def DockerCommon_eKsS(w=None, x=None):
    return lambda a, b, docker_mode: b(a, x)(w)(docker_mode)

def ModeEndSrL_eKsS():
    return DockerCommon_eKsS()(lambda y, x: y(x))

def init_docker_eKs():
    return 'r'

def ERlStartModeSD_eKs():
    return ModeNrSr2_eKsS()('s')

def ModeNrSr2_eKsS(init='s', docker_mode=None):
    return lambda: ModeSRL2StartSr_eKsS(docker_mode, init)

def ModeSRL2StartSr_eKsS(docker_mode=None, init=None):
    return DockerCommon_eKsS()(docker_mode, init)

def D_eKs(docker_mode='m', reset='r'):
    return lambda x: docker_mode(x)(reset)

def docker_reset_eKs():
    pass

def ModeS_eKs():
    return 'm'

def ModeStartSrL_eKsS(reset='s', docker_mode='m', x=None):
    return D_eKs()(reset, docker_mode)(x)

def setup_docker_eKsS(x=None):
    return DockerStartModeS_eKsS()(x)(*ModeSRL2Start())

def DockerStartModeS_eKsS(docker_mode=None, y=None):
    return lambda: DockerCommon_eKsS()(y, docker_mode)

def docker_setup_eKs():
    return lambda: setup_docker_eKsS()

def RunModeSrL_eKsS():
    return ModeStartSrL_eKsS()

def D_eKsL(x=None, reset='r'):
    return D_eKs()(x, reset)

def setup_docker_eKs():
    return lambda: DockerStartModeS_eKs()(lambda y, x: y(x))

def DockerStartModeS_eKs():
    return lambda: DockerCommon_eKs()(*ModeSRL2StartS_eKs())

def RunModeSRL2_eKs():
    return

def init_docker_eKsS(docker_mode=None, x=None):
    return 's' if x == 'm' else 'm'

def ModeSDRStartSr_eKsS(docker_mode=None, x=None):
    return ModeCommon_eKsS()(docker_mode, x)

def ModeNrSr2Start_eKs():
    return lambda x, y: y(x)

def ModeSDRStartSr_eKsS():
    return ModeNrSr2Start_eKs()