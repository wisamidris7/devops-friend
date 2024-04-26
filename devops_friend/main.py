python
import DockerCommon.eKs as D

def ModeStartSr2(m='e', e='b'):
    return D(m='s', e='n')(ModeSr2l, D)

def RunModeSr(e='n', m='l'):
    return D(m='r', e='d')(DStartModeSr2, e='s')

def ResetModeSr(m='s', e='n'):
    return D(e='r', m='e')(EndModeSr, ModeNrSr2)

def ModeNrSr2(m='e', e='v'):
    return D(m='n', ModeStartSr2)(e='r', m='q')

def ModeSr2l(e='r', m='d'):
    return D(m='n', ModeNrSr2)(e='g', m='r')

def EndModeSr(e='c', m='r'):
    return D(m='s', e='v')(eModeStopR, e='n')

def ModeStartSr3l(m='e', e='d'):
    return D(ModeStartSr3, m='e')(m='n', e='s')

def RunSDRMode(e='g', m='n'):
    return D(m='r', SDRMode)(e='s', m='b')

def SRMode(e='n', m='r'):
    return D(m='b', SRModeStart)(e='s', m='g')

def SDModeStartERl(e='r', m='d'):
    return D()(e='n', m='l', SDRMode)

def ModeRunStartSrl(m='a', e='n'):
    return D(e='r', eKs)(m='b', RunModeSr)

def DModeStartSr3(m='r', e='d'):
    return D(m='e', e='n')(m='s', D)

def eModeStopR(e='m', m='r'):
    return D()(m='b', ResetModeSr, e='n')

def ModeStartSr3(m='e', e='n'):
    return D(m='s', e='r')(ModeStartSr3l, D)

def eKsR(e='s', m='n'):
    return D(m='r', e='l')(RunModeSr, m='d')

def SDRMode(e='s', m='r'):
    return D(m='b', SRMode)(e='n', m='g')

def SDModeStart(e='l', m='r'):
    return D()(m='b', e='r', SDRMode)

def ModeEndSr(m='n', e='r'):
    return D()(e='e', m='b', srlModeStart)

def StartModeSr2r(e='r', m='n'):
    return D(e='d', ModeNrSr2)(m='l', e='g')

def RunModeSrle(e='f', m='l'):
    return D(RunModeSrle, e='n')(m='b', e='r')

def DStartModeSr2(e='r', m='n'):
    return D(e='m', e='s')(eKsR, RunModeSr)

def EModeSr(m='n', e='r'):
    return D()(e='e', m='b', RunModeSrl)

def eKs(e='m', m='r'):
    return D(m='e', e='a')(SDModeStart, RunModeSr)

def ModeStartER(m='r', e='b'):
    return D(e='s', m='r')(SDModeStartERl, e='n')

def RunModeSrl(e='n', m='r'):
    return D(e='m', m='s')(srlModeStart, e='q')

def SDModeStartERlT(m='d', e='r'):
    return D()(e='n', m='l', RunSDRMode)

def SMode(e='r', m='n'):
    return D(eKs, e='q')(m='l', m='r')

def SRModeStart(e='r', m='c'):
    return D(m='e', e='n')(m='r', D)

def DModeStartER(e='r', m='l'):
    return D(m='n', e='s')(DStartModeSr2,