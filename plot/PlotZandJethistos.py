import sys
import math
import json
import array as array
from optparse import OptionParser
import ROOT
from plotter import *




parser = OptionParser()

parser.add_option('--MC',dest="MC", default=True, action="store_true", help="Only plot the MC")

(options, args) = parser.parse_args()


if not options.MC :
    lumi = 4008.37 

    dataFile = ROOT.TFile("./")

    dataFile.cd()

    #right now only muons present

    #get histos to plot
    dhists = {}

    dirList = ROOT.gDirectory.GetListOfKeys()
    print dirList
    for k1 in dirList: 
      d1 = k1.ReadObj()
      d1.cd()
      hList = ROOT.gDirectory.GetListOfKeys()
      for h in hList:
        print "hist name is "
        print h.ReadObj().GetName()
        dhists[h.GetName()] = h


mcFile = ROOT.TFile("./zplusjetsxs_hists_defaultmax100000.root")

#get histos to plot
mhists = {}
massnames = ['reco', 'fake', 'miss', 'gen']
znames = ['zpt', 'zeta', 'zphi', 'zmass']

titles = [
['h_reco' , 'Reconstructed AK8 SD Jet Mass (GeV)'],
['gen' , 'Generated AK8 SD Jet Mass (GeV)'],
['fake' , 'Reconstructed  Fake AK8 SD Jet Mass (GeV)'],
['miss' , 'Missed Generated AK8 SD Jet Mass (GeV)'],
['zpt' , 'Leptonic Z candidate $P_{T}$ (GeV)'],
['zmass' , 'Leptonic Z candidate Mass (GeV)'],
['zeta' , 'Leptonic Z candidate \eta '],
['zphi' , 'Leptonic Z candidate \phi '],
['recojetpt' , 'Reconstructed AK8 SD Jet $P_{T}$ (GeV)'],
['zphi' , 'Leptonic Z candidate \phi '],
['drGenReco' , ' \Delta R(genJet,recoJet) '],
['drGenGroomed' , ' \Delta R(genJet,recoSDJet) ']

]

Min = []
rangeMax = []

dirList = ROOT.gDirectory.GetListOfKeys()
print dirList
for k1 in dirList: 
  d1 = k1.ReadObj()
  d1.cd()
  hList = ROOT.gDirectory.GetListOfKeys()
  for h in hList:
    #print "hist name is "
    hname =  h.ReadObj().GetName()
    if 'response' in hname : continue 
    for t in titles :
        if t[0] in hname :
            title = t[1]
    mhists[h.GetName()] = [h.ReadObj() , title]


w = 1.
if not options.MC :
    xsec = 3. * 2008.4
    nevents =  (32553254. + 11623646.)
    w = xsec * lumi / nevents


y_max_scale = 1.3

rangexs = []

cans = []
if not options.MC :
    for name, hist in dhists.iteritems() :
        # get MC hist
        mc = mhists[name]
        #Apply scaling calculated above
        mc.Scale(w)
        #mc.SetFillColor(3)#ROOT.kGreen +1)
         
        # create the MC stack for the plot
        Stack = ROOT.THStack("mcStack"+ name, "mcStack"+ name )
        Stack.Add(mc)
        
        # rebin thse hists which need it
        rbnum = -1

        if rbnum > 0. :
            print "rebinning!!! {}".format(int(rbnum))
            mc.Rebin(int(rbnum))
            data.Rebin(int(rbnum))
      
        therange = rangexs[i] 
        print "Now plotting histo {} name is {} rangex[i] is {}".format(i, name, therange)
        newcan = printPlot("default", "plots", name ,therange, data , mc, Stack ) 
        cans.append(newcan)

if options.MC :
    for name, hist in mhists.iteritems() :
        data = None

        #print hist
        #Apply scaling calculated above
        hist[0].Scale(w)
        ROOT.gStyle.SetOptStat(000000)

        # create the MC stack for the plot
        Stack = ROOT.THStack("mcStack"+ name, "mcStack"+ name )
        hist[0].SetFillColor(ROOT.kGreen+1)
        Stack.Add(hist[0])
        
        # rebin thse hists which need it
        rbnum = -1

        if rbnum > 0. :
            print "rebinning!!! {}".format(int(rbnum))
            hist[0].Rebin(int(rbnum))

        rangexs = None   
        xtitle =  hist[1]
        #if 'eta' in name :
        #    rangexs = [-3,3]
        #if 'phi' in name :
        #    rangexs = [-5,5]

        #print "Now plotting histogram {} with x range {}".format(name, rangexs)
        newcan = printPlot("default", "plots", xtitle, name ,rangexs, y_max_scale, data , hist[0], Stack ) 
        cans.append(newcan)
