
#'94XNanoV0-DYtoLL-histos.root', '94XNanoV0-DYtoLL-nanoTrees.root'

import FWCore.ParameterSet.Config as cms
process = cms.Process('NANO')
process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring(),

)
process.source.fileNames = [
       '/store/user/asparker/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/NANAODreclusterDY1JetsToLLM-50TuneCP513TeV-madgraphMLM-pythia8RunIIFall17MiniAOD-94Xmc2017/180205_213147/0000/test94X_NANO_96.root',
       '/store/user/asparker/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/NANAODreclusterDY1JetsToLLM-50TuneCP513TeV-madgraphMLM-pythia8RunIIFall17MiniAOD-94Xmc2017/180205_213147/0000/test94X_NANO_97.root',
       '/store/user/asparker/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/NANAODreclusterDY1JetsToLLM-50TuneCP513TeV-madgraphMLM-pythia8RunIIFall17MiniAOD-94Xmc2017/180205_213147/0000/test94X_NANO_98.root',
       '/store/user/asparker/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/NANAODreclusterDY1JetsToLLM-50TuneCP513TeV-madgraphMLM-pythia8RunIIFall17MiniAOD-94Xmc2017/180205_213147/0000/test94X_NANO_99.root',


]
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10))

process.options = cms.untracked.PSet()

process.output = cms.OutputModule("PoolOutputModule", fileName = cms.untracked.string('94XNanoV0-DYtoLL-nanoTrees.root'), fakeNameForCrab =cms.untracked.bool(True))
process.out = cms.EndPath(process.output)
