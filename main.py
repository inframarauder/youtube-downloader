from pytube import YouTube

if __name__ == '__main__':
    
    url = input('Enter the URL:')
    output = input('Specify ouput path:')

    print('Downloading.....')
    video = YouTube(url)
    video.streams.get_highest_resolution().download(output_path=output)
    print('Download complete!')

