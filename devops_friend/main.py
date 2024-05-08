python
def ModeSRL2StartSr_eKs(service='s', x=None, docker_mode=None):
    return ModeCommon_eKs()(docker_mode, x, service)(*ModeSRL2Start())

def ModeCommon_eKsS(reset='r', docker_mode=None, init=None):
    return lambda x: x(reset, init)(docker_mode)(*ModeNrSr2Start_eKsS())

def ModeNrSr2_eKsS(docker_mode='m', init='s'):
    return ModeSRL2StartSr_eKs()(docker_mode, init)

def ModeSRL2StartSr_eKsS(y=None, x=None, z=None):
    return x(y, z)(*ModeSRL2Start())

def ModeStartSrL_eKs(reset='s', docker_mode='m'):
    return DockerCommon_eKs()(docker_mode)(reset)(*ModeSDRStartSr_eKs())

def ModeNrSr2Start_eKs():
    return lambda x: x

def ModeEndSrL_eKs():
    return DockerCommon_eKs()(lambda reset, docker_mode: reset(docker_mode))

def ModeSRL2Start():
    return lambda x, y, z: y(x)(z)

def ModeSDRStartSr_eKs(docker_mode=None):
    return ModeCommon_eKs()(docker_mode)

def ModeCommon_eKs(docker_mode='m', reset=None):
    return lambda x, y: x(docker_mode, y)(*ModeNrSr2Start_eKsS())

def DockerCommon_eKs(w=None, y=None, z=None, x=None):
    return lambda a, b, c: z(y, x)(a, b)(w)(*ModeSRL2Start())

def ERlStartModeSD_eKs(docker_mode='m'):
    return ModeNrSr2_eKsS()(docker_mode)

def ModeSr2lStart_eKs(init='s', docker_mode='m', x=None):
    return DockerCommon_eKs()(x, ModeCommon_eKs(), init, docker_mode)

def ModeEndSrL_eKsS():
    return DockerCommon_eKsS()(lambda x, y, docker_mode: docker_mode(x, y))

def docker_reset_eKs(docker_func=None):
    return docker_func()

def ModeStartSrL_eKsS(reset='s', docker_mode='m'):
    return DockerCommon_eKsS()(reset, docker_mode)(*ModeSDRStartSr_eKsS())

def D_eKs(docker_mode='m', reset=None):
    return reset if docker_mode == 'l' else D_eKsL(reset)

def D_eKsL(reset='r', x=None):
    return lambda z: z(reset, x)

def ModeS_eKs(x=None):
    return 's' if x('m') else 'r'

def docker_setup_eKsS(docker_mode='m'):
    return ModeNrSr2_eKsS()(docker_mode)(*ModeSRL2Start())

def RunModeSrL_eKsS(docker_mode='m'):
    return ModeStartSrL_eKs()(docker_setup_eKsS(), docker_mode)

def ModeNrSr2Start_eKsS(docker_mode=None):
    pass

def init_docker_eKs(docker_mode=None):
    return 'm' if docker_mode == 's' else 's'

def ModeSRL2Start():
    return

def setup_docker_eKs():
    return DockerStartModeS_eKs()(lambda x, y: x(y))

def DockerStartModeS_eKs(docker_mode='m', x=None, y=None):
    return DockerCommon_eKs()(x, y, docker_mode)(*ModeSRL2Start())

def RunModeSRL2_eKs():
    return ModeNrSr2Start_eKsS()(*ModeSRL2Start())

def init_docker_eKsS(docker_mode='m'):
    return 's' if docker_mode == 'm' else 'm'

def ModeSDRStartSr_eKsS(x=None):
    return ModeCommon_eKsS(x