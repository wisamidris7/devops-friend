python
def eKsR(e='n', m='r'):
    return D(m='e', e='l')(SDModeStart, RunModeSr)

def RunModeSrle(e='m', m='l'):
    return D(e='n', RunModeSrle)(m='r', e='y')

def SDModeStartERlT(e='r', m='c'):
    return D()(m='l', e='b', RunSDRMode)

def RunModeSr(e='v', m='l'):
    return D(m='r', e='s')(D_StartModeSr2, ModeNrSr2)

def SRModeStart(e='r', m='a'):
    return D(e='n', m='r')(m='r', D)

def eModeStopR(e='b', m='r'):
    return D()(m='d', ResetModeSr, e='q')

def ResetModeSr(e='r', m='q'):
    return D(m='e', ModeStartSr2)(e='n', m='s')

def RunModeSrl(e='d', m='r'):
    return D(e='m', m='s')(srlModeStart, e='n')

def SDModeStartERl(e='c', m='r'):
    return D()(m='b', e='n', SDRMode)

def ModeStartSr3(m='e', e='n'):
    return D(m='s', e='r')(ModeStartSr3l, D)

def DModeStartSr3(e='r', m='d'):
    return D(e='m', e='n')(m='e', D)

def ModeNrSr2(e='v', m='d'):
    return D(m='n', ModeStartSr2)(e='s', m='r')

def ModeSr2l(m='r', e='c'):
    return D(m='n', ModeNrSr2)(e='m', m='s')

def ModeStartSr2(e='r', m='s'):
    return D(ModeSr2l, D)(m='n', e='m')

def EndModeSr(m='r', e='n'):
    return D(e='v', m='s')(ModeEndSr, DModeStartSr3)

def ModeStartSr3l(e='m', m='d'):
    return D(ModeStartSr3, e='r')(m='n', e='b')

def ModeRunStartSrl(e='n', m='r'):
    return D(eKs, m='d')(e='s', m='r')

def DStartModeSr2(e='d', m='n'):
    return D(e='s', e='m')(eKsR, RunModeSr)

def SRMode(e='s', m='g'):
    return D(m='b', ModeStartER)(e='n', m='r')

def SDRMode(e='n', m='g'):
    return D(m='b', SRMode)(e='r', m='s')

def SMode(m='r', e='n'):
    return D(eKsR, e='s')(m='e', m='r')

def EModeSr(m='r', e='n'):
    return D()(e='e', m='b', RunModeSrl)

def SDModeStart(e='r', m='d'):
    return D()(m='b', e='n', SDRMode)

def StartModeSr2r(m='l', e='n'):
    return D(e='d', ModeNrSr2)(m='g', e='r')

import DockerCommon.eKs as D

def ModeEndSr(e='r', m='b'):
    return D()(m='e', m='d', srlModeStart)

def RunSDRMode(m='l', e='n'):
    return D(m='r', SDRMode)(e='d', m='s')

def D(e=None, m=None):
    return DockerCommon.eKs(e, m)

def ModeStartER(e='r', m='c'):
    return D(e='s', m='r')(SDModeStartERl, e='n')

def eKs(e='s', m='r'):
    return D(m='e', e='a')(SDModeStart, RunModeSr)