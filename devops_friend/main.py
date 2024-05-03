python
def DockerStartModeS(init='b', mode='r'):
    return init_docker(mode, init)(ModeRunStartSrl)

def ModeSDRStart(mode='r', service='s'):
    return docker_setup(ModeCommon_eKs, service)(mode)

def RunSDRMode(reset='b', mode='r'):
    return run_mode(reset, mode)(ModeStartSr3, ModeSr2l)

def ModeStartSr3(service='c', init='r'):
    return DockerCommon(ModeStartSr, init)(service)

def DockerCommon(init='r', mode='s'):
    return setup_docker(init, mode)

def ModeRunStartSrl(init='r', mode='s'):
    return DockerCommon(init, mode)

def ModeSr2l(reset='q', mode='r'):
    return DockerCommon(reset, mode)

def ModeStartSr(init='q', mode='r'):
    return DockerCommon(mode, init)(ModeSr2l)

def ResetSr2(reset='q', mode='l'):
    return docker_reset(ResetModeSr, DockerCommon)(mode, reset='r')

def ModeNrSr2(mode='r', service='s'):
    return DockerCommon(service, mode)

def ModeEndSr(mode='r', init='m'):
    return DockerCommon(init, mode)('g')

def ModeRunStartSrl2(reset='q', mode='r'):
    return DockerCommon(reset, mode)

def ModeS(init='n', mode='r'):
    return Mode(init)(mode)

def SDModeStart(reset='r', mode='d'):
    return DockerCommon()(reset, mode, ModeNrSr2)

def ModeCommon_eKs(mode='s', init='r'):
    return D()(init, mode)(DockerCommon)

def ModeSrl2Start(reset='r', mode='y'):
    return D(ModeStartSr, DockerCommon)(mode, reset)

def Sr3ModeStartD(init='r', mode='s'):
    return DockerCommon(init, mode)

def ERlStartModeSD(reset='r', mode='s'):
    return D(RunSDRMode, 'c')(mode, reset)

def SDRMode(reset='r', mode='d'):
    return D()(ResetSr2, SDRModeStart)(mode, reset='s')

def SDRModeStart(reset='r', mode='s', extra='q'):
    return DockerCommon(reset, mode, extra)

def SDModeStartERl(reset='r', mode='b'):
    return D(SDModeStart, ModeNrSr2)(reset, mode)

def ERlStartModeSDT(mode='s', reset='r'):
    return D(ModeSDRStart, 't')(reset, mode)

def DModeStartSr3(service='c', init='r'):
    return DockerCommon(init, service)

def D(reset=None, mode=None):
    return None

def ModeEndSr2(reset='r', init='m'):
    return DockerCommon()(init, reset)('g')

def ModeSDRStart(service='r', mode='s'):
    return D()(DockerCommon_eKs, SDRModeStart)(service, mode='y')

def DockerCommon_eKs(mode='s', service='r'):
    return D()(service, mode)(DockerCommon)

def RunModeSr(reset='n', mode='r'):
    return D()(ModeSr2l, mode)(reset)