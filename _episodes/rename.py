#!/usr/bin/python3
import optparse as op
import glob
import os

def parseOptions():
  """Parses command line options
  """
  
  parser=op.OptionParser(usage="Usage %prog",version="%prog 1.0",description="Renames numbered md files. Should be run in directory where files are located.")
  parser.add_option("--start"
    ,dest="startFileName"
    ,help="Name of file to start applying increment [default: <name-of-first-file>]."
    ,default=None)
  parser.add_option("--end"
    ,dest="endFileName"
    ,help="Name of file to stop applying increment [default: <name-of-last-file>]."
    ,default=None)
  parser.add_option("--increment"
    ,dest="increment"
    ,help="Increment to apply to file name number [default: %default]."
    ,type="int"
    ,default=1)
  parser.add_option("--dry-run"
    ,dest="dryRun"
    ,action="store_true"
    ,help="Only print out what would be done, but don't do it [default: %default]."
    ,default=False)
  return parser.parse_args()
def main():
  
  #parse command line options
  (options,args)=parseOptions()
  
  files=glob.glob('./[0-9][0-9]-*.md')
  files.sort()
  startFound=False
  endFound=False
  if options.startFileName==None:
    startFound=True
  for file in files:
    
    #remove path from file name
    fileTmp=os.path.basename(file)
    
    #check to see if file is start file
    if options.startFileName!=None:
      if fileTmp == os.path.basename(options.startFileName):
        startFound=True
    
    #check to see if file is end file
    if options.endFileName!=None:
      if fileTmp == os.path.basename(options.endFileName):
        endFound=True
    
    #if we have started
    if startFound and not endFound:
      
      #increment file name
      index=int(fileTmp[0:2])
      indexInc=str(index+options.increment)
      newName=indexInc.zfill(2)+fileTmp[2:]
      print("incrementing file name \""+fileTmp+"\" to \""+newName+"\"\" ...")
      if not options.dryRun:
        os.rename(os.path.join("./",fileTmp),os.path.join("./",newName))

if __name__ == "__main__":
 main()