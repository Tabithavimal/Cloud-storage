import dropbox

class Transferdata:
    def __init__(self,accesstoken):
        self.accesstoken=accesstoken
    
    def uploadfolder(self,source,destination):
        dbx=dropbox.Dropbox(self.accesstoken)
        f=open(source,'rb')
        dbx.folder_upload(f.read(),destination)

def main():
    accesstoken='pwT_0y8Fp9oAAAAAAAAAAUkCriigACWrJDE_EgpSK_QKH-xI4nn8O2VaIjsITzEv'
    transferdata=Transferdata(accesstoken)
    source=input("Enter the folder path to transfer:")
    destination=input("Enter the folder path to upload to dropbox:")
    transferdata.uploadfile(source,destination)
    print("folder has been moved")

main()
        