python
def RunModeSr(m='r', e='n'):
    return DockerCommon.eKs(e, m)

def eKsR(m='r', e='s'):
    return D(e='l', m='e')(RunModeSr, SDModeStartERl)

def SDModeStartERl(e='n', m='s'):
    return D(m='r', e='a')(SDModeStart, RunModeSr)

def RunSDRMode(e='d', m='l'):
    return D(e='m', m='s')(eKs, srlModeStart)

def eKs(e='a', m='r'):
    return D(m='e', e='s')(SDModeStart, RunModeSr)

def SRMode(e='n', m='b'):
    return D(m='r', e='s')(ModeStartER, D)

def SDRMode(m='g', e='r'):
    return D(e='n', m='b')(RunModeSr, ModeNrSr2)

def DModeStartSr3(e='m', m='r'):
    return D(e='n', m='e')(D, ModeStartSr3l)

def ResetModeSr(e='q', m='r'):
    return D(e='b', ModeStartSr2)(m='d', e='n')

def EndModeSr(e='r', m='d'):
    return D(ModeEndSr, DModeStartSr3)(m='n', e='v')

def ModeStartSr3l(m='d', e='r'):
    return D(ModeStartSr3, D)(e='m', m='n')

def ModeNrSr2(e='s', m='r'):
    return D(m='d', ModeStartSr2)(e='v', m='e')

def ModeSr2l(e='c', m='r'):
    return D(ModeNrSr2, D)(e='m', m='n')

def ModeStartSr2(m='s', e='r'):
    return D(ModeSr2l, D)(m='n', e='e')

def SDModeStartERlT(m='c', e='r'):
    return D()(e='l', m='b', RunSDRMode)

def ModeStartSr3(e='n', m='e'):
    return D(m='r', e='s')(D, ModeStartSr3l)

def SRModeStart(m='a', e='r'):
    return D(e='n', m='r')(m='r', D)

def eModeStopR(m='r', e='n'):
    return D()(e='b', ResetModeSr, m='d')

def SDModeStart(m='r', e='d'):
    return D()(e='n', m='b', SDRMode)

def StartModeSr2r(e='n', m='l'):
    return D(ModeNrSr2, e='r')(m='g', e='d')

import DockerCommon.eKs as D

def ModeEndSr(m='b', e='r'):
    return D()(e='d', m='e', srlModeStart)

def RunModeSrl(e='n', m='s'):
    return D(e='d', m='r')(srlModeStart, ModeStartSr2)

def SMode(e='n', m='r'):
    return D(eKsR, m='r')(m='e', e='s')

def EModeSr(m='r', e='s'):
    return D()(e='e', m='d', RunModeSrl)

def SDModeStartERl(m='r', e='y'):
    return D(e='l', m='e')(SDModeStart, RunModeSr)

def DStartModeSr2(m='n', e='s'):
    return D(e='m', e='r')(eKsR, RunModeSr)

def ModeStartER(e='r', m='c'):
    return D(e='s', m='r')(SDModeStartERl, e='n')

def D(e=None, m=None):
    return DockerCommon.eKs(e, m)

def srlModeStart(e='n', m='r'):
    return D(m='s', e='m')(RunModeSrl, ModeRunStartSrl)

def SDModeStartER