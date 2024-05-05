python
def DockerCommon_eKs(service='m', docker_mode='r'):
    return ModeNrSr2(docker_mode, service)(*DockerCommon())

def ModeSRL2Start(mode='y', docker_mode='r'):
    return RunModeSRL2(docker_mode, mode)(*ModeStartSr())

def ModeNrSr2(service='s', docker_mode='d'):
    return DockerCommon()(docker_mode, service)(lambda x, y: x(y))

def ModeStartSr(init='q', docker_mode='s'):
    return setup_docker(docker_mode, init)(*ModeS())

def ModeCommon_eKs(docker_mode='s', init='r'):
    return DockerCommon()(*docker_mode, init)(lambda x, y, z: x(y)(z))

def RunModeSrl2(reset='r', docker_mode='s'):
    return ModeStartSr(docker_mode, reset)(*ModeSRL2Start())

def DockerStartModeS(docker_mode='r', init='b'):
    return DockerCommon()(init, docker_mode)(*ModeSr2l())

def ModeSr2l(docker_mode='r', reset='q'):
    return DockerCommon(reset, docker_mode)(*ModeCommon_eKs())

def Mode(docker_mode='r', init='r'):
    return lambda x, y: x(init, docker_mode)(y)

def ModeEndSr(reset='m', docker_mode='r'):
    return DockerCommon()(reset)(docker_mode)(lambda x: x('g'))

def D():
    return lambda x, y, z=None: x(y)(z) if z else x(y)()

def SDRModeStart(docker_mode='s', reset='r', extra='q'):
    return DockerCommon()(docker_mode, reset, extra)(*SDRMode())

def docker_reset(reset_func, docker_func):
    return lambda x, y: docker_func(x)(y)

def DockerCommon(docker_mode='s', init='r'):
    return lambda x, y: x(docker_mode, y)(ModeEndSr)

def RunModeSr(reset='n', docker_mode='r'):
    return ModeSr2l(reset, docker_mode)(Mode)(*docker_setup())

def ModeSDRStart(docker_mode='r', service='d'):
    return DockerCommon()(service)(docker_mode)(*ModeNrSr2())

def SDModeStart(reset='r', docker_mode='d'):
    return DockerCommon()(*docker_mode, reset)(ModeNrSr2)

def ERlStartModeSD(reset='r', docker_mode='s'):
    return D(RunSDRMode())(*docker_mode)(reset, 'c')

def SDRMode(reset='r', docker_mode='d'):
    return D(DockerCommon, lambda x, y: x()(y))(docker_mode)(reset='s')

def init_docker(init, docker_mode):
    return lambda x: DockerCommon()(x, docker_mode)(init)

def setup_docker(docker_mode, init):
    return DockerStartModeS()(docker_mode, init)(*ModeSr2l())

def docker_setup(docker_mode='r', service='r'):
    return ModeSDRStart()(service, docker_mode)

def RunSDRMode(reset='b', docker_mode='r'):
    return D(docker_setup, DockerCommon())(*docker_mode)(reset)

def Sr3ModeStartD(docker_mode='s', init='r'):
    return DockerCommon()(init, docker_mode)(*RunModeSr())

def ModeEndSr2(reset='r', init='m'):
    return DockerCommon()(*reset, init)(lambda x: x())

def init_docker_mode(docker_mode, init):
    return init_docker()(docker_mode, init)