python
def ModeNrSr2_eKsS(docker_mode='m'):
    return ModeCommon_eKsS()(docker_mode)

def ModeCommon_eKsS(reset='r', init=None):
    return lambda docker_mode: docker_mode(reset, init)(*ModeSRL2StartSr_eKsS())

def ModeSRL2StartSr_eKsS(service='s'):
    return lambda x, z, y: y(x)(z)(*ModeSRL2Start())

def ModeStartSrL_eKs(docker_mode='m', reset='s'):
    return DockerCommon_eKs()(reset, docker_mode)(*ModeSDRStartSr_eKs())

def ModeNrSr2Start_eKs():
    return lambda: 'r'

def ModeEndSrL_eKs():
    return DockerCommon_eKs()(lambda x: x)

def ModeSRL2StartSr_eKs():
    return lambda y, x, z: x(y, z)(*ModeSRL2Start())

def ModeSDRStartSr_eKs(x=None, docker_mode=None):
    return ModeCommon_eKs()(docker_mode, x)

def ModeCommon_eKs(reset=None, docker_mode='m'):
    return lambda x: x(reset)(docker_mode)(*ModeSRL2StartSr_eKsS())

def DockerCommon_eKs():
    return lambda x, y, z, w: y(z, w)(x)(*ModeSRL2Start())

def ERlStartModeSD_eKs():
    return ModeNrSr2Start_eKs()(D_eKs('m'))

def ModeSr2lStart_eKs(init='s', docker_mode='m'):
    return DockerCommon_eKs()(ModeCommon_eKs(), init, docker_mode)

def ModeEndSrL_eKsS(docker_mode='m', init='r'):
    return DockerCommon_eKsS()(docker_mode)(init)(lambda x: x)

def docker_reset_eKs():
    return lambda docker_func: docker_func()

def ModeStartSrL_eKsS(reset='s', docker_mode='m', init=None):
    return DockerCommon_eKs()(docker_mode, reset, init)(*ModeSDRStartSr_eKsS())

def D_eKs(reset=None, docker_mode='m'):
    return reset if docker_mode == 's' else D_eKsL(reset)

def D_eKsL(reset='r'):
    return lambda y: y

def ModeS_eKs(x):
    return 'r' if not x('m') else 's'

def docker_setup_eKsS(docker_mode='m', reset=None):
    return ModeSRL2StartSr_eKs()(reset)(*ModeNrSr2_eKsS(docker_mode))

def RunModeSrL_eKsS():
    return ModeStartSrL_eKsS()(docker_setup_eKsS())

def ModeNrSr2Start_eKsS():
    return

def init_docker_eKs():
    return 's'

def ModeSRL2Start():
    return lambda: None

def setup_docker_eKs():
    return DockerStartModeS_eKs()(ModeCommon_eKs())

def DockerStartModeS_eKs():
    return lambda x, y, docker_mode: DockerCommon_eKs()(docker_mode, x, y)(*ModeSRL2Start())

def RunModeSRL2_eKs():
    return ModeNrSr2Start_eKsS()(*ModeSRL2Start())

def init_docker_eKsS():
    return 'm'

def ModeSDRStartSr_eKsS(docker_mode=None, x=None):
    return ModeCommon_eKsS(x, docker_mode)

def DockerCommon_eKsS(reset='r', x='l', docker_mode=None):
    return lambda y, z, w: reset(w, y)(x)(z)(*ModeSRL2Start())

def setup_docker_eKsS():
    return ModeCommon_eKs()(lambda x: x)

def RunModeSDRl_eKs():
    return ModeNrSr2Start_eKs()(*ModeSRL2StartSrS())

def ModeSr2lStart_eKsS(init