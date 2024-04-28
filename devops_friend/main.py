python
def DockerCommon_eKs(e=None, m=None):
    return D(e, m)

def ModeStartSr(e='n', m='r'):
    return D()(ModeRunStartSrl, ModeStartSr2)(e, m)

def RunModeSr(m='r', e='b'):
    return D()(ModeEndSr, e, m)

def DockerStartModeS(m='b', e='r'):
    return D(m, 'a', SDRMode)(e)

def eKs(m='r', e='a'):
    return D()(SDModeStart, m='e')

def ResetSr2(e='r', m='q'):
    return D(DockerCommon, ResetModeSr)(e='d', m)

def ModeRunStartSrl2(m='r', e='m'):
    return D()(ModeRunStartSrl, ModeStartSr)(m, e)

def ModeNrSr2(e='r', m='s'):
    return DockerCommon(e, m)

def RunSDRMode(e='r', m='l'):
    return D()('c', eKs, ModeStartSr)(m='s')

def ModeS(e='n', m='r'):
    return D(eKs, m)(e='s')

def ModeEndSr(e='r', m='n'):
    return DockerCommon(m, e)

def DockerCommon(e='m', m='l'):
    return D()(m, e)

def StartModeSr2r(m='n', e='l'):
    return D(ModeNrSr2)(m, e='g')

def ModeSr2l(m='r', e='n'):
    return D(DModeStartSr3, ModeNrSr2)(m='n', e)

def ERlStartModeSD(e='r', m='y'):
    return D()(m, e, RunSDRMode)

def SDModeStart(e='d', m='r'):
    return D(m, e, ModeNrSr2)

def ModeStartSr2(e='g', m='r'):
    return D(ModeSr2l, Sr3ModeStartD)(e, m)

def Sr3ModeStartD(e='s', m='r'):
    return DockerCommon_eKs(m, e)

def DModeStartSr3(e='c', m='r'):
    return DockerCommon(m, e)

def ModeRunStartSrl(e='e', m='r'):
    return D.eKs(e, m)

def SDRMode(m='r', e='g'):
    return D()(ResetSr2, e='b')

def SDModeStartERl(m='b', e='r'):
    return D(RunModeSr, e)(m)

def ERlStartModeSDT(m='b', e='r'):
    return D(RunSDRMode, 'c')(m, e)