import passphrase_generator
import subprocess
import crypt
import argparse

def replaceStrInFile(strMatch,strReplace,fileName):
  """Replace all occurrences of strMatch with strReplace in file fileName
  """

  file=open(fileName,mode='r')
  fileText=file.read()
  file.close()
  fileText=fileText.replace(strMatch,strReplace)
  file=open(fileName,mode='w')
  file.write(fileText)
  file.close()
def createUserWebDirectory(username):

  webDirectory="/var/www/html/"+username
  subprocess.run(["mkdir",webDirectory])
  subprocess.run(["chown",username+":"+username,webDirectory])
def deleteUserWebDirectory(username):

  webDirectory="/var/www/html/"+username
  subprocess.run(["rm","-rf",webDirectory])
def createGuestAccounts(numAccounts):

  print("creating guest accounts")
  guest_account_passphrase=passphrase_generator.getRandom3WordPhrase()
  guest_account_passphrase_enc=crypt.crypt(guest_account_passphrase)
  print("  Guest accounts passphrase: \""+guest_account_passphrase+"\"")
  for i in range(numAccounts):

    username="{}{:02d}".format("user",i+1)
    print("  "+username)
    subprocess.run(["useradd","-s","/bin/bash","-m","-p",
      guest_account_passphrase_enc,username])

    createUserWebDirectory(username)
def deletGuestAccounts(numAccounts):

  print("deleting guest accounts")
  for i in range(numAccounts):

    username="{}{:02d}".format("user",i+1)
    print("  "+username)
    subprocess.run(["deluser","--remove-home",username])
    deleteUserWebDirectory(username)
def enablePasswordSSHAuthentication():
  '''NOTE: really should have fail2ban running before this function is called.
  '''

  print("***WARNING: SHOULD HAVE FAIL2BAN RUNNING NOW***")
  print("enabling ssh password authentication")
  replaceStrInFile("PasswordAuthentication no","PasswordAuthentication yes",
    "/etc/ssh/sshd_config")
  subprocess.run(["service","ssh","restart"])
def installJekyll():

  subprocess.run(["gem","install","jekyll","bundler"])
def main():

  parser = argparse.ArgumentParser(description='Setup Jekyll and create guest accounts')
  parser.add_argument('numGuestAccounts', metavar='N', type=int,
                      help='Number of guest accounts to create')
  #parser.add_argument('--delete', action=argparse.BooleanOptionalAction,help="Delete accounts rather than create them")
  parser.add_argument('--delete', action='store_true',default=False,help="Delete accounts rather than create them [account creation is default action]")
  args = parser.parse_args()

  installJekyll()
  enablePasswordSSHAuthentication()
  if args.delete:
    deletGuestAccounts(args.numGuestAccounts)
  else:
    createGuestAccounts(args.numGuestAccounts)

if __name__=="__main__":
  main()
