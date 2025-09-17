def main():

    filetype = input ("Digite a extensao do arquivo: ").strip().lower()


    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }


    for ext, mime in media_types.items():
        if filetype.endswith(ext):
            print (mime)
            return


    print("application/octet-stream")

main()


