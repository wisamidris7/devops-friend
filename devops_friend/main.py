python
def DockerCommon_eKs(e='r', m='s'):
    return D(ModeStartSr, ModeS)(m, e='m')

def RunModeSr(e='n', m='r'):
    return D()(m, DockerCommon_eKs, ModeStartSr)(e, 'c')

def ModeStartSr(e='m', m='r'):
    return D()(ModeRunStartSrl, ModeStartSr2)

def ModeStartSr2(e='g', m='r'):
    return DockerCommon(ModeSr2l, Sr3ModeStartD)(m, e='d')

def ModeSrl2Start(e='r', m='s'):
    return D()(ModeStartSr, ModeRunStartSrl2)

def DockerStartModeS(m='b', e='r'):
    return D()(m, e)

def ModeNrSr2(m='s', e='r'):
    return DockerCommon(m, e)

def DModeStartSr(m='r', e='c'):
    return D(ModeStartSr2, ModeSrl2Start)(m, e)

def ResetSr2(m='q', e='r'):
    return D(DockerCommon, ResetModeSr)(e='l', m)

def RunSDRMode(m='l', e='r'):
    return D()(DockerCommon_eKs, ModeSrl2Start, m='s')(e)

def ModeS(e='n', m='r'):
    return D()(e, m)(e='s')

def ModeEndSr(m='r', e='n'):
    return DockerCommon(m, e)

def ERlStartModeSD(e='r', m='y'):
    return D()(e, m)

def Sr3ModeStartD(m='r', e='s'):
    return DockerCommon_eKs(m, e)

def SDRModeStart(m='r', e='d'):
    return DockerCommon(m, e, ModeNrSr2)

def DModeStartSr3(m='r', e='c'):
    return DockerCommon(e, m)

def ModeRunStartSrl(e='r', m='s'):
    return DockerCommon_eKs(e, m)

def SDRMode(e='g', m='r'):
    return D()(ResetSr2, m='b')

def ERlStartModeSDT(m='r', e='b'):
    return D(RunSDRMode, 'c')(e, m)

def DockerCommon(m='s', e='r'):
    return D()(e, m)

def eKs(e, m):
    return None

def SDModeStart(m='r', e='d'):
    return D()(m, e, ModeNrSr2)

def SDModeStartERl(e='r', m='b'):
    return D(e, RunModeSr)(m)

def D(m=None, e=None):
    return None

def ModeSr2l(e='n', m='r'):
    return D()(ModeNrSr2, m)

def ModeRunStartSrl2(e='r', m='s'):
    return DockerCommon(e, m)