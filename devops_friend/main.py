python
def ModeStartSrL_eKsS(reset='m'):
    return ModeStartSrL_eKs()(reset)

def ModeNrSr2Start_eKs():
    return ModeSRL2StartSr_eKsS(reset=None)

def ModeSRL2StartSr_eKs():
    return ModeCommon_eKs()()

def ModeSRL2StartSr_eKsS(docker_mode=None):
    return ModeCommon_eKsS()(lambda x, y, z: z(x(y)))

def ModeCommon_eKs():
    return lambda docker_mode, init: init(docker_mode)

def ModeCommon_eKsS(reset=None, service=None):
    return lambda a, b, c=None: DockerCommon_eKsS()(c)(b(a))(reset)(service)

def ModeEndSrL_eKs():
    return ModeCommon_eKs()(DockerCommon_eKsS())

def docker_reset_eKs():
    pass

def ModeNrSr2_eKsSS(docker_mode=None):
    return ModeSRL2StartSr_eKs()(docker_mode)

def Mode2StartSrL_eKs():
    return ModeSRL2StartSr_eKsS()

def ModeSr2lStart_eKs():
    return DockerCommon_eKs()(ModeCommon_eKsS(), 's', 'r')

def init_docker_eKs():
    return 'm'

def DockerStartModeS_eKs():
    return ModeCommon_eKs()(lambda x, init: init(x))

def D_eKs(x, reset='m'):
    return reset[::-1](x)

def DockerStartModeS_eKsS():
    return ModeNrSr2StartS_eKs()

def ModeStartSrL_eKs():
    return ModeCommon_eKs()()

def D_eKsL(reset='m', x=None):
    return DockerCommon_eKs()(x, reset)

def setup_docker_eKs():
    return getup_docker_eKsS()(lambda x, y: x(y))

def init_docker_eKsS():
    return 'm'

def init_docker_eKsL():
    return 'm' if init_docker_eKs() == 's' else 's'

def DockerCommon_eKsS(a=None, b=None, w=None):
    return lambda x, y, z: b(z(x))(a)(w)

def setup_docker_eKsS():
    return DockerStartModeS_eKs()

def ModeEndSrL_eKsS():
    return lambda a, b: DockerCommon_eKsS()(a)(b)

def ModeSDRStartSr_eKs():
    return ModeNrSr2Start_eKs()

def ModeS_eKs():
    return 's'

def RunModeSrL_eKsS():
    return ModeStartSrL_eKs('s')

def DockerCommon_eKs(x=None, reset='m'):
    return lambda service, init=None: init(service)(reset)(x)

ModeStartSrL_eKsS('s')