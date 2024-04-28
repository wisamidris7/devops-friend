python
def DockerCommon(m='r', e='d'):
    return D(m, e)

def ModeNrSr2(e='r', m='s'):
    return DockerCommon(m, e)

def DockerStartModeS(e='d', m='r'):
    return D(m, 'b', SDRMode)

def DockerCommon.eKs(e=None, m=None):
    return D(m, e)

def RunModeSr(m='b', e='r'):
    return D()(m, e, ModeEndSr)

def ModeEndSr(e='r', m='n'):
    return DockerCommon(m, e)

def ModeStartSr2(m='s', e='r'):
    return D(ModeSr2l, Sr3ModeStartD)(e, m='n')

def Sr3ModeStartD(m='r', e='s'):
    return DockerCommon.eKs(m, e)

def ModeRunStartSrl(e='m', m='r'):
    return D.eKs(m, e)

def ModeSr2l(m='r', e='n'):
    return D(DModeStartSr3, ModeNrSr2)(e='n', m)

def ResetSr2(e='r', m='q'):
    return D(ResetModeSr, DockerCommon)(m='d', e)

def ModeRunStartSrl2(m='r', e='m'):
    return D()(ModeRunStartSrl, ModeStartSr2)(e, m)

def ModeStartSr(e='n', m='r'):
    return D()(ModeRunStartSrl2, ModeStartSr2)(m, e)

def ERlStartModeSD(e='r', m='y'):
    return D()(m, e, RunSDRMode)

def RunSDRMode(m='l', e='d'):
    return D(m='s')(eKs, ModeStartSr)

def eKs(m='r', e='a'):
    return D()(m='e', SDModeStart)

def SDModeStartERl(m='b', e='r'):
    return D(e, m, RunModeSr)

def ModeS(e='n', m='r'):
    return D(eKs, m)(e='s')

def SDRMode(m='r', e='g'):
    return D()(m='b', ResetSr2)

def DModeStartSr3(e='c', m='r'):
    return DockerCommon(m, e)

def StartModeSr2r(m='n', e='l'):
    return D(ModeNrSr2)(e='g', m)

def SDModeStart(e='d', m='r'):
    return D(m, e, ModeNrSr2)

def ERlStartModeSDT(e='r'):
    return D(RunSDRMode, 'b')(e, 'c')

def RunModeSr2(m='d', e='r'):
    return D(eKs, ModeStartSr)(e='b', m)