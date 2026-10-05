#Step 1: Create a repository on gihub on the web and name is according to the assignments. I will also try to create the repository within from the terminal no website

#Step 2: to clone a repo in github( it is stored on the cloud!) to your local machine use the command git clone [THE LINK OF THE REPO IN HTTPS] . As you can see this ADDS that repo INTO your machines local files. I have added it do D:\ , that is also where last weeks 471 repo is located

#Step 3: Now change your directory to that folder before you create any branches
# #Lets create the new branch. We use git checkout -b [branch name]. "checkout" causes you to go to another branch ( exiting the current branch),"-b" creates the new branch.

#step 4:git add [DOSYA ADI] kullanarak stage'e eklemek istediğin dosyayı ekle. Dosyayı stageden çekmek için  git restore --staged [Dosya adı] kullan

#step 5:git commit -m ["MESAJIN"] ve git push -u origin [branch adı] kullanarak message ekle ve repona pushla. artık web de görünür! Ama branch olarak main de değil fix/conform'da

#step 6 :main ile birleştirmke için çnce main branche gidelim. git checkout main, sonra istenilen branchindeki içeriği main e eklemek için merge atalım git merge [branch adı]
#NOT: BUNDAN SONRA EKLEDİĞİN VE MERGLEDİĞİN ŞEY HALA İKİ BRANCHDE DE VAR HEM MAİN HEM MERGEDEN ÖNCEKİ BRACH

#git push -u origin [branch] deki origin bir nevi senin repon. "-u" ise bgilgisayarındaki yerel dal (local branch) ile GitHub'daki uzak dalı (remote branch) birbirine kalıcı olarak bağlar (track eder).
 
##Part 2
#step 7 : yeni branchi oluştur 

#step 8 : you know name
#step 9 : kodu ekle VE SAVE ALMAYI UNUTMAAAA

#step 10 : add commit push
#step 11 : conflict simüle edeceğiz, main branch e chekoutla B: Kodu düzelt junior dev de SAVELE add commit push ama mainde olduğun için -u gerek yok C: merge feat/ into main. Hata çıkınca senior olanı seç keep current
#Step 12 :