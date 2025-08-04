import streamlit as st
import numpy as np
import soundfile as sf
import tempfile
import os
from kokoro import KPipeline
import uuid
from pathlib import Path
import warnings

# Suppress warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
# Suppress specific torch warnings
warnings.filterwarnings("ignore", message="dropout option adds dropout after all but last recurrent layer")
warnings.filterwarnings("ignore", message="`torch.nn.utils.weight_norm` is deprecated")

# Configure page
st.set_page_config(
    page_title="Kokoro TTS UI",
    page_icon="🎤",
    layout="wide"
)

# Language and voice mapping based on voices.md
LANGUAGES = {
    'a': 'American English 🇺🇸',
    'b': 'British English 🇬🇧', 
    'j': 'Japanese 🇯🇵',
    'z': 'Mandarin Chinese 🇨🇳',
    'e': 'Spanish 🇪🇸',
    'f': 'French 🇫🇷',
    'h': 'Hindi 🇮🇳',
    'i': 'Italian 🇮🇹',
    'p': 'Brazilian Portuguese 🇧🇷'
}

VOICES = {
    'a': {
        'af_heart': '🚺❤️ af_heart',
        'af_alloy': '🚺 af_alloy',
        'af_aoede': '🚺 af_aoede', 
        'af_bella': '🚺🔥 af_bella',
        'af_jessica': '🚺 af_jessica',
        'af_kore': '🚺 af_kore',
        'af_nicole': '🚺🎧 af_nicole',
        'af_nova': '🚺 af_nova',
        'af_river': '🚺 af_river',
        'af_sarah': '🚺 af_sarah',
        'af_sky': '🚺 af_sky',
        'am_adam': '🚹 am_adam',
        'am_echo': '🚹 am_echo',
        'am_eric': '🚹 am_eric',
        'am_fenrir': '🚹 am_fenrir',
        'am_liam': '🚹 am_liam',
        'am_michael': '🚹 am_michael',
        'am_onyx': '🚹 am_onyx',
        'am_puck': '🚹 am_puck',
        'am_santa': '🚹 am_santa'
    },
    'b': {
        'bf_alice': '🚺 bf_alice',
        'bf_emma': '🚺 bf_emma',
        'bf_isabella': '🚺 bf_isabella',
        'bf_lily': '🚺 bf_lily',
        'bm_daniel': '🚹 bm_daniel',
        'bm_fable': '🚹 bm_fable',
        'bm_george': '🚹 bm_george',
        'bm_lewis': '🚹 bm_lewis'
    },
    'j': {
        'jf_alpha': '🚺 jf_alpha',
        'jf_gongitsune': '🚺 jf_gongitsune',
        'jf_nezumi': '🚺 jf_nezumi',
        'jf_tebukuro': '🚺 jf_tebukuro',
        'jm_kumo': '🚹 jm_kumo'
    },
    'z': {
        'zf_xiaobei': '🚺 zf_xiaobei',
        'zf_xiaoni': '🚺 zf_xiaoni',
        'zf_xiaoxiao': '🚺 zf_xiaoxiao',
        'zf_xiaoyi': '🚺 zf_xiaoyi',
        'zm_yunjian': '🚹 zm_yunjian',
        'zm_yunxi': '🚹 zm_yunxi',
        'zm_yunxia': '🚹 zm_yunxia',
        'zm_yunyang': '🚹 zm_yunyang'
    },
    'e': {
        'ef_dora': '🚺 ef_dora',
        'em_alex': '🚹 em_alex',
        'em_santa': '🚹 em_santa'
    },
    'f': {
        'ff_siwis': '🚺 ff_siwis'
    },
    'h': {
        'hf_alpha': '🚺 hf_alpha',
        'hf_beta': '🚺 hf_beta',
        'hm_omega': '🚹 hm_omega',
        'hm_psi': '🚹 hm_psi'
    },
    'i': {
        'if_sara': '🚺 if_sara',
        'im_nicola': '🚹 im_nicola'
    },
    'p': {
        'pf_dora': '🚺 pf_dora',
        'pm_alex': '🚹 pm_alex',
        'pm_santa': '🚹 pm_santa'
    }
}

# Initialize session state
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if 'generated_audio_path' not in st.session_state:
    st.session_state.generated_audio_path = None

if 'generated_filename' not in st.session_state:
    st.session_state.generated_filename = None

def cleanup_previous_audio():
    """Remove previous audio file if exists"""
    if st.session_state.generated_audio_path and os.path.exists(st.session_state.generated_audio_path):
        try:
            os.remove(st.session_state.generated_audio_path)
        except:
            pass
    st.session_state.generated_audio_path = None
    st.session_state.generated_filename = None

@st.cache_resource
def load_pipeline(lang_code):
    """Load Kokoro pipeline with caching for better performance"""
    return KPipeline(lang_code=lang_code, repo_id='hexgrad/Kokoro-82M')

def generate_audio(text, lang_code, voice, speed):
    """Generate audio using Kokoro pipeline"""
    try:
        # Clean up previous audio
        cleanup_previous_audio()
        
        # Create pipeline with caching
        pipeline = load_pipeline(lang_code)
        
        # Generate audio
        generator = pipeline(text=text, voice=voice, speed=speed)
        
        audio_chunks = []
        for i, (gs, ps, audio) in enumerate(generator):
            audio_chunks.append(audio)
        
        if audio_chunks:
            full_audio = np.concatenate(audio_chunks).astype('float32')
            
            # Create temporary file for this session
            temp_dir = Path(tempfile.gettempdir()) / "kokoro_ui" / st.session_state.session_id
            temp_dir.mkdir(parents=True, exist_ok=True)
            
            # Create filename: first 15 chars + voice + timestamp
            import datetime
            text_prefix = text[:15].replace(" ", "_").replace("\n", "_")
            # Remove special characters that might cause issues
            text_prefix = "".join(c for c in text_prefix if c.isalnum() or c in "_-")
            timestamp = datetime.datetime.now().strftime("%y%m%d%H%M%S")
            filename = f"{text_prefix}_{voice}_{timestamp}.wav"
            output_path = temp_dir / filename
            
            # Save audio file
            sf.write(str(output_path), full_audio, 24000)
            
            # Update session state
            st.session_state.generated_audio_path = str(output_path)
            st.session_state.generated_filename = filename
            
            return True, str(output_path), filename
        else:
            return False, None, None
            
    except Exception as e:
        return False, str(e), None

# Main UI
st.title("🎤 Kokoro TTS Generator")
st.markdown("Convert text to speech using Kokoro AI voices")

# Create two columns
col1, col2 = st.columns([1, 1])

with col1:
    st.header("Settings")
    
    # Text input
    text_input = st.text_area(
        "Input Text",
        max_chars=500,
        height=150,
        help="Up to 500 characters per Generate.",
        placeholder="Enter your text here..."
    )
    
    # Character counter
    char_count = len(text_input) if text_input else 0
    st.caption(f"Characters: {char_count}/500")
    
    # Language selection
    selected_lang_code = st.selectbox(
        "Language",
        options=list(LANGUAGES.keys()),
        format_func=lambda x: LANGUAGES[x],
        index=8  # Default to Brazilian Portuguese
    )
    
    # Voice selection (filtered by language)
    available_voices = VOICES.get(selected_lang_code, {})
    if available_voices:
        selected_voice = st.selectbox(
            "Voice",
            options=list(available_voices.keys()),
            format_func=lambda x: available_voices[x]
        )
    else:
        st.warning("No voices available for selected language")
        selected_voice = None
    
    # Speed slider
    speed = st.slider(
        "Speed",
        min_value=0.1,
        max_value=2.0,
        value=1.0,
        step=0.1,
        help="Adjust the speech speed"
    )
    
    # Generate button
    generate_btn = st.button(
        "🎵 Generate",
        type="primary",
        use_container_width=True
    )

with col2:
    st.header("Generated Audio")
    
    if generate_btn:
        if not text_input:
            st.error("Please enter some text to generate audio.")
        elif not selected_voice:
            st.error("Please select a voice.")
        else:
            with st.spinner("Generating audio..."):
                success, audio_path, filename = generate_audio(
                    text_input, 
                    selected_lang_code, 
                    selected_voice, 
                    speed
                )
            
            if success:
                st.success("Audio generated successfully!")
            else:
                st.error(f"Error generating audio: {audio_path}")
    
    # Display audio player and download if audio exists
    if st.session_state.generated_audio_path and os.path.exists(st.session_state.generated_audio_path):
        st.subheader("🎧 Audio Player")
        
        # Audio player
        with open(st.session_state.generated_audio_path, 'rb') as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
        
        # File info and download
        st.subheader("📁 File Download")
        
        #col_info, col_download = st.columns([1, 1])
        
        #with col_info:
        st.info(f"**Filename:** {st.session_state.generated_filename}")
            
        #with col_download:
        st.download_button(
            label="Download WAV",
            data=audio_bytes,
            file_name=st.session_state.generated_filename,
            mime="audio/wav",
            icon=":material/download:",
            use_container_width=True
        )
    else:
        st.info("Click 'Generate' to create audio")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "Powered by <a href='https://github.com/hexgrad/kokoro' target='_blank'>Kokoro TTS</a>"
    "</div>", 
    unsafe_allow_html=True
)

# Cleanup on app restart (optional)
import atexit

def cleanup_temp_files():
    """Clean up temporary files on exit"""
    temp_base = Path(tempfile.gettempdir()) / "kokoro_ui"
    if temp_base.exists():
        import shutil
        try:
            shutil.rmtree(temp_base)
        except:
            pass

atexit.register(cleanup_temp_files)
