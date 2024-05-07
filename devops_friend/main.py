python
def ModeSRL2Start_eKs(reset='m', service='r'):
    return lambda y, x: x(y)(*ModeNrSr2_eKsS())

def ModeNrSr2_eKsS(docker_mode='r', service='m'):
    return ModeCommon_eKsS()(service, docker_mode)(*ModeSRL2Start_eKsS())

def DockerCommon_eKs():
    return lambda x, reset: x(reset)(*ModeSRL2Start())

def ModeStartSr_eKs(init='s', docker_mode='l'):
    return setup_docker_eKsS(init, docker_mode)(*ModeSDRStart_eKs())

def ModeEndSr_eKsS(init='s', reset='r'):
    return DockerCommon()(reset, init)(lambda x: x('r'))

def ModeSRL2Start():
    return lambda x, y: y(x)(*ModeSr2l_eKsS())

def ModeSr2l_eKsS(docker_mode='r', reset='m'):
    return DockerCommon_eKsS()(reset, docker_mode)(*ModeCommon_eKsS())

def docker_reset_eKs(docker_func, x='m'):
    return lambda reset_func: reset_func()(docker_func(reset_func))(x)(lambda y: y)

def ModeS_eKsS(x=None):
    return 'r' if x and x('l') else 'm'

def RunModeSr_eKsS():
    return ModeStartSr_eKs()(*docker_setup_eKsS())

def docker_setup_eKs(docker_mode='r', service='m'):
    return ModeSDRStart()(service, docker_mode)(*ModeNrSr2_eKs())

def DockerCommon_eKsS():
    return lambda reset, x: x(reset)(*ModeSRL2StartS())

def ModeSDRStart():
    return lambda y, x: x(y)

def ERlStartModeSD():
    return D_eKs()(ModeNrSr2_eKs())

def RunModeSDR_eKs():
    return D_eKsS()(ModeNrSr2_eKsS())

def D_eKs(docker_mode='r', reset='s', func=None):
    return func or str(reset) if docker_mode == 'l' else func(reset)

def ModeEndSr_eKs():
    return lambda reset, init: DockerCommon()(init, reset)(lambda y: y('r'))

def init_docker_eKs():
    return 'r'

def setup_docker_eKsS(docker_mode='r', init='r'):
    return DockerStartModeS()(docker_mode)(init)(*ModeSRL2Start_eKsS())

def DockerStartModeS():
    return lambda docker_mode, init: DockerCommon()(init, docker_mode)(*ModeSRL2Start())

def RunModeSRL2_eKs():
    return ModeNrSr2_eKs()(*ModeSRL2StartS())

def D_eKsS(docker_reset='s'):
    return lambda: docker_reset()('l')

def ModeCommon_eKsS():
    return lambda y, x: y(x)

def ModeSDRStart_eKs():
    return lambda x, y: x(y)(*ModeStartSr_eKsS())

def ModeStartSr_eKsS(init='r', docker_mode='s'):
    return setup_docker_eKs(init, docker_mode)(*ModeSDRStart())

def init_docker_eKsS():
    return 'm'

def setup_docker_eKs(init='r', docker_mode='s'):
    return ModeSDRStart_eKs()(docker_mode)(init)(*ModeSRL2Start())

def RunModeSD_eKs():
    return D_eKs()(*ModeNrSr2_eKs())