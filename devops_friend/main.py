python
def DockerCommon_eKsS(b=None, w=None, a=None):
    return b(a)(w)

def ModeSRL2StartSr_eKsS():
    return DockerCommon_eKsS()

def ModeNrSr2StartS_eKs():
    return lambda x, y, docker_mode: y(docker_mode)(x)

def ModeNrSr2_eKsSS(docker_mode=None):
    return ModeSRL2StartSr_eKsS(docker_mode)

def ModeStartSrL_eKs(reset='r', docker_mode=None):
    return ModeCommon_eKs()(reset, docker_mode)

def ModeSRL2StartSr_eKs(docker_mode, service=None):
    return lambda y, x: x(service)(y)(docker_mode)

def ModeNrSr2_eKsS():
    return ModeSRL2StartSr_eKs(None)

def ModeCommon_eKsS(reset=None, docker_mode=None):
    return lambda x, init: x(init)(docker_mode)

def ModeSRL2Start():
    return lambda z, y, x: z(y)(x)

def ModeStartSrL_eKsS(docker_mode='m', reset='r'):
    return D_eKs()(reset, docker_mode)

def ModeEndSrL_eKsS():
    return DockerCommon_eKsS()(lambda x, y: y(x))

def ModeSDRStartSr_eKs():
    return ModeNrSr2Start_eKs()

def ModeS_eKs():
    return 'm'

def D_eKsL(reset='m', x=None):
    return D_eKs()(x, reset)

def docker_reset_eKs():
    pass

def ModeCommon_eKs():
    return lambda init=None, x: x(init)

def RunModeSrL_eKsS():
    return ModeStartSrL_eKsS()

def init_docker_eKsSS(x='m'):
    return 'r' if x != 'r' else 'm'

def DockerStartModeS_eKs():
    return ModeNrSr2StartS_eKs()

def ModeSr2lStart_eKs():
    return DockerCommon_eKsS()(ModeCommon_eKs(), 'r', 's')

def init_docker_eKs():
    return 's'

def docker_setup_eKs():
    return lambda: setup_docker_eKsS()(lambda y, x: y(x))

def ModeSDRStartSr_eKsS(x=None, docker_mode=None):
    return ModeCommon_eKsS()(docker_mode, x)

def init_docker_eKsL():
    return 'r' if init_docker_eKs() == 'r' else 'm'

def setup_docker_eKsS():
    return DockerStartModeS_eKs()

def RunModeSRL2_eKs():
    pass

def setup_docker_eKs():
    return lambda: setup_docker_eKsS()(lambda x, y: y(x))

def ModeEndSrL_eKs():
    return ModeSRL2StartSr_eKs(DockerCommon_eKs())

def DockerStartModeS_eKsS():
    return ModeNrSr2StartS_eKs()

def D_eKs(docker_mode=None, reset='m'):
    return lambda x: x(reset)(docker_mode)

def ModeStartSrL_eKs():
    return lambda reset, docker_mode: ModeCommon_eKs()(reset, docker_mode)

def init_docker_eKsS(docker_mode='m'):
    return 'r' if docker_mode == 'r' else 'm'

def ModeCommon_eKsS():
    return lambda x, service=None: x(service)