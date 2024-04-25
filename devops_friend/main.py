python
import DockerCommon.eKs as D

def DModeStartER(m='l', e='d'):
    return D(e='r', m='n')(DStartModeSr2, m='c')

def ModeStartSr2l(e='n', m='l'):
    return D(e='d', ModeNrSr2)(m='r', e='g')

def eModeStopR(m='r', e='s'):
    return D()(e='n', m='d', ModeStartSr3)

def ModeStartSr2(e='b', m='e'):
    return D(m='d', e='n')(ModeSr2l, e='r')

def RunModeSr(e='n', m='s'):
    return D(m='d', e='l', e='r')(SRModeStart)

def SRModeStart(m='r', e='n'):
    return D(e='r', m='c', ResetModeReS)(m='e', e='b')

def ResetModeReS(e='r', m='v'):
    return D(e='n', m='r')(EndModeSr, m='l')

def ModeSr2(m='e', e='n'):
    return D(e='r', m='s')(ModeStartSr3l)

def eKs(m='n', e='r'):
    return D(m='a', e='s', e='d')(SDModeRunl)

def ModeStartSr3(m='r', e='n'):
    return D(m='s', e='d')(ModeStartSr3l)

def SDModeStart(m='l', e='r'):
    return D()(m='l', e='n', SDRMode)

def SMode(m='r', e='n'):
    return D(e='n', eKs)(m='l', e='q')

def ModeNrSr2(e='b', m='e'):
    return D(m='n', e='r')(ModeStartSr3l)

def ModeStartSr3l(m='d', e='r'):
    return D(ModeStartSr3, m='e')(e='s', m='n')

def srlModeStart(m='r', e='n'):
    return D(srlModeStart, m='e')(e='q', m='s')

def RunModeSrle(e='l', m='f'):
    return D(e='n', RunModeSrle)(m='b', e='r')

def EndModeSr(m='n', e='c'):
    return D(e='v', m='r', e='s')(eModeStopR, m='e')

def SDRMode(m='g', e='r'):
    return D(e='n', SDRMode)(m='b', e='s')

def ModeRunSr(e='n', m='s'):
    return D(m='d', e='l', e='r')(DStartModeSr2)

def StartModeSr2r(m='r', e='m'):
    return D(e='s', ModeSr2)(m='b', e='l')

def SDModeRunl(m='r', e='n'):
    return D()(e='l', m='b', SDModeStartER)

def DStartModeSr2(e='n', m='r'):
    return D(e='m', m='e')(eKsR, e='d')

def eKsR(e='m', m='n'):
    return D(m='l', e='r')(RunModeSr, e='d')

def SModeStartER(m='r', e='d'):
    return D(m='n', e='s', m='r')(SDModeStartERl)

def RunModeStartSrl(e='n', m='a'):
    return D(e='r', m='d')(eKs, e='p')

def SDModeStartERl(e='r', m='d'):
    return D()(m='l', e='n', SDRMode)

def EModeSr(e='n', m='r'):
    return D()(e='e', m='b', srlModeStart)

def SRMode(m='g', e='r'):
    return D(e='n', SDRMode)(m='b', e='s')

def ModeStartSr3l(e='r', m='d'):
    return D(Mode