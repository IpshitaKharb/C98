def swapFiles(): 
    file1 = input('Enter File Name')
    file2 = input('Enter The Swapping Location')

    #Here w represents write mode and r represents read mode
    fileOpen1 = open(file1,'r')
    fileOpen2 = open(file2,'r')

   #Here we want to swap the content so we are giving content read 1
    contentRead1 = fileOpen1.read()
    contentRead2 = fileOpen2.read()

   #Now we will swap so we need write here
    fileOpen1 = open(file1,'w')
    fileOpen2 = open(file2,'w')

  # os is operating system
    
    fileOpen2.write(contentRead1)

   
    fileOpen1.write(contentRead2)

swapFiles()



