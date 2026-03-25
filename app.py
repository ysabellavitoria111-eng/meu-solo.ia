import streamlit as st
import yt_dlp
import os
from basic_pitch.inference import predict

st.title("🎸 IA Tiradora de Solos")
url = st.text_input("Cole o link do TikTok, Insta ou YouTube:")

if st.button("🚀 Gerar Solo Agora"):
    if url:
        st.write("📥 Baixando e ouvindo o solo...")
        # Lógica de download e IA aqui...
        ydl_opts = {'format': 'bestaudio/best', 'outtmpl': 'audio.mp3'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        # IA tirando de ouvido
        model_output, midi_data, note_events = predict("audio.mp3")
        
        st.audio("audio.mp3")
        st.success("Solo extraído! Veja as notas abaixo:")
        
        # Mostra a "tabela" de números
        for n in midi_data.instruments[0].notes[:20]:
            st.write(f"🎵 Nota MIDI: {n.pitch} | Sugestão de Traste: {n.pitch - 40}")
    else:
        st.error("Coloque um link válido!")
