import cv2
import os

input_image = input("Enter Image Path (example.png) = " )

image = cv2.imread(input_image)

if image is  None:
    print("Error: Image is not found!")
else:
    image = cv2.resize(image,(300,300))
    print("\n1.Line on Image") #Line Module Working Correctly
    print("\n2.Circle on Image") #Working
    print("\n3.Rectangle on Image") #Working
    print("\n4.Text on Image") #working
    choice = int(input("\nWhat you want to perform? "))
    new_image = ''
    if(choice == 1):
        pt1 = input("Enter Quardinates of Lines starting point in format 10,30 : ")
        pt2 = input("Enter Quardinates of Lines Ending point in format (10,30) : ")
        
        pt1 = pt1.split(",")
        pt2 = pt2.split(",")
        new_pt1 = []
        new_pt2 = []
        for i in pt1:
            new_pt1.append(int(i))
        
        for i in pt2:
            new_pt2.append(int(i))

        new_pt1 = tuple(new_pt1)
        new_pt2 = tuple(new_pt2)

        
        thickness = int(input("Enter thickness of line e.g 1,2,3,... : "))

        new_image = cv2.line(image,new_pt1,new_pt2,(255,0,0),thickness)

    elif(choice == 2):
        center = input("Enter Center Quardinates for Circle to appear in format (10,30) : ")
        radius = int(input("Enter radius e.g 50,100,... : "))

        center = center.split(",")
        new_center = []
        for i in center:
            new_center.append(int(i))
        new_center = tuple(new_center)
        # color = input("Enter color code in rgb format (12,345,234) : ")
        thickness = int(input("Enter thickness e.g 1,2,3,... : "))

        new_image = cv2.circle(image,new_center,radius,(255,0,0),thickness)
    
    elif(choice == 3):
        pt1 = input("Enter Quardinates of Rectanlge top left point in format (10,30) : ")
        pt2 = input("Enter Quardinates of Rectangle bottom right point in format (10,30) : ")
        pt1 = pt1.split(",")
        pt2 = pt2.split(",")
        new_pt1 = []
        new_pt2 = []
        for i in pt1:
            new_pt1.append(int(i))
        
        for i in pt2:
            new_pt2.append(int(i))

        new_pt1 = tuple(new_pt1)
        new_pt2 = tuple(new_pt2)
        # color = input("Enter color code in rgb format (12,345,234) : ")
        thickness = int(input("Enter thickness  e.g 1,2,3,... : "))

        new_image = cv2.rectangle(image,new_pt1,new_pt2,(255,0,0),thickness)
    
    elif(choice == 4):
        text = input("Enter Text to write : ")
        org = input("Enter Quardinates for text to appear on image in format (10,30) : ")

        org = org.split(",")
        new_org = []
        for i in org:
            new_org.append(int(i))
        new_org = tuple(new_org)
        # color = input("Enter color code in rgb format (12,345,234) : ")
        thickness = int(input("Enter thickness e.g 1,2,3,... : "))
        fontStyle = cv2.FONT_HERSHEY_SIMPLEX
        new_image = cv2.putText(image,text,new_org,fontStyle,1,(255,0,0),thickness)

    else:
        print("Write the correct choice")


    y = input("What do you want to do with the image (1.Show | 2. Save) ? ")
    if(int(y)==1):
        cv2.imshow("New Image",new_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif(int(y)==2):
        # Extract the extension
        _, extension = os.path.splitext(input_image)


        #Where image going ?
        cv2.imwrite(f"download{extension}",new_image) # Now working

    else:
        print("Write Correct Choice")
