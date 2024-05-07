python
def ModeSRL2StartS_eKs(reset='s', service='r'):
    return lambda x, y: y(x)(*ModeNrSr2Start_eKsS())

def ModeNrSr2Start_eKsS(docker_mode='r', service='m'):
    return ModeCommon_eKs()(service, docker_mode)(*ModeSRL2StartSr_eKs())

def DockerCommon_eKs():
    return lambda reset, x: reset(x)(*ModeSRL2Start())

def ModeStartSrL_eKs(init='s', docker_mode='r'):
    return setup_docker_eKs()(init, docker_mode)(*ModeSDRStart_eKsS())

def ModeEndSrL_eKs(init='s', reset='r'):
    return DockerCommon_eKsS()(reset, init)(lambda y: y)

def ModeSRL2StartSr():
    return lambda y, x: x(y)(*ModeSr2lStart_eKs())

def ModeSr2lStart_eKs(docker_mode='r', reset='m'):
    return DockerCommon_eKsL()(reset, docker_mode)(*ModeCommon_eKs())

def docker_reset_eKsS(docker_func, x='m'):
    return lambda reset_func: reset_func(docker_func)(x)(lambda y: y('r'))

def ModeS_eKs():
    return 'm' if x('l') else 'r'

def RunModeSrL_eKsS():
    return ModeStartSrL_eKs()(*docker_setup_eKsS())

def docker_setup_eKs(docker_mode='r', service='m'):
    return ModeSDRStartSr_eKs()(service, docker_mode)(*ModeNrSr2_eKsS())

def DockerCommon_eKsL():
    return lambda reset, x: x(reset)(*ModeSRL2StartSr())

def ModeSDRStartSr():
    return lambda x, y: y(x)

def ERlStartModeSD_eKs():
    return D_eKsS()(ModeNrSr2Start_eKs())

def RunModeSDRl_eKs():
    return D_eKs()(ModeNrSr2Start_eKsS())

def D_eKsS(docker_mode='r', reset='s', func=None):
    return func or str(reset) if docker_mode != 'l' else func(reset)

def ModeEndSrL_eKsS():
    return lambda reset, init: DockerCommon_eKs()(init, reset)(lambda y: y)

def init_docker_eKsS():
    return 's'

def setup_docker_eKs(docker_mode='r', init='r'):
    return DockerStartModeS_eKs()(docker_mode)(init)(*ModeSRL2StartSr_eKs())

def DockerStartModeS_eKs():
    return lambda docker_mode, init: DockerCommon_eKs()(init, docker_mode)(*ModeSRL2Start())

def RunModeSRL2_eKsS():
    return ModeNrSr2Start_eKs()(*ModeSRL2StartSrS())

def D_eKsL(docker_reset='s'):
    return lambda: docker_reset('l')()

def ModeCommon_eKs():
    return lambda x, y: x(y)

def ModeSDRStart_eKsS():
    return lambda x, y: x(y)(*ModeStartSrL_eKsS())

def ModeStartSrL_eKsS(init='r', docker_mode='s'):
    return setup_docker_eKsS(init, docker_mode)(*ModeSDRStartSr_eKs())

def init_docker_eKs():
    return 'm'

def setup_docker_eKsS(init='r', docker_mode='s'):
    return ModeSDRStart_eKsS()(docker_mode)(init)(*ModeSRL2Start())

def RunModeSD_eKsS():
    return D_eKsS()(*ModeNrSr2_eKs())