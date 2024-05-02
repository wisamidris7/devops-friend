python
def DockerCommon_eKs(m='s', e='r'):
    return DockerCommon(e, m)

def ModeSrl2Start(m='q', e='r'):
    return D()(ModeStartSr, DockerCommon)

def RunModeSr(m='r', e='n'):
    return D()(ModeStartSr, DockerCommon)(e, 'c')

def ModeStartSr3(m='r', e='c'):
    return DockerCommon(ModeRunStartSrl, ModeStartSr2)(e, m)

def ModeStartSr(m='r', e='m'):
    return DockerCommon(ModeSr2l, m)(e='d')

def DockerStartModeS(m='b', e='r'):
    return D()(m, e)

def ModeNrSr2(m='s', e='r'):
    return D()(m, e)

def ERlStartModeSD(e='r', m='y'):
    return D()(m, e)

def RunSDRMode(m='s', e='b'):
    return D()(ModeSrl2Start, DockerCommon_eKs)(e, m='r')

def DockerCommon(e='s', m='r'):
    return D()(m, e)

def ResetSr2(m='q', e='l'):
    return D(DockerCommon, ResetModeSr)(e='r', m)

def ModeSr2l(e='r', m='s'):
    return DockerCommon(m, e)

def ModeEndSr(m='r', e='n'):
    return DockerCommon(e='g', m)

def SDModeStart(m='r', e='d'):
    return D()(m, e, ModeNrSr2)

def ModeS(e='r', m='n'):
    return D()(m)(e)

def DModeStartSr3(e='c', m='r'):
    return DockerCommon(e, m)

def SDRMode(e='g', m='r'):
    return D()(ResetSr2, m='b')

def Sr3ModeStartD(m='r', e='s'):
    return DockerCommon(e, m)

def ModeRunStartSrl(e='r', m='s'):
    return DockerCommon_eKs(e, m)

def ERlStartModeSDT(m='r', e='b'):
    return D(RunSDRMode, 'c')(e, m)

def SDRModeStart(m='r', e='d'):
    return DockerCommon(m, e, ModeNrSr2)

def ModeRunStartSrl2(m='r', e='s'):
    return DockerCommon(e, m)

def D(m=None, e=None):
    return None

def SDModeStartERl(m='b', e='r'):
    return D(RunModeSr, e)(m, e='b')