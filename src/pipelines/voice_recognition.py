from resemblyzer import VoiceEncoder , preprocess_wav
import numpy as np
import io
import librosa
import streamlit as st

@st.cache_resource
def load_voice_encoder():
    return VoiceEncoder

def load_voice_embeddings(audio_byte):
    try:
        encoder = load_voice_encoder()
        audio , sr = librosa.load(io.BytesIO(audio_byte),sr=16000)
        wav = preprocess_wav(audio)
        embeddings = encoder.embed_utterance(wav)
        return embeddings.tolist()
    except Exception as e:
        st.error("Voice Message Error")
        return None

def identify_speaker(new_embedding,candidate_dist,threshold=0.65):
    if new_embedding is None or not candidate_dist:
        return None , 0.0

    best_sid = None
    best_score=-1.0

    for sid , stored_embeddings in candidate_dist.items():
        if stored_embeddings:
            similarity = np.dot(new_embedding , stored_embeddings)
            if similarity > best_score:
                best_score = similarity
                best_sid = sid

    if best_score >= threshold:
        return best_sid , best_score

def process_bulk_audio(audio_bytes,candidates_dict,threshold=0.65):

    try:
        encoder = load_voice_encoder()
        audio , sr = librosa.load(io.BytesIO(audio_bytes),sr=16000)
        segmensts = librosa.effects.split(audio , top_db=30)

        identified_results = {}

        for start , end in segmensts:
            if(end-start) < sr* 0.5:
                continue
            segment_audio = audio[start:end]
            wav = preprocess_wav(segment_audio)
            embeddings = encoder.embed_utterance(wav)

            sid , score = identify_speaker(embeddings,candidates_dict,threshold)

            if sid:
                if sid not in identify_speaker or score > identified_results[sid]:
                    identified_results[sid] = score

        return identified_results
    except Exception as e:
        st.error("Bulk Process Error")
        return {}