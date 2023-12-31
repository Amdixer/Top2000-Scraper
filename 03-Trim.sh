#!/bin/bash

mkdir -p Output

# Read the CSV file line by line
while IFS=, read -r date start_hour end_hour url time_start time_end news_start news_end
do
    # Convert times to seconds
    start_time=$(echo $time_start | awk -F: '{ print ($1 * 3600) + ($2 * 60) + $3 }')
    end_time=$(echo $time_end | awk -F: '{ print ($1 * 3600) + ($2 * 60) + $3 }')
    news_start=$(echo $news_start | awk -F: '{ print ($1 * 3600) + ($2 * 60) + $3 }')
    news_end=$(echo $news_end | awk -F: '{ print ($1 * 3600) + ($2 * 60) + $3 }')

    # Format the input and output file names
    input_file="Downloads/$(printf "%02d" $date)Dec-$(printf "%02d" $start_hour)00-$(printf "%02d" $end_hour)00.mp3"
    output_file1="Output/$(printf "%02d" $date)Dec-$(printf "%02d" $start_hour).mp3"
    output_file2="Output/$(printf "%02d" $date)Dec-$(printf "%02d" $(($start_hour + 1))).mp3"

    # Run the ffmpeg commands
    if [ ! -f "$output_file1" ]; then
        ffmpeg -nostdin -y -hide_banner -loglevel fatal -stats -ss $start_time -i "$input_file" -to $(echo "$news_start - $start_time" | bc) -b:a 192k "$output_file1"
        wait
    fi
    if [ ! -f "$output_file2" ]; then
        ffmpeg -nostdin -y -hide_banner -loglevel fatal -stats -ss $news_end -i "$input_file" -to $(echo "$end_time - $news_end" | bc) -b:a 192k "$output_file2"
        wait
    fi
done < Top2000-2022.csv