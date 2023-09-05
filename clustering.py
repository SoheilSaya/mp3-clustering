from preprocessing import cleaning
from IPython import display

import numpy as np
import pandas as pd
import shutil
import hazm
import requests
import time
import traceback
import torch
from sentence_transformers import models, SentenceTransformer, util
from sklearn.cluster import KMeans
def rtl_print(outputs, font_size="15px", n_to_br=False):
    outputs = outputs if isinstance(outputs, list) else [outputs] 
    if n_to_br:
        outputs = [output.replace('\n', '<br/>') for output in outputs]
        
    outputs = [f'<p style="text-align: right; direction: rtl; margin-right: 10px; font-size: {font_size};">{output}</p>' for output in outputs]
    display.display(display.HTML(' '.join(outputs)))

    
def load_st_model(model_name_or_path):
    word_embedding_model = models.Transformer(model_name_or_path)
    pooling_model = models.Pooling(
        word_embedding_model.get_word_embedding_dimension(),
        pooling_mode_mean_tokens=True,
        pooling_mode_cls_token=False,
        pooling_mode_max_tokens=False)
    
    model = SentenceTransformer(modules=[word_embedding_model, pooling_model])
    return model
# Corpus with example sentences
corpus = [
'Aref - Gole Golkhooneh.mp3',
           'Aref - Soltane Ghalbha.mp3'

           ,
           'Aron Afshar - Eshgh.mp3'
           ,
           'Dariush - Age Ye Rooz_GuitarMusic.mp3'
           ,
           'Dariush - Ahay Mardome Donya_GuitarMusic.mp3'
           ,

           'Habib_-_Shabe_Jodayee.mp3'
           ,
           'Habib_-_Shabe_Siah.mp3'
           ,
           'Habib_-_Shahla.mp3'
]
# Import the os module
import os

# Create an empty list to store the mp3 files
mp3_list = []

# Loop through the files in the current directory
for file in os.listdir("."):
    # Check if the file has the .mp3 extension
    if file.endswith(".mp3"):
        # Append the file name to the mp3 list
        mp3_list.append(file)

# Print the mp3 list
print(mp3_list)
corpus=mp3_list
num_clusters = 100

def rtl_print(outputs, n_to_br=False):
    outputs = outputs if isinstance(outputs, list) else [outputs] 
    if n_to_br:
        outputs = [output.replace('\n', '<br/>') for output in outputs]
                    
    outputs = [output.strip('<p>').strip('</p>').strip() for output in outputs]
    for output in outputs:
        print(output)

    # Load the Sentence-Transformer


embedder = load_st_model('m3hrdadfi/bert-fa-base-uncased-wikinli-mean-tokens')
corpus_embeddings = embedder.encode(corpus, show_progress_bar=True)

# Perform kmean clustering
clustering_model = KMeans(n_clusters=num_clusters)
clustering_model.fit(corpus_embeddings)
cluster_assignment = clustering_model.labels_

clustered_sentences = [[] for i in range(num_clusters)]
for sentence_id, cluster_id in enumerate(cluster_assignment):
    clustered_sentences[cluster_id].append(corpus[sentence_id])

for i, sentences in enumerate(clustered_sentences):
    rtl_print(f'Cluster: {i + 1}', '20px')

    rtl_print(sentences)
    rtl_print('- - ' * 50)
# Assume the current directory is called source_dir
source_dir = os.getcwd()

# Iterate over the list of lists
for file_list in clustered_sentences:
    try:
        if len(file_list[0].split(" "))>1:
            namestr=f'{file_list[0].split(" ")[0]} {file_list[0].split(" ")[1]}'
        else:
            namestr=f'{file_list[0].split(" ")[0]}'
        print(len(file_list))
        print(file_list)
        print(file_list[0])
        print(file_list[0].split(" ")[0],file_list[0].split(" ")[1])
        # Create a folder name based on the first file in each inner list
        namestr=f'{file_list[0].split(" ")[0]} {file_list[0].split(" ")[1]}'
        folder_name = namestr
        # Create the destination directory path
        dest_dir = os.path.join(source_dir, folder_name)
        # Make the destination directory if it does not exist
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        # Iterate over the files in each inner list
        for file in file_list:
            #try:
                # Create the source file path
                src_path = os.path.join(source_dir, file)
                # Create the destination file path
                dest_path = os.path.join(dest_dir, file)
                # Move the file from source to destination
                shutil.move(src_path, dest_path)
            #except:
            #    print(Exception)
            #    traceback.print_exc ()
    except:
        print(Exception)
        traceback.print_exc ()
        

