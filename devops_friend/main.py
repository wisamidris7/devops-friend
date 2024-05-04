python
def ModeNrSr2(docker_mode='r', service='s'):
    return DockerCommon(docker_mode, service)

def ModeStartSr(docker_mode='r', init='q'):
    return setup_docker(docker_mode, init)

def ModeSRL2Start(mode='y', reset='r'):
    return RunModeSRL2(reset, mode)(ModeStartSr)

def ModeEndSr(docker_mode='r', reset='m'):
    return DockerCommon(reset, docker_mode)(lambda x: x('g'))

def ModeCommon_eKs(docker_mode='s', init='r'):
    return DockerCommon()(docker_mode, init)(lambda x, y: x(y))

def ModeS(docker_mode='r', init='n'):
    return ModeStartSr(docker_mode, init)(ModeSRL2Start)

def ModeSr2l(reset='q', docker_mode='r'):
    return DockerCommon(reset, docker_mode)(ModeCommon_eKs)

def DockerStartModeS(init='b', docker_mode='r'):
    return DockerCommon(docker_mode, init)(ModeS)

def RunModeSr(docker_mode='r', reset='n'):
    return ModeSr2l(reset, docker_mode)(Mode)(docker_mode)

def Mode(init='r', docker_mode='r'):
    return lambda x: x(init)(docker_mode)

def DockerCommon(docker_mode='s', init='r'):
    return lambda x: x(docker_mode, init)(ModeEndSr)

def RunModeSrl2(docker_mode='s', reset='r'):
    return ModeStartSr(docker_mode, reset)

def D():
    return lambda x, y=None, z=None: x(y)(z) if z else x(y)

def ModeSDRStart(service='s', docker_mode='r'):
    return DockerCommon(docker_mode)(service)(ModeNrSr2)

def SDRMode(docker_mode='d', reset='r'):
    return D(DockerCommon, lambda x, y: x(y))(docker_mode)(reset='s')

def init_docker(init, docker_mode):
    return lambda x: x(init)(docker_mode)

def setup_docker(docker_mode, init):
    return DockerStartModeS(docker_mode, init)(ModeSr2l)

def docker_setup(service, docker_mode='r'):
    return ModeSDRStart(service, docker_mode)

def RunSDRMode(docker_mode='r', reset='b'):
    return D(docker_setup, DockerCommon)(docker_mode)(reset)

def Sr3ModeStartD(docker_mode='s', init='r'):
    return DockerCommon(docker_mode, init)(RunModeSr)

def ERlStartModeSD(docker_mode='s', reset='r'):
    return D(RunSDRMode)(docker_mode)(reset, 'c')

def SDRModeStart(docker_mode='s', reset='r', extra='q'):
    return DockerCommon(docker_mode, reset, extra)(SDRMode)

def SDModeStartERl(docker_mode='b', reset='r'):
    return D(ModeSRL2Start, ModeNrSr2)(reset, docker_mode)

def docker_reset(docker_func, reset_func):
    return lambda x, y: reset_func(docker_func(x), y)

def SDModeStart(docker_mode='d', reset='r'):
    return DockerCommon()(docker_mode, reset)(ModeNrSr2)

def DockerCommon_eKs(docker_mode='r', service='m'):
    return ModeNrSr2(docker_mode, service)(DockerCommon)

def ModeEndSr2(init='m', reset='r'):
    return DockerCommon()(reset, init)(lambda x: x)

def init_docker_mode(docker_mode, init):
    return init_docker(init, docker_mode)