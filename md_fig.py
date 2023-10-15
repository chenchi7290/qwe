import base64
f=open('affb57a31ed720ccd0587622ea17764.png','rb') #二进制方式打开图文件
ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
f.close()
# print(str(ls_f))

def image_to_base64(image_file, output_file=1):

  # need base 64
  import base64,sys
  # open the image
  image = open(image_file, 'rb') 
  # read it
  image_read = image.read() 
  # encode it as base 64
  # after python>=3.9, use `encodebytes` instead of `encodestring`  
  image_64_encode = base64.encodestring(image_read) if sys.version_info <(3,9) else base64.encodebytes(image_read)
  # convert the image base 64 to a string
  image_string = str(image_64_encode)
  # replace the newline characters
  image_string = image_string.replace("\\n", "")
  # replace the initial binary
  image_string = image_string.replace("b'", "")
  # replace the final question mark
  image_string = image_string.replace("'", "")
  # add the image tags
  image_string = '<p><img src="data:image/png;base64,' + image_string + '"></p>'
  # write it out
#   image_result = open(output_file, 'w')
#   image_result.write(image_string)
  print(image_string)


image_to_base64("affb57a31ed720ccd0587622ea17764.png")