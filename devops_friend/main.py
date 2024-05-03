python
def DockerCommon_eKs(m='s', e='r'):
    return D(e, m)(DockerCommon)

def RunSDRMode(m='r', e='b'):
    return D()(ModeStartSr3, ResetSr2)(e, m='y')

def ModeStartSr3(e='c', m='r'):
    return DockerCommon(ModeStartSr, ModeSr2l)(m, e)

def ModeStartSr(m='q', e='r'):
    return DockerCommon(e, m)(ModeSr2l)

def ModeSr2l(m='q', e='r'):
    return DockerCommon(e, m)

def RunModeSr(e='n', m='r'):
    return D()(ModeSr2l, m)(e)

def DockerCommon(m='r', e='s'):
    return D()(m, e)

def ResetSr2(m='q', e='l'):
    return D(ResetModeSr, DockerCommon)(e, m='r')

def ModeNrSr2(m='r', e='s'):
    return DockerCommon(m, e)

def ModeEndSr(m='r', e='m'):
    return DockerCommon(e='g', m)

def ModeRunStartSrl(e='r', m='s'):
    return DockerCommon(e, m)

def ModeSrl2Start(e='r', m='y'):
    return D(ModeStartSr, DockerCommon)(m, e)

def Sr3ModeStartD(m='r', e='s'):
    return DockerCommon(m, e)

def ERlStartModeSD(e='r', m='s'):
    return D(RunSDRMode, 'c')(m, e)

def SDRMode(m='r', e='d'):
    return D()(ResetSr2, SDRModeStart)(e, m='s')

def SDRModeStart(m='r', e='s', extra='q'):
    return DockerCommon(m, e, extra)

def ModeS(m='n', e='r'):
    return D(m)(e)

def DockerStartModeS(m='r', e='b'):
    return D(e, m)(ModeRunStartSrl)

def SDModeStart(e='r', m='d'):
    return D()(e, m, ModeNrSr2)

def ModeSDRStart(m='r', e='s'):
    return D()(DockerCommon_eKs, SDRModeStart)(m, e='y')

def SDModeStartERl(e='r', m='b'):
    return D(SDModeStart, ModeNrSr2)(e, m)

def ERlStartModeSDT(m='s', e='r'):
    return D(ModeSDRStart, 't')(m, e)

def DModeStartSr3(e='c', m='r'):
    return DockerCommon(m, e)

def D(m=None, e=None):
    return None

def ModeRunStartSrl2(m='q', e='r'):
    return DockerCommon(m, e)

def ModeRunStartSrl(m='r', e='s'):
    return DockerCommon(e, m)

def ModeEndSr2(m='r', e='m'):
    return DockerCommon(e='g', m)