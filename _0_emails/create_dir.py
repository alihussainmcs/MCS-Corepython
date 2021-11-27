# Python program to explain os.mkdir() method

# importing os module
import os
'''
names = ['Abdul Nisar Mulla', 'Abdulla Kondameedi', 'Abhinav Viswateja Kota', 'Bindu Gangavaram', 'Chandrahas Reddy Vangala', 'Girija Indukuri', 'Harish Babu Konanki', 'Harsha vardhan Reddy Nagireddy', 'Hemannachowdari Palabandla', 'Kiran Palamaneni ', 'Laxman S', 'Madhulatha Barapanedi ', 'Maheswari Cheemala', 'Manikanta Dhanenkula', 'Manoj Pulaganti ', 'Naveen Adabala', 'Nirmala Reddyvari', 'Pravallika Ganji', 'Priyanka Vemula ', 'Rajitha Gavireddy', 'Ritesh Telang', 'Sathyanarayanareddy Sunnampalli', 'Simon Gidieon', 'Sravani Tammineni', 'Teja Ganta', 'Vinay Kumar Reddy Yeddula', 'Vinitha Kavali ', 'Vishnu Vardhan Babu Dasari', 'Yamini MarappaReddy', 'Yaswanth Nimmala', 'Yaswantha Reddy Puttaparthi']
for directory in names:
    # Parent Directory path
    parent_dir = "E:/VNSQUARE/CANDIDATURES/B17/"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory '% s' created" % directory)
'''
sub_folders = ['1.Proofs','2. Consultancy','3. Interview Qs,Coding Tests','4. Offer Letter','5. Projects Company']
#import os
rootdir = 'mod'

for subdir, dirs, files in os.walk(rootdir):
    dir2 = rootdir
    # print(dir2)
    dirs = None
    for subdir, dirs2, files in os.walk(dir2):
        #print("Directory:",subdir,dirs,files)
        dirs = dirs2
    for each in dirs:
        fold = os.path.join(subdir,each)
        for sub_fold in sub_folders:
            #print("-0----------")
            path = os.path.join(fold, sub_fold)
            os.mkdir(path)
            print("Created:",path)

