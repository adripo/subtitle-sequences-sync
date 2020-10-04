from pysubparser import parser

subtitles = parser.parse('./original_subtitle.srt')
f = open("new_subtitle.srt", "w")

prevStart = None
i = 1
for subtitle in subtitles:
    if prevStart and prevStart == subtitle.start:
        f.write(subtitle.text + '\n')
    else:
        f.write('\n')
        f.write(str(i) + '\n')
        i += 1
        f.write(
            str(subtitle.start.strftime("%H:%M:%S,%f")[:-3]) + " --> " +
            str(subtitle.end.strftime("%H:%M:%S,%f")[:-3]) + '\n')
        f.write(subtitle.text + '\n')

        prevStart = subtitle.start

f.close()
print("Finished")
