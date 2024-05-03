python
def ModeStartSr(m='q', e='r'):
    return DockerCommon(e, m)(ModeSr2l)

def DockerCommon_eKs(m='r', e='s'):
    return D(m, e)(DockerCommon)

def RunModeSr(e='n', m='r'):
    return D()(ModeSr2l, m)(e)

def DockerStartModeS(e='b', m='r'):
    return D(e, m)(ModeRunStartSrl)

def ModeNrSr2(e='s', m='r'):
    return DockerCommon(m, e)

def ModeS(m='n', e='r'):
    return D(m)(e)

def ResetSr2(m='q', e='l'):
    return D(ResetModeSr, DockerCommon)(e, m='r')

def ModeSr2l(e='r', m='q'):
    return DockerCommon(m, e)

def ModeEndSr(m='r', e='m'):
    return DockerCommon(e='g', m)

def ModeRunStartSrl(e='r', m='s'):
    return DockerCommon(e, m)

def DModeStartSr3(e='c', m='r'):
    return DockerCommon(m, e)

def RunSDRMode(e='b', m='r'):
    return D()(DockerCommon_eKs, ResetSr2)(m, e='y')

def ModeSrl2Start(m='y', e='r'):
    return D(ModeStartSr, DockerCommon)(m, e)

def Sr3ModeStartD(m='r', e='s'):
    return DockerCommon(m, e)

def ERlStartModeSD(m='s', e='r'):
    return D(RunSDRMode, 'c')(m, e)

def SDRMode(m='r', e='d'):
    return D()(ResetSr2, SDRModeStart)(e, m='s')

def D(m=None, e=None):
    return None

def ModeStartSr3(m='r', e='c'):
    return DockerCommon(ModeStartSr, ModeSr2l)(m, e)

def SDRModeStart(m='r', e='s', extra='q'):
    return DockerCommon(m, e, extra)

def ModeRunStartSrl2(m='q', e='r'):
    return DockerCommon(m, e)

def SDModeStart(m='d', e='r'):
    return D()(e, m, ModeNrSr2)

def SDModeStartERl(e='r', m='b'):
    return D(SDModeStart, ModeNrSr2)(e, m)

def ERlStartModeSDT(m='s', e='r'):
    return D(RunSDRMode, 't')(m, e)

def DockerCommon(m='r', e='s'):
    return D()(m, e)