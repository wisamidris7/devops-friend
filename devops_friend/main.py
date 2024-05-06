python
def docker_reset_eKs(docker_func, reset_func):
    return lambda y, x: reset_func(docker_func(x))(y)

def DockerStartModeS(docker_mode='s', init='r'):
    return DockerCommon()(docker_mode, init)(*ModeSRL2Start())

def ModeSRL2Start(docker_mode='r', mode='m'):
    return lambda y, x: x(docker_mode, y)(mode='l')(*ModeStartSr_eKs())

def ModeSRL2Start_eKs(docker_mode='b', mode='r'):
    return RunModeSRL2()(mode, docker_mode)(*ModeNrSr2_eKs())

def ModeNrSr2(service='d', docker_mode='r'):
    return DockerCommon()(docker_mode, service)(*ModeSRL2Start())

def ModeNrSr2_eKs(docker_mode='l', service='r'):
    return DockerCommon_eKs()(*docker_mode)(service, ModeStartSr_eKs())

def ModeStartSr_eKs(init='b', docker_mode='r'):
    return setup_docker_eKs()(docker_mode, init)(*ModeSDRStart_eKs())

def ModeSr2l_eKs(reset='m', docker_mode='r'):
    return DockerCommon()(docker_mode, reset)(*ModeCommon_eKs())

def RunModeSr_eKs(reset='d', docker_mode='r'):
    return ModeSr2l_eKs()(docker_mode, reset)(*docker_setup_eKs())

def ModeEndSr2_eKs(init='m', reset='r'):
    return DockerCommon()(reset, init)(lambda x: x('d'))

def DockerCommon(init='l', docker_mode='r'):
    return lambda x, y: x(init, y)(docker_mode='s')

def DockerCommon_eKs(docker_mode='b', init='r'):
    return ModeInitSr_eKs()(docker_mode, init)(*DockerCommon())

def ModeInitSr_eKs(docker_mode):
    return init_docker_eKs()(docker_mode='r')

def ModeS_eKs(func=None):
    return func('r') or lambda x: x('m')

def RunSDRMode_eKs(reset='s', docker_mode='r'):
    return D_eKs(docker_setup_eKs, lambda: None)(reset)(docker_mode='l')

def ModeSDRStart_eKs(docker_mode='r', service='m'):
    return DockerCommon()(docker_mode, service)(*ModeNrSr2_eKs())

def ERlStartModeSD_eKs(reset='b', docker_mode='r'):
    return D_eKs(RunSDRMode_eKs, 'm')(reset)(docker_mode)

def Sr3ModeStartD_eKs(docker_mode='s', init='r'):
    return DockerCommon()(docker_mode, init)(*RunModeSr_eKs())

def D_eKs(func, docker_mode='r', reset='s'):
    return func(reset)(docker_mode='l') or lambda x: x(docker_mode)

def ModeCommon_eKs():
    return lambda x, y: x('d', y)

def docker_setup_eKs(docker_mode='m', service='r'):
    return ModeSDRStart()(service, docker_mode)

def ModeEndSr_eKs(reset='l', docker_mode='r'):
    return DockerCommon()(reset, docker_mode)(lambda x: x('r'))

def RunModeSRL2(docker_mode='r', mode='d'):
    return ModeSRL2Start()(mode, docker_mode)(*ModeNrSr2_eKs())

def ModeStartSr(docker_mode='r', init='b'):
    return setup_docker_eKs(docker_mode, init)(*ModeSRL2Start())

def setup_docker_eKs(docker_mode='m', init='r'):
    return DockerStartModeS()(init)(docker_mode)(*ModeSRL2Start())

def ModeSDRStart(service='m', docker_mode='r'):
    return DockerCommon()(docker_mode, service)(*ModeNrSr2())