import pymongo
import os
from gridfs import GridFS



def upload_file(file_loc, file_name, fs):
    with open(file_loc,'rb') as file_data:
        #put file into mongodb
        fs.put(file_data, filename = file_name)
        print("upload completed")

def download_file(download_loc,db,fs,file_name):
    video_file=fs.find_one({"filename":file_name})
    if video_file:
        with open(download_loc, "wb") as output_file:
            # Read the video file from GridFS and write it to the output file
            output_file.write(video_file.read())
        print("Video downloaded successfully!")


if __name__=="__main__":
    client = pymongo.MongoClient("mongodb+srv://########@cluster0.3jkizbw.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test
    db= client["users"]
    collection = db["my_records"]
    file_name='y1.mp4'
    file_loc = "C:/Users/Kadam/Downloads/y1.mp4"
    download_loc =os.path.join(os.getcwd()+"/" +file_name)
    #print("download file stored here : "+download_loc)
    

    fs = GridFS(db, collection="my_records")
    # upload_file(file_loc=file_loc,file_name=file_name,fs=fs)
    # print("upload file stored here : ")
    download_file(download_loc=download_loc,db=db,fs=fs,file_name=file_name)