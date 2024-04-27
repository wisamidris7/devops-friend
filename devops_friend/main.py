python
def RunModeSr(m='n', e='r'):
    return DockerCommon.eKs(e, m)

def ResetModeSr(e='q', m='r'):
    return D(ModeStartSr2, e)(m='d', e='n')

def ModeStartSr3(m='r', e='m'):
    return DockerCommon.eKs(e, m)

def EndModeSr(m='r', e='d'):
    return ModeStartSr3(e='v')

def SRModeStart(m='a', e='r'):
    return D(e, m)(D, m)

def ModeNrSr2(e='s', m='r'):
    return D(m)(ModeStartSr2, D)

def RunSDRMode(e='d', m='l'):
    return D(m='s')(eKs, srlModeStart)

def ModeStartSr3l(m='d', e='r'):
    return D(ModeStartSr3, D)(e='m', m='n')

def eModeStopR(m='r', e='n'):
    return D(m, e)

def ModeStartER(m='c', e='r'):
    return D(e='r', m='s')(SDModeStartERl, e)

def SDModeStartERl(m='r', e='y'):
    return D()(RunModeSr, e)

def ModeSr2l(e='c', m='r'):
    return D(ModeNrSr2, D)(e='n', m)

def DModeStartSr3(m='r', e='s'):
    return DockerCommon.eKs(m, e)

def ModeEndSr(m='b', e='r'):
    return D(ModeStartSr2, DModeStartSr3)(e='d')

def SDRModeStart(m='r', e='d'):
    return D()(m='b', e, SDRMode)

def EModeSr(m='r', e='s'):
    return D()(e='e', m, RunModeSrl)

def SDModeStartERlT(m='c'):
    return D()(m, 'b', RunSDRMode)

import DockerCommon.eKs as D

def SMode(e='n', m='r'):
    return D(eKs, m)(e='s', m='e')

def srlModeStart(e='n', m='r'):
    return D(m='s')(RunModeSrl, ModeRunStartSrl)

def ModeRunStartSrl(e='m', m='s'):
    return DockerCommon.eKs(m, e)

def StartModeSr2r(e='l', m='n'):
    return D(ModeNrSr2)(m='g', e)

def SDRMode(m='g', e='r'):
    return D(m='b')(RunModeSr, ModeNrSr2)

def eKs(e='a', m='r'):
    return D(m='e')(SDModeStart, RunModeSr)

def RunModeSrl(m='n', e='s'):
    return DockerCommon.eKs(e, m)

def ModeStartSr2(m='s', e='r'):
    return D(ModeSr2l, D)(m='n', e='e')

def SDModeStart(m='r', e='d'):
    return D()(m='b', e, SDRMode)

def SRMode(e='n', m='b'):
    return D(e='s')(ModeStartER, D)

def D(e=None, m=None):
    return DockerCommon.eKs(e, m)