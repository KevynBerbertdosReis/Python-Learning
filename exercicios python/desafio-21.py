#faça um programa em python que abra e reproduza o audio de um arquivo mp3. 
link = input('Digite o caminho do arquivo mp3:')
from pytubefix import YouTube
from pytubefix.cli import on_progress
yt = YouTube(link, on_progress_callback=on_progress)
print(yt)