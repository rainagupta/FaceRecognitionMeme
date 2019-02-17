import io
import os

from memegenerator import make_meme
#import SimpleCV
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw
import random

client = vision.ImageAnnotatorClient()

def changeEnumToValue(x):
    if (x == 'VERY_UNLIKELY'):
        y =  0
    elif (x == 'UNLIKELY'):
        y = 1
    elif (x == 'POSSIBLE'):
        y =  2
    elif (x == 'LIKELY'):
        y =  3
    elif (x == 'VERY_LIKELY'):
        y = 4
    else:
        y = -1

    return y


#SadMEMES
#def sadMemes(x, image_file = 'face_image.png'):
#    img = Image(image_file)
    #img.dl().listFonts()
#    img.dl().selectFont('purisa')
#    img.drawText("Hello!")
#    img.show()


def sadMemes (x):
    if x == 0:
        make_meme("Tries to Remove Swap File" , "Removes Actual File", "opencv_frame_0.png")
    elif x == 1:
        make_meme("Puts dignity at stake and runs for the LX" , "Bus driver doesn't stop", "opencv_frame_0.png")
    elif x == 2:
        make_meme("Tries to Have a Social Life" , "Welcome to Data Structures","opencv_frame_0.png")
    elif x == 3:
        make_meme("Spend 24 Hours Coding" , "Code Doesnt Compile", "opencv_frame_0.png")
    elif x == 4:
        make_meme("Hackathon Group Promises to Stay Awake" , "Everyone Goes to Sleep", "opencv_frame_0.png")
    #img = Image.open('opencv_frame_0.png')
    #img.show()
    #mg = Image.open('temp.png')
#    img.show()


#AngerMemes
def angerMemes (x):
    if x == 0:
        make_meme("Python is Admirable Skill for CS" , "Lets Learn C Programming", "opencv_frame_0.png")

    elif x == 1:
        make_meme("Deadline is 12:00" , "Submitted on 12:01")
    elif x == 2:
        make_meme("Eats unhealthy as a college student" , "Attends a Hackathon", "opencv_frame_0.png")
    elif x == 3:
        make_meme("Tries to Meet Significant Other" , "Realizes That You Are a CS Major", "opencv_frame_0.png")
    elif x == 4:
        make_meme("Want to Take a Quick Nap" , "Oversleeps by 10 Hours", "opencv_frame_0.png")
#    img = Image.open('opencv_frame_0.png')
#    img.show()
    #mg = Image.open('temp.png')
    #img.show()

#JoyMemes

def joyMemes (x):
    if x == 0:
        make_meme("When you open WebReg" , "and a CS class is open", "opencv_frame_0.png")

    elif x == 1:
        make_meme("When you are waiting for the bus" , "and you end up right in front of the door", "opencv_frame_0.png")
    elif x == 2:
        make_meme("CS Know-it-all Takes Exam" , "Does Worse Than You", "opencv_frame_0.png")
    elif x == 3:
        make_meme("Takes Interview with a Company while at Rutgers" , "Interview is in Java", "opencv_frame_0.png")
    elif x == 4:
        make_meme("Knows Nothing about APIs" , "Gets an API to work for Hackathon", "opencv_frame_0.png")
    #mg = Image.open('temp.png')
#    img.show()

#    img = Image.open('opencv_frame_0.png')
#    img.show()
#SurpriseMemes
def surpriseMemes (x):
    if x == 0:
        make_meme("Stays up till 4 every night" , "Body is tired", "opencv_frame_0.png")
    elif x == 1:
        make_meme("Codes a Project" , "Code Compiles for the First time", "opencv_frame_0.png")
    elif x == 2:
        make_meme("Project 2 is Due Next Week" , "Project 3 is Assigned", "opencv_frame_0.png")
    elif x == 3:
        make_meme("Scores 100% on Coding Interview" , "Rejected by Company", "opencv_frame_0.png")
    elif x == 4:
        make_meme("Run Code for the First Time" , "No Compile Time Errors", "opencv_frame_0.png")
    #img = Image.open('opencv_frame_0.png')
    #img.show()
    #mg = Image.open('temp.png')
    #img.show()



def detect_face2(path):
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations
# Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')
#    vertices = (['({},{})'.format(vertex.x, vertex.y)

#        for vertex in face.bounding_poly.vertices])
#    print('face bounds: {}'.format(','.join(vertices)))



    list = []

    for face in faces:
        sadnessfactor = 'sorrow: {}'.format(likelihood_name[face.sorrow_likelihood])
        sadnessfactor = sadnessfactor[8:]
        #print(sadnessfactor)
        x = changeEnumToValue(sadnessfactor)
        #print (x)
        list = [changeEnumToValue(sadnessfactor)]
        angerfactor = 'anger: {}'.format(likelihood_name[face.anger_likelihood])
        angerfactor = angerfactor[7:]
        list.append(changeEnumToValue(angerfactor))
        joyfactor = 'joy: {}'.format(likelihood_name[face.joy_likelihood])
        joyfactor = joyfactor[5:]
        list.append(changeEnumToValue(joyfactor))
        surprisefactor = 'surprise: {}'.format(likelihood_name[face.surprise_likelihood])
        surprisefactor = surprisefactor[10:]
        list.append(changeEnumToValue(surprisefactor))
        #print(list)

        break

    if len(list) == 0:
        print("No face found!")
        return "-1"
    check = list.index(max(list))

    if check == 0:
        str = "Sadness"
    elif check == 1:
        str = "Anger"
    elif check == 2:
        str = "Joy"
    elif check == 3:
        str = "Surprised"
    else:
        str = "Unknown"




    print("Sadness: " + sadnessfactor)
    print("Anger: " + angerfactor)
    print("Joy: " + joyfactor)
    print("Surprise: " + surprisefactor)
    print("OVERALL EMOTION FACTOR: " +  str)



    return str

    #img = Image(path)
###img.show()






def detect_face(face_file, max_results=4):
    """Uses the Vision API to detect faces in the given file.

    Args:
        face_file: A file-like object containing an image with faces.

    Returns:
        An array of Face objects with information about the picture.
    """
    client = vision.ImageAnnotatorClient()

    content = face_file.read()
    image = types.Image(content=content)

    return client.face_detection(image=image, max_results=max_results).face_annotations


def highlight_faces(image, faces, output_filename):
    """Draws a polygon around the faces, then saves to output_filename.

    Args:
      image: a file containing the image with the faces.
      faces: a list of faces found in the file. This should be in the format
          returned by the Vision API.
      output_filename: the name of the image file to be created, where the
          faces have polygons drawn around them.
    """
    im = Image.open(image)
    draw = ImageDraw.Draw(im)
    # Sepecify the font-family and the font-size
    for face in faces:
        box = [(vertex.x, vertex.y)
               for vertex in face.bounding_poly.vertices]
        draw.line(box + [box[0]], width=5, fill='#00ff00')
        # Place the confidence value/score of the detected faces above the
        # detection box in the output image
        draw.text(((face.bounding_poly.vertices)[0].x,
                   (face.bounding_poly.vertices)[0].y - 30),
                  str(format(face.detection_confidence, '.3f')) + '%',
                  fill='#FF0000')
    im.save(output_filename)



def main(input_filename, output_filename, max_results):
    with open(input_filename, 'rb') as image:
        faces = detect_face(image, max_results)
        print('Found {} face{}'.format(
            len(faces), '' if len(faces) == 1 else 's'))

        print('Writing to file {}'.format(output_filename))
        # Reset the file pointer, so we can read the file again
        image.seek(0)
        highlight_faces(image, faces, output_filename)






import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
	break

cam.release()

cv2.destroyAllWindows()


main("opencv_frame_0.png", "face_image.png", 4)
str2 = detect_face2("face_image.png")


y = random.randint(0,4)
#print(y)

if str2 == "Sadness":
    #print("inhere")
    sadMemes(y)
elif str2 == "Joy":
    joyMemes(y)
elif str2 == "Anger":
    angerMemes(y)
elif str2 == "Surprised":
    surpriseMemes(y)
elif str2 == "Unknown":
    make_meme("Sorry, Unable to Recognize Face!","" ,"opencv_frame_0.png" )

#make all the files go to opencv_frame_0.png, or we can change in meme generator, to open whatever.


if (str2 != "-1"):
    img = Image.open('face_image.png')
    img.show()

    img = Image.open('temp.png')
    img.show()
#str = "Joy"






#make_meme("WASSUP", "HI", "opencv_frame_0.png")
#sadMemes(1, "face_image.png")
