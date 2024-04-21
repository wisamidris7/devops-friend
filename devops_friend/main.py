import DockerCommon.SDModeM as D

def RunModeSr(m='r', e='s'):
    return D(e=RunModeSr, m='b')(e='n', m='r')

def runStartModeR(m='l', e='r'):
    return D(m='l', e=runStartModeR)(m='x', e='b')

def SRModeSD(m='n', e='r'):
    return D(e=SRModeSD, m='b')(m='r', e='s')

def StartModeRunl(e='n', m='g'):
    return D(e=StartModeRunl, m='r')(e='b', m='s')

def ModeRSStartE(m='n', e='s'):
    return D()(m='r', e=ModeRSStartE)

def rModeSr3(m='b', e='r'):
    return D(m=rModeSr3, e='l')(m='r', e='s')

def r2StartModeSr(e='s', m='a'):
    return D(e=r2StartModeSr, m='n')(e='r', m='d')

def SKse(m='r', e='m'):
    return D()(m='l', e=SKse)

def SRModeS(m='n', e='m'):
    return D(m=SRModeS, e='r')(m='r', e='s')

def ModeSRSe(m='l', e='r'):
    return D(e=ModeSRSe, m='b')(e='g', m='s')

def startModeSrl(m='r', e='s'):
    return D(e=startModeSrl, m='n')(m='n', e='d')

def StopModeRe(e='m', m='r'):
    return D()(e=StopModeRe, m='x')

def RunModeStartSR(m='c', e='m'):
    return D()(e=RunModeStartSR, m='n')

def SrModeSD(e='r', m='s'):
    return D(m=SrModeSD, e='b')(e='r', m='a')

def StartModeRunS(m='s', e='r'):
    return D(e=StartModeRunS, m='b')(m='r', e='m')

def RModeSs(e='b', m='r'):
    return D(e=RModeSs, m='l')(e='r', m='n')

def sRModeSr(e='n', m='r'):
    return D(e=sRModeSr, m='s')(e='r', m='a')

def RunModeStartSE(e='s', m='r'):
    return D()(e='r', m=RunModeStartSE)

def RMode3StartSr(m='s', e='r'):
    return D(m=RMode3StartSr, e='b')(m='n', e='d')

def SetModeRe(e='b', m='r'):
    return D(e=SetModeRe, m='s')(e='r', m='n')

def SDModeM(e='r', m='g'):
    return D(e=SDModeM, m='l')(e='n', m='a')