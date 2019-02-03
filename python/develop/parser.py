def Main():
    file_name = 'sample.txt'

    # get all file data
    with open(file_name, 'r') as file:
        file_lines = file.readlines()

    # Get the titles and subtitles
    cur_title_number = 0
    titles = []
    subtitles = []
    for idx in range(0, len(file_lines)):
        # if title
        if idx + 1 < len(file_lines) and file_lines[idx + 1][0] == '=':
            cur_title_number += 1
            cur_title = file_lines[idx].strip()
            cur_line_pos = idx + 1
            titles.append((cur_title, cur_line_pos))

        # if subtitle
        elif idx + 1 < len(file_lines) and file_lines[idx + 1][0] == '-':
            cur_line_pos = idx + 1
            cur_subtitle = file_lines[idx].strip()
            subtitles.append((cur_subtitle, cur_line_pos, cur_title_number))

    # print The titles and subtitles to output file in formatted way
    with open('output ' + file_name, 'w') as file:
        # write the header of file
        file.write('File: ' + file_name + "\n\n")
        file.write("Titles founds:\n\n")

        # for each title
        for title_info in titles:
            title = title_info[0]
            title_length = len(title)
            title_pos = title_info[1]
            file.write(title + " in line " + str(title_pos) + "; length = " + str(title_length) + " characters\n")

        # print the header of subtitles
        file.write("\nLoop through " + str(len(titles)) + " titles and list subtitles:\n")

        previous_title_number = 0

        # for each subtitle
        for subtitle_info in subtitles:
            subtitle = subtitle_info[0]
            subtitle_length = len(subtitle)
            subtitle_pos = subtitle_info[1]
            title_number = subtitle_info[2]

            # if this subtitle for new title the new title header
            if previous_title_number != title_number:
                previous_title_number = title_number
                file.write('\nSubtitles for title ' + str(title_number) + ":\n\n")

            file.write(subtitle + " in line " + str(subtitle_pos) +
                       "; length = " + str(subtitle_length) + " characters\n")


if __name__ == "__main__":
    Main()
