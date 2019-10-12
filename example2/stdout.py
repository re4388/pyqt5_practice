# https://stackoverflow.com/questions/18421757/live-output-from-subprocess-command

# import subprocess
# result = subprocess.check_output("ls", shell=True)
# print(str(result).split('\\n'))

# import subprocess, sys
# process = subprocess.Popen(['ebook-convert', 'test.epub', 'test.mobi'], stdout=subprocess.PIPE)
# for line in iter(process.stdout.readline, ''):
#     x = sys.stdout.write(line)
#     print(x)
# out = p.stdout.read()
# print(out)


# https://stackoverflow.com/questions/2804543/read-subprocess-stdout-line-by-line
# FINALLY SUCCESS!!!

# import subprocess
# proc = subprocess.Popen(['ebook-convert', 'test.epub', 'test.mobi'], stdout=subprocess.PIPE)
# while True:
#     line = proc.stdout.readline()
#     if not line:
#         break
#     # the real code does filtering here
#     print(bytes.decode(line, "cp950", "ignore"))

sendText = ""
for i in range(10):
    sendTextList = '123'
    sendText += "\n" + sendTextList

print(len(sendText))


# import subprocess
# with subprocess.Popen(['ping', '8.8.8.8'], stdout=subprocess.PIPE) as proc:
#     print(proc.stdout.readline)


# process = subprocess.run(['ping', '8.8.8.8'], stdout=subprocess.PIPE)
# print(subprocess.PIPE)
# for line in iter(process.stdout.readline, ''):
#     print(bytes.decode(line, "cp950", "ignore"))

# Set up the echo command and direct th output to a pipe
# Run the command


# import subprocess
# with subprocess.Popen(['ping', '8.8.8.8'], stdout=subprocess.PIPE) as proc:
#     for line in iter(proc.stdout.readline, ''):
#         print(bytes.decode(line, "cp950", "ignore"))
#     proc.send_signal(0)

# import subprocess
# process = subprocess.Popen(['ping', '8.8.8.8'], stdout=subprocess.PIPE)
# with process as proc:
#     for line in iter(proc.stdout.readline, ''):
#         print(bytes.decode(line, "cp950", "ignore"))
# process.communicate()
# print(process.communicate()[0])


# success!!
# import subprocess
# import sys
# process = subprocess.Popen(['ebook-convert', 'test.epub', 'test.mobi'], stdout=subprocess.PIPE)
# for line in iter(process.stdout.readline, ''):
#     print(bytes.decode(line,"cp950","ignore"))
# process.communicate()


# success!!
# import subprocess
# import sys
# with open('test.log', 'w') as f:
#     process = subprocess.Popen(['ebook-convert', 'test.epub', 'test.mobi'], stdout=subprocess.PIPE)
#     for line in iter(process.stdout.readline, ''):
#         sys.stdout.write(bytes.decode(line,"cp950","ignore"))
#         f.write(bytes.decode(line,"cp950","ignore"))
# process.wait()


# print(type(out))
# out2 = str(out, encoding = "utf-8")
# print(type(out2))

# print(out)


# subprocess.call(["ls"])

# decode_stuff = ' MOBI 6 output\nApplying case-transforming CSS...\nRasterizing SVG images...\nConverting XHTML to Mobipocket markup.. MOBI 6 output\nApplying case-transforming CSS...\nRasterizing SVG images...\nConverting XHTML to Mobipocket markup...\nSerializing markup content...\n  Compressing markup content...\nGenerating MOBI index for a book\nMOBI output written to D:\\test.mobi\n\xb1N\xbf\xe9\xa5X\xc0x\xa6s\xa8\xec   D:\\test.mobi\n"'

# import subprocess
# import sys
# with open('test.log', 'wb') as f:
#     process = subprocess.Popen("ebook-convert", 'test.epub', 'test.mobi', stdout=subprocess.PIPE)
#     for c in iter(lambda: process.stdout.read(1), b''):
#         sys.stdout.write(c)
#         f.write(c)
