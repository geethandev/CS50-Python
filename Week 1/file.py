def get_mime_type(file_name):
    file_extension = file_name.lower().split('.')[-1].replace(" ","")

    if file_extension == "gif":
        return "image/gif"
    elif file_extension in ["jpeg", "jpg"]:
        return "image/jpeg"
    elif file_extension == "png":
        return "image/png"
    elif file_extension == "pdf":
        return "application/pdf"
    elif file_extension == "txt":
        return "text/plain"
    elif file_extension == "zip":
        return "application/zip"
    else:
        return "application/octet-stream"

file_name = input("File name: ")
mime_type = get_mime_type(file_name)
print(mime_type)
